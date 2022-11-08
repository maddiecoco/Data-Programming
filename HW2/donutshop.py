# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Tue Sep 20 10:22:06 2022

File: donutshop.py
    
Description: Calculate profit and customer cost of donuts after reading in files
"""

def main():
    print("Welcome to the Donut Shop!")

#Find out which file is being read
    donut_type = input("What kind of donut do you want[glazed, chocolate, sprinkled]? ")
    filename = donut_type + ".txt"

    with open(filename, "r") as infile:
        donut_price = float(infile.readline())
        ingredient_cost = float(infile.readline())
    
    donut_number = int(input("How many donuts are you purchasing? "))

#Compute costs and profit based on type of donut and number ordered
    customer_cost = donut_price * donut_number
    business_cost = ingredient_cost * donut_number
    profit = customer_cost - business_cost

    print("Please pay $", customer_cost)
    print("This sale made us $", round(profit, 2))
    print("Enjoy your donuts!")
    
main()