# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Thu Sep 29 08:47:07 2022

File: walk2d.py
    
Description:
"""

def main():
    
    import random as rnd
    import matplotlib.pyplot as plt
    x_pos = 0
    y_pos = 0
    second_count = 1
    total_seconds = 1000
    x_pos_list = []
    y_pos_list = []

#Generate random numbers to decide direction of walk
#Make sure E/W have double the chance over N/S    
    while second_count < total_seconds:
        rand = rnd.randint(1,6)
        if rand == 1 or rand ==2:
            x_pos = x_pos + 1 #EAST
        elif rand == 3 or rand == 4:
            x_pos = x_pos - 1 #WEST
        elif rand == 5:
            y_pos = y_pos + 1 #NORTH
        elif rand == 6:
            y_pos = y_pos - 1 #SOUTH
        
        x_pos_list.append(x_pos)
        y_pos_list.append(y_pos)

        second_count = second_count + 1
        
#Plot the movement of the squirrel in both directions        
    plt.plot(x_pos_list, y_pos_list, 'o', color = "r")
    plt.xlabel("West to East")
    plt.ylabel("South to North")
    plt.title("Squirrel's walk in 2 dimensions")
    plt.savefig("walk2d.png", bbox_inches="tight")
    plt.show()
main()