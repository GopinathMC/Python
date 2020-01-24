# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:17:04 2020

@author: g440051
"""

#s = 'ABCDEFGHIJ'
#w = 4
#l = len(s)
#for i in range(0,l,w):
#    print(s[i:i+w])
    
    
    
import textwrap

def wrap(string, max_width):
    ans= ''
    l = len(string)
    for i in range(0,l,max_width):
        ans += string[i:i+max_width] + "\n"
#        print(ans)
#        print(string[i:i+max_width])
    return ans
    

if __name__ == '__main__':
    string  = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)