# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:16:37 2019

@author: g440051
"""
#storing dict values, if they are repeated keys add values
#n = int(input())
#l1 = []
#
#for i in range(0,n):
#    l1.append(str(input()))
#    
#print(l1)
#
#s1 = set(l1)
#print(len(s1))


from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
print(words)   
print(len(words))
print(*words.values())