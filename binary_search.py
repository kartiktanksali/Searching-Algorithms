#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:16:43 2019

@author: kartiktanksali
"""

#Binary Search recursive implementation

lst = [1,2,3,4,10,20,30,99]


ele = int(input("Enter the element to be searched: "))


start = 0
end = len(lst)-1
flag = False
while(start <= end):
    mid = int(start + (end-start) /2)
    
    if lst[mid] == ele:
        print(f"The element {ele} was found at index {mid}")
        flag = True
        break
    elif ele < lst[mid]:
        end = mid-1
    elif ele > lst[mid]:
        start = mid+1

if flag == False:
    print("Element not present")
