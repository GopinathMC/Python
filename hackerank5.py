# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:14:09 2019

@author: g440051
"""


#s= set()
#p= set()
#q= set()
#r= set()
#
#
#a,b = (int(input()),input().split())
#c,d = (int(input()),input().split())
#
#p = set(b)
#s = set(d)
#q=s.difference(p)
#r=p.difference(s)
#print(q.union(r))

a,b=(input(),input().split())
c,d=(input(),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))
