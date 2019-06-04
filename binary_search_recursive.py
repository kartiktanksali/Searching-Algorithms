#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:45:00 2019

@author: kartiktanksali
"""






def binarySearch(lst,start,end,ele):
    mid = int(start + (end-start)/2)
   
    if end >= start:

        if lst[mid] == ele:
            return f"Element {ele} found at index {mid}"
        elif ele < lst[mid]:
            return binarySearch(lst,start,mid-1,ele)
        elif ele > lst[mid]:
            return binarySearch(lst,mid+1,end,ele)
    else:
        return -1
    
    
lst = [1,2,3,4,10,20,30,99]

ele = int(input("Enter the element to be searched: "))

res = binarySearch(lst,0,len(lst)-1,ele)

if res != -1:
    print(res)
else:
    print("Element not found")