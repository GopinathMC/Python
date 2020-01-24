# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:09:10 2019

@author: g440051
"""

#n,m = int,(input()).split()
#
#l = input().split()
#
#A = set(map(int,input().split()))
#B = set(map(int,input().split()))


#code to change the cases


def swapcases(s):
    a=""
    for i in s:
        if i.isupper() == True:
            a+=(i.lower())
        else:
            a+=(i.upper())
    return a
        
print(swapcases(input()))
