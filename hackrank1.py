# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:13:07 2019

@author: g440051
"""
#n = int(input())
#print(range(1,(n+1)),sep='')

#print(*range(1,3))

x,y,z,n = (int(input()) for _ in range(0,4))

print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k)!=n])

#line(17 to 24, getting second max from a list)-----------------------------------------------
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
large = max(arr)

while max(arr) == large:
    arr.remove(max(arr))
print(max(arr))

#(27 to 37)getting name&marks in runtime, printing the name where their marks are second lowest---------
n = int(input())

marksheet = [[input(),float(input())] for _ in range(n)]

print(marksheet)

l1 = sorted(set(mark for name,mark in marksheet))[1]
print(l1)

n1 = '\n'.join([name for name,mark in sorted(marksheet) if mark == l1])
print(n1)