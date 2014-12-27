#!/usr/bin/python

"""A tuple is a sequence of values much like a list. 
The values stored in a tuple can be any type, and they are indexed by integers. 
The important difference is that tuples are immutable. 
Tuples are also comparable and hashable so we can sort lists of them and use tuples as key values in Python dictionaries"""

"""Description:   sort list of words from longest to shortest"""

import os 

os.system('clear')

txt = 'i love ted talks , its a great learning experience from different people  '
words = txt.split()
t = list()
for word in words:
   t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print "\nIntial list of words : \n",txt
print "\nsorted list of words from longest to shortest: \n",res
print "\n"
