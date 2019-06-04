#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:36:58 2019

@author: kartiktanksali
"""

#Binary search to search first or last occurence



def binarySeachFirstOccurence(lst,ele):
    
    start = 0
    end = len(lst)-1
    result = -1
    
    while(start<=end):
        mid = int(start + (end-start)/2)
        
        if lst[mid] == ele:
            result = mid
            end = mid - 1
        elif ele < lst[mid]:
            end = mid - 1
        elif ele > lst[mid]:
            start = mid + 1
    
    return result
            
def binarySeachLastOccurence(lst,ele):
    
    start = 0
    end = len(lst)-1
    result = -1
    
    while(start<=end):
        mid = int(start + (end-start)/2)
        
        if lst[mid] == ele:
            result = mid
            start = mid + 1
        elif ele < lst[mid]:
            end = mid - 1
        elif ele > lst[mid]:
            start = mid + 1
    
    return result
        



lst = [1,2,3,4,10,10,10,20,30,99]

ele = int(input("Enter the element to be searched: "))

res = binarySeachFirstOccurence(lst,ele)
res1 = binarySeachLastOccurence(lst,ele)

if res and res1 != -1:
    print(f"Element {ele} first occurance at {res}")
    print(f"Element {ele} last occurance at {res1}")
    
else:
    print("Element not found")