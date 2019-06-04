#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:11:34 2019

@author: kartiktanksali
"""

#Linear Search

lst = [10,20,50,5,12,40,60,30]

ele = int(input("Enter the element to be searched: "))

flag = False
ind = 0

for i in range(0,len(lst)):
    if lst[i] == ele:
        print(f"Element {ele} found at index {i}")
        break
        