# -*- coding: utf-8 -*-
"""
Madeline Coco
DS 2000: Intro to Programming with Data

Created on Fri Sep 9 13:18:59 2022

File: running.py

Description: A program to calculate the average pace of a runner based on inputs
"""

print("Hello!")

#Ask how much time they ran for

mins = int(input("Enter time in minutes: "))
secs = int (input("Enter time in seconds?: "))

#Ask the distance of the run
distance_km = float(input("Enter distance of run in kilometers: "))


distance_miles = distance_km / 1.61

converted = mins * 60

time = converted + secs

pace = time/distance_miles

pace_mins = int(pace / 60)
pace_secs = round((pace % 60), 1)

print("Your average pace was ", pace_mins,  "minutes and ", pace_secs, "seconds")