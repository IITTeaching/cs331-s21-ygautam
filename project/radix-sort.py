import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()
    
def sort(lst, current):
    bits = [0] * 128
    final = [None] * len(lst)
    for i in range(0,len(lst)):
      if(len(lst[i]) - 1 < current):
       x=0
      else:
       x = ord(lst[i].decode('ascii')[current])
      bits[x]+=1
    for i in range(1, len(bits)):
        bits[i] += bits[i - 1]
    for i in range(len(lst),0, -1):
        if len(lst[i-1]) - 1 < current:
            x = 0
        else:
            x = ord(lst[i-1].decode('ascii')[current])

        final[bits[x] - 1] = lst[i-1]
        bits[x] += -1

    return final



def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
  x = book_to_words()
  longest = 0
  for i in range(0,len(x)):
    
    if(len(x[i])>longest):
      longest = len(x[i])
  final = x
  for i in range(longest-2,-1,-1):
    final = sort(final,i)
  return final
  
  





print(radix_a_book())
