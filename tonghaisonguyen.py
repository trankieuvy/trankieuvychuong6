# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:29:26 2024

@author: Admin
"""
a=int(input("nhập vào số nguyên có 2 chữ số: "))
if (10<=a <=99):
    
    phandu= a%10
    phannguyen= a//10
    print("tổng các chữ số của N: ", phandu+phannguyen)
else:
    print("cú pháp sai")
    