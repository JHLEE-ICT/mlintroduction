# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:20:50 2019

@author: JIHYUN
"""

num = eval(input("몇 개의 품목을 구입하십니까? "))

if(num<=10):
    price = 12
elif(num<=99):
    price = 10
else:
    price = 7

total_price = num * price
print("총 비용은 ", total_price, "달러입니다. ")