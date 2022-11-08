# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Thu Sep 29 08:25:45 2022

File: walk.py
    
Description: Tracks the position of a rabbit for 1000 seconds
"""

def main():
    
    import random as rnd
    import matplotlib.pyplot as plt
    position = 0
    second_count = 1
    total_seconds = 1000
    position_list = []
    second_list = []

#Generate random number to decide what direction the squirrel is walking each second    
    while second_count < total_seconds:
        rand = rnd.randint(1,2)
        if rand == 1:
            position = position + 1
        else:
            position = position - 1
        position_list.append(position)
        second_list.append(second_count)
        second_count = second_count + 1
        
#Plot the findings        
    plt.plot(second_list, position_list, 'o')
    plt.xlabel("Seconds")
    plt.ylabel("Position")
    plt.title("Position vs. Time of Squirrel")
    plt.savefig("walk.png", bbox_inches="tight")
    plt.show()
main()