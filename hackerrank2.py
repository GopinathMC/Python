# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:15:55 2019

@author: g440051
"""
#getting marks for multiple subjects and return average
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_scores = student_marks[query_name]
    print(query_scores)
    print("{0:.6f}".format(sum(query_scores)/3))