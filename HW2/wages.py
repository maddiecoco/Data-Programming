# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Tue Sep 20 10:37:42 2022

File: wages.py
    
Description
"""
def main():
    
#Ask what day
    date = input("Which day should we analyze? ")
    profitfile = "profits_" + date + ".txt"
    employeefile = "employees_" + date + ".txt"

#Read in the data from files
    with open(profitfile, "r") as infile:
        profit_glazed = float(infile.readline())
        profit_chocolate = float(infile.readline())
        profit_sprinkled = float(infile.readline())
    
    with open(employeefile, "r") as infile:
        num_employees = int(infile.readline())
        hours_worked = int(infile.readline())

#Compute the profit, hours worked, and calculate wage
    total_profit = profit_glazed + profit_chocolate + profit_sprinkled
    total_hours = num_employees * hours_worked
    print("On", date, ",you made: $", total_profit)
    print(num_employees, "worked for", hours_worked, "hours each, totaling", total_hours, "hours.")

    wage = float(total_profit / total_hours)

    print("You should pay your employees $", round(wage, 2), "per hour.")
    
main()  