#Question 4
def get_nesting_depth(s: str):
  x = Stack()
  currentMax = 0 
  for i in range(0,len(s)):
    current = s[i]
    if(current not in "()"):
      return -1 
    if(current == '('):
      x.push(current)
    if(len(x)>currentMax):
      currentMax=len(x)
    if(current==')'):
      if(not x.empty):
        x.pop()
      else:
        return -1
  if(not x.empty()):
    return -1
  return currentMax
  
class Stack:
  def __init__(self):
    self.data = []

  def push(self, val):
    self.data.append(val)

  def pop(self):
    assert not self.empty()
    val = self.data[-1]
    del self.data[-1]
    return val

  def peek(self):
    assert not self.empty()
    return self.data[-1]

  def empty(self):
    return self.data == []

  def __len__(self):
           return len(self.data)

  def __bool__(self):
    return not self.empty()

  def __repr__(self):
    return self.data.__repr__()

  def __str__(self):
    return self.__repr__()
  
  
  #Question 5
class AVLTree:
     class Node:
         def __init__(self, val, left=None, right=None):
             self.val = val
             self.left = left
             self.right = right

         def rotate_right(self):
             n = self.left
             self.val, n.val = n.val, self.val
             self.left, n.left, self.right, n.right = n.left, n.right, n, self.right

         def rotate_left(self):
             n = self.right
             self.val, n.val = n.val, self.val
             self.left, n.left, self.right, n.right = n, self.left, n.right, n.left

         def __repr__(self):
             return str(self.val)

         def __str__(self):
             return self.__repr__()

         @staticmethod
         def height(n):
             if not n:
                 return 0
             else:
                 return max(1+AVLTree.Node.height(n.left), 1+AVLTree.Node.height(n.right))

     def __init__(self):
         self.size = 0
         self.root = None

     @staticmethod
     def rebalance(t):
         if AVLTree.Node.height(t.left) > AVLTree.Node.height(t.right):
             if AVLTree.Node.height(t.left.left) >= AVLTree.Node.height(t.left.right):
                 t.rotate_right()
             else:
                 t.left.rotate_left()
                 t.rotate_right()
         else:
             if AVLTree.Node.height(t.right.right) >= AVLTree.Node.height(t.right.left):
                 t.rotate_left()
             else:
                 t.right.rotate_right()
                 t.rotate_left()

     def min(self):
        if(len(self)==0):
          return None
        x = self.root
        while(x.left):
          x = x.left
        return x.val


     def max(self):
       if(len(self)==0):
         return None
       x = self.root
       while(x.right):
          x = x.right
       return x.val

     def next(self,v):
       y = self.root
       found = False
       final = None
       while(y and not found):
         if(y.val == v):
           found = True
         if(y.val>v):
           final = y #tracks potential finals as it travels through
           y=y.left #go through 
         if(y.val<v):
           y=y.right #go through
       if(not found):
         return None #Not in the tree
       if(y.right):
         final = y.right #bigger one
         while(final.left):# go down smaller
           final = final.left#Directly bigger one 

        
       return final
      
       
         

     def add(self, val):
         assert(val not in self)
         def add_rec(node):
             if not node:
                 return AVLTree.Node(val)
             elif val < node.val:
                 node.left = add_rec(node.left)
             else:
                 node.right = add_rec(node.right)
             if abs(AVLTree.Node.height(node.left) - AVLTree.Node.height(node.right)) >= 2:
                 AVLTree.rebalance(node)
             return node
         self.root = add_rec(self.root)
         self.size += 1

     def __delitem__(self, val):
         assert(val in self)
         def delitem_rec(node):
             to_fix = [node]

             if val < node.val:
                 node.left = delitem_rec(node.left)
             elif val > node.val:
                 node.right = delitem_rec(node.right)
             else:
                 if not node.left and not node.right:
                     return None
                 elif node.left and not node.right:
                     return node.left
                 elif node.right and not node.left:
                     return node.right
                 else:
                     t = node.left
                     if not t.right:
                         node.val = t.val
                         node.left = t.left
                     else:
                         to_fix.append(t)
                         n = t
                         while n.right.right:
                             n = n.right
                             to_fix.append(n)
                         t = n.right
                         n.right = t.left
                         node.val = t.val
             while to_fix:
                 n = to_fix.pop()
                 if abs(AVLTree.Node.height(n.left) - AVLTree.Node.height(n.right)) >= 2:
                     AVLTree.rebalance(n)
             return node

         self.root = delitem_rec(self.root)
         self.size -= 1

     def __contains__(self, val):
         def contains_rec(node):
             if not node:
                 return False
             elif val < node.val:
                 return contains_rec(node.left)
             elif val > node.val:
                 return contains_rec(node.right)
             else:
                 return True
         return contains_rec(self.root)

     def __len__(self):
         return self.size

     def __iter__(self):
         def iter_rec(node):
             if node:
                 yield from iter_rec(node.left)
                 yield node.val
                 yield from iter_rec(node.right)
         yield from iter_rec(self.root)

     def pprint(self, width=64):
         """Attempts to pretty-print this tree's contents."""
         height = self.height()
         nodes  = [(self.root, 0)]
         prev_level = 0
         repr_str = ''
         while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                 prev_level = level
                 repr_str += '\n'
            if not n:
                 if level < height-1:
                     nodes.extend([(None, level+1), (None, level+1)])
                 repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                 if n.left or level < height-1:
                     nodes.append((n.left, level+1))
                 if n.right or level < height-1:
                     nodes.append((n.right, level+1))
                 repr_str += '{val:^{width}}'.format(val=n.val, width=width//2**level)
         print(repr_str)

     def height(self):
        def height_rec(t):
             if not t:
                 return 0
             else:
                 return max(1+height_rec(t.left), 1+height_rec(t.right))
        return height_rec(self.root)

#Question 6 
def sortavl(l):
  thing = AVLTree()
  for i in range(len(l)):
    thing.add(l[i])
  x = []*len(l)
  y = thing.min()
  for i in range(len(thing)):
    x.append(y)
    y = thing.next(y)
    if(y):
      y=y.val
  return x


