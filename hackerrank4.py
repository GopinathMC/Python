# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:15:54 2019

@author: g440051
"""

#from collections import deque
#d = deque()
#for _ in range(int(input())):
#    cmd, *args = input().split()
#    getattr(d, cmd)(*args)
#[print(x, end=' ') for x in d]
#print(*d)

l = []
for _ in range(int(input())):
    cmd,*args = input().split()
    if(cmd != "print"):
        cmd += "("+",".join(args)+")"
        eval("l."+cmd)
    else:
        print(l)