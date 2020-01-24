# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:41:07 2019

@author: g440051
"""
#
#a = input()
#
#b = a.split(" ")
#c = '-'.join(b)
#
#print(c)


#code for insertion in string
#new = []
#s = input()
#l = list(s)
#n,m = input().split()
#x = int(n)
#l[x] = m
#s = ''.join(l)
#print(s)

#code for finding number of substring occurrence in main string
def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)-len(sub_string)+1):
        if (string[i:len(sub_string)+i] == sub_string):
            c+=1
        else:
            pass
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)