# -*- coding: utf-8 -*-
"""
Madeline Coco
DS 2000: Intro to Programming with Data

Created on Tue Sep 13 13:18:59 2022

File: light.py
    
Description: Calculating light travel time based on distance input
"""

lightspeed_mps = 299792458

distance_miles = float(input("Enter Distance [in miles]: "))

distance_meters = distance_miles * 1.61 * 1000

#speed = distance/time so time = distance/speed

time_total = distance_meters / lightspeed_mps

#convert time to read in hrs, mins, seconds

time_hrs = int(time_total / 3600)

time_mins = int((time_total % 3600)/60)

time_secs = round((time_total % 60), 1)

print("Light travel time: ", time_hrs, "h", time_mins, "m", time_secs, "s")
