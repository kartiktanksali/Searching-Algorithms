#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:51:14 2019

@author: kartiktanksali
"""

#Binary Search to find count of element


def findCount(lst,ele):
    index1 = binarySeachFirstOccurence(lst,ele)
    index2 = binarySeachLastOccurence(lst,ele)

    if index1 and index2 != -1:
        print(f"Count of {ele} in the list is {index2-index1+1}")


lst = [1,2,3,4,10,10,10,10,20,30,30,99]

ele = int(input("Enter the element to be searched: "))

findCount(lst,ele)






#MEthods to get the first occurence index and last occurence index

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
        