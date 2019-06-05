#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:19:23 2019

@author: kartiktanksali
"""

#Find element in a rotated array


def binarySearchRotationElement(lst,ele):
    n = len(lst)-1
    start = 0
    end = n
    
    while(start <= end):
        mid = int((start+end)/2)
        
        if lst[mid] == ele:
            return mid
        else:
            if lst[mid] <= lst[end]:
                if ele > lst[mid] and ele <= lst[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif lst[mid] > lst[start]:
                if ele < lst[mid] and ele >= lst[start]:
                    end = mid - 1
                else:
                    start = mid + 1





lst = [20,30,99,1,2,3,4,10]



ele = int(input("Enter the element to be found: "))

res = binarySearchRotationElement(lst,ele)

print(res)