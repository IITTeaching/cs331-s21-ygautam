import unittest
import sys
from contextlib import contextmanager
from io import StringIO

#################################################################################
# TESTING OUTPUTS
#################################################################################
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

#################################################################################
# EXERCISE 1
#################################################################################

# implement this function
def is_perfect(n):
    x = 0
    for i in range(n,1,-1):
        y = int(n/i)
        if(y*i==n):
            x+=y
    if(x==n):
        return True
    return False 

# (3 points)
def test1():
    tc = unittest.TestCase()
    for n in (6, 28, 496):
        tc.assertTrue(is_perfect(n), '{} should be perfect'.format(n))
    for n in (1, 2, 3, 4, 5, 10, 20):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))
    for n in range(30, 450):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))

#################################################################################
# EXERCISE 2
#################################################################################

# implement this function
def multiples_of_3_and_5(n):
   x = 0 
   for i in range(n-1,0,-1):
        y = int(i/3)
        z = i/3
        if((y)==z):
            x+= i
        else: 
            y = int(i/5)
            z = i/5
            if((y)==z):
                x+= i
   return x

# (3 points)
def test2():
    tc = unittest.TestCase()
    tc.assertEqual(multiples_of_3_and_5(10), 23)
    tc.assertEqual(multiples_of_3_and_5(500), 57918)
    tc.assertEqual(multiples_of_3_and_5(1000), 233168)

#################################################################################
# EXERCISE 3
#################################################################################
def integer_right_triangles(p):
    x = 0
    okay = int(p/2)
    for i in range(2,p-okay):
        for j in range(p-i,1,-1):
            z = (p-i-j)
            if((j*j)+(z*z)==(i*i)):
                x+=1
    x = x/2
    return (x)

def test3():
    tc = unittest.TestCase()
    tc.assertEqual(integer_right_triangles(60), 2)
    tc.assertEqual(integer_right_triangles(100), 0)
    tc.assertEqual(integer_right_triangles(180), 3)

#################################################################################
# EXERCISE 4
#################################################################################

# implement this function
def gen_pattern(chars):
    
    base = ""

    tres = ""

    for i in range(len(chars)-1,-1,-1):
        okay = ""
        base+= chars[i]
        for j in range(len(base)-2,-1,-1):
            okay+=base[j]
        tres=base+okay 
        print('.'.join(tres).center((len(chars)-1)*4+1,'.'))

    for i in range (len(chars)-1,0,-1):
        x = int(len(tres)/2)
        upside = ""
        
        for j in range(0,len(tres)):
            if(j!=x and j!= x+1):
                upside+=tres[j]
        tres = upside
        print('.'.join(tres).center((len(chars)-1)*4+1,'.'))



def test4():
    tc = unittest.TestCase()
    with captured_output() as (out,err):
        gen_pattern('@')
        tc.assertEqual(out.getvalue().strip(), '@')
    with captured_output() as (out,err):
        gen_pattern('@%')
        tc.assertEqual(out.getvalue().strip(),
        """
..%..
%.@.%
..%..
""".strip())
    with captured_output() as (out,err):
        gen_pattern('ABC')
        tc.assertEqual(out.getvalue().strip(),
        """
....C....
..C.B.C..
C.B.A.B.C
..C.B.C..
....C....
""".strip())
    with captured_output() as (out,err):
        gen_pattern('#####')
        tc.assertEqual(out.getvalue().strip(),
                             """
........#........
......#.#.#......
....#.#.#.#.#....
..#.#.#.#.#.#.#..
#.#.#.#.#.#.#.#.#
..#.#.#.#.#.#.#..
....#.#.#.#.#....
......#.#.#......
........#........
""".strip())
    with captured_output() as (out,err):
        gen_pattern('abcdefghijklmnop')
        tc.assertEqual(out.getvalue().strip(),
"""
..............................p..............................
............................p.o.p............................
..........................p.o.n.o.p..........................
........................p.o.n.m.n.o.p........................
......................p.o.n.m.l.m.n.o.p......................
....................p.o.n.m.l.k.l.m.n.o.p....................
..................p.o.n.m.l.k.j.k.l.m.n.o.p..................
................p.o.n.m.l.k.j.i.j.k.l.m.n.o.p................
..............p.o.n.m.l.k.j.i.h.i.j.k.l.m.n.o.p..............
............p.o.n.m.l.k.j.i.h.g.h.i.j.k.l.m.n.o.p............
..........p.o.n.m.l.k.j.i.h.g.f.g.h.i.j.k.l.m.n.o.p..........
........p.o.n.m.l.k.j.i.h.g.f.e.f.g.h.i.j.k.l.m.n.o.p........
......p.o.n.m.l.k.j.i.h.g.f.e.d.e.f.g.h.i.j.k.l.m.n.o.p......
....p.o.n.m.l.k.j.i.h.g.f.e.d.c.d.e.f.g.h.i.j.k.l.m.n.o.p....
..p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p..
p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p
..p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p..
....p.o.n.m.l.k.j.i.h.g.f.e.d.c.d.e.f.g.h.i.j.k.l.m.n.o.p....
......p.o.n.m.l.k.j.i.h.g.f.e.d.e.f.g.h.i.j.k.l.m.n.o.p......
........p.o.n.m.l.k.j.i.h.g.f.e.f.g.h.i.j.k.l.m.n.o.p........
..........p.o.n.m.l.k.j.i.h.g.f.g.h.i.j.k.l.m.n.o.p..........
............p.o.n.m.l.k.j.i.h.g.h.i.j.k.l.m.n.o.p............
..............p.o.n.m.l.k.j.i.h.i.j.k.l.m.n.o.p..............
................p.o.n.m.l.k.j.i.j.k.l.m.n.o.p................
..................p.o.n.m.l.k.j.k.l.m.n.o.p..................
....................p.o.n.m.l.k.l.m.n.o.p....................
......................p.o.n.m.l.m.n.o.p......................
........................p.o.n.m.n.o.p........................
..........................p.o.n.o.p..........................
............................p.o.p............................
..............................p..............................
""".strip()
)

#################################################################################
# RUN ALL TESTS
#################################################################################
def main():
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()
