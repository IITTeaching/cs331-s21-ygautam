import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')

#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:
  x = lst

  for i in range(0,len(lst)-1):
    for j in range(i,len(lst)):
      if(compare(x[i],x[j])==1):
        y = x[j]
        z = x[i]
        x[i] = y
        x[j] = z



  return x




def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
  x = 0
  y = len(lst)-1

  while x <= y:
    z = int((x+y)/2)

    if (compare(lst[z],elem)==-1):
      x = z+1
    if(compare(lst[z],elem)==1):
      y = z-1
    if(compare(lst[z],elem)==0):
      return z

  return -1

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)

#################################################################################
# EXERCISE 2
#################################################################################
class PrefixSearcher():
    x = []
    k = 0
    def __init__(self, document, k):
      self.k = k
      for i in range(0,len(document)-k):
        self.x.append(document[i:i+k])
      if(len(document)/k != len(document)//k):
         for i in range(0,k):
          self.x.append(document[len(document)-k+1:len(document)])
      thing = lambda x,y: 0 if x==y else (-1 if x<y else 1)
      self.x = mysort(self.x,thing)






    def search(self, q):
      if(len(q)>self.k):
        raise Exception("q too big ")
      thing = lambda x,y: 0 if x==y else (-1 if x<y else 1)
      if(mybinsearch(self.x,q,thing)!=-1):
        return True
      return False

# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'http://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

#################################################################################
# EXERCISE 3
#################################################################################
class SuffixArray():
    document = ""
    x = []
    def __init__(self, document: str):
      self.document = document
      for i in range(0,len(document)):
        self.x.append(i)
        thing = lambda x,y: 0 if self.document[x:]==self.document[y:] else (-1 if self.document[x:]<self.document[y:] else 1)
      self.x = mysort(self.x,thing)



    def positions(self, searchstr:str):
      output = []
      x = 0
      y = len(self.x)-1
      while x<=y:
        z = int((x+y)/2)

        if(self.document[self.x[z]:self.x[z]+len(searchstr)]<searchstr):
          x = z+1
        if(self.document[self.x[z]:self.x[z]+len(searchstr)]>searchstr):
          y=z-1
        if(self.document[self.x[z]:self.x[z]+len(searchstr)]==searchstr):

          output.append(self.x[z])

          temp = z

          z = z- 1
          while(self.document[self.x[z]:self.x[z]+len(searchstr)]==searchstr):
            output.append(self.x[z])
            z = z - 1
          while(self.document[self.x[temp]:self.x[temp]+len(searchstr)]==searchstr):
            output.append(self.x[z])
            temp = temp + 1

          return output
      return output

    def contains(self, searchstr: str):

      if(self.positions(searchstr)==[]):
        return False
      return True
# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'http://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
<<<<<<< HEAD
    print(md_text[0:1000])
    # tc.assertTrue(s.contains("Moby Dick"))
    # tc.assertTrue(s.contains("Herman Melville"))
    # tc.assertEqual(s.positions("Moby Dick"), [427])
=======
    tc.assertTrue(s.contains("Moby-Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
    posset = set(s.positions("Moby-Dick"))
    tc.assertEqual(posset, {355, 356})
>>>>>>> 510e22a975f6dab2cb5e6d567c1e36a37e3e9033


#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
