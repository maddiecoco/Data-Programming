# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Sep 28 19:00:24 2022

File: change.py
    
Description: Displays the breakdown of change owed in different coins
"""
def main():

#Ask user to input price. Ensure it is between 1 and 100
    price = int(input("Enter price in cents: "))
    if price < 1 or price > 100:
        print("You entered an invalid price. Please enter a number 1-100.")
    else:
        change_owed = 100 - price
    
        print("Change to be given back:", change_owed)

#Calculate number of each coin
        quarters = int(change_owed / 25)
    
        change_owed = change_owed - (quarters * 25)
    
        dimes = int(change_owed / 10)
    
        change_owed = change_owed - (dimes * 10)
    
        nickels = int(change_owed / 5)
    
        change_owed = change_owed - (nickels * 5)
    
        pennies = int(change_owed)

#Print number of coins given for change    
        print("Quarters back: ", quarters)
        print("Dimes back: ", dimes)
        print("Nickels back: ", nickels)
        print("Pennies back: ", pennies)
    
main()
