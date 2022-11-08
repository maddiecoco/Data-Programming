# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Tue Sep 13 12:52:39 2022

File: mortgage.py
    
Description: Calculating a monthly mortgage payment
"""

print ("Welcome, please input the information below.")

P = int(input("Principal loan amount: "))
i = float(input("Annual interest rate (as a decimal): "))
y = int(input("Years to repay loan: "))

r = i / 12
n = y * 12

#Calculate monthly payment using given equation

payment = round((((P * r * ((1 + r)**n)))/(((1+r)**n)-1)), 2)

print("Monthly payment: ", payment)