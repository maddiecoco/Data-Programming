# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Tue Sep 20 10:05:03 2022

File: applecider.py
    
Description: Reading files and determining max and min values from a list
"""
def main():

#Ask which list to read in
    filename = input("Which rating list would you like to read? ")

#Read in data from selected list
    with open(filename, "r") as infile:
        option_1 = (infile.readline())
        option_1_value = float(infile.readline())
        option_2 = (infile.readline())
        option_2_value = float(infile.readline())
        option_3 = (infile.readline())
        option_3_value = float(infile.readline())
        option_4 = (infile.readline())
        option_4_value = float(infile.readline())
    
#Find max and min values from selected list   
    max_num = max(option_1_value, option_2_value, option_3_value, option_4_value)
    print("Maximum rating: ", max_num)
    
    min_num = min(option_1_value, option_2_value, option_3_value, option_4_value)
    print("Minimum rating: ", min_num)

main()