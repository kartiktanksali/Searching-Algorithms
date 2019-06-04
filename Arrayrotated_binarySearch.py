#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 01:05:32 2019

@author: kartiktanksali
"""

#How many times a the array has been rotated

def binarySearchRotationCount(lst):
    
    start = 0
    end = len(lst)-1
    n = len(lst)
    
    while(start <= end):
        if lst[start] < lst[end]:
            return start
        else:
            mid = int(start + (end-start)/2)
            next1 = int((mid+1)%n)
            prev = int((mid+n-1)%n)
            
            if lst[mid] <= lst[next1] and lst[mid] <= lst[prev]:
                return mid
            elif lst[mid] <= lst[end]:
                end = mid - 1
            elif lst[mid] >= lst[start]:
                start = mid + 1


lst = [20,30,99,1,2,3,4,10]


res = binarySearchRotationCount(lst)

print(res)