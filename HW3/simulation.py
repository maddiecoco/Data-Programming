# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Sep 28 19:00:34 2022

File: simulation.py
    
Description: Finding the experimental probability of 3 dice rolls being different
"""
def main():

    import random as rnd
    
    count_mismatch = 0
    roll_count = 0
    simulation_number = 1
    total_rolls = 10
    
#Create nested while loop to generate random dice rolls
    while simulation_number <= 3:
        while roll_count <= total_rolls:
            roll_count = roll_count + 1
            roll_1 = rnd.randint(1,6)
            roll_2 = rnd.randint(1,6)
            roll_3 = rnd.randint(1,6)
            
            if roll_1 != roll_2 and roll_1 != roll_3 and roll_2 != roll_3:
                count_mismatch = count_mismatch + 1  
                
        probability = count_mismatch/total_rolls
        
#print values
        print("The dice was rolled", total_rolls, "times")
        print("Number of mis-matched rolls:", count_mismatch)
        print("Experamental probability:", round(probability, 4))
        print("\n")
        
        total_rolls = total_rolls * 10
        simulation_number = simulation_number + 1

#Reset counters for rolls and mis-matched rolls
        roll_count = 0
        count_mismatch = 0
main()