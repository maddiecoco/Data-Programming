# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Oct 19 17:49:36 2022

File: exoplanet.py
    
Description: read in a file with many lines of data on different planets, and then use
that data to find the most similar planet to earth and visualize the planets on a scatterplot.

    MOST SIMILAR PLANET TO EARTH (based on euclidian score) 

    Name:  2MASS 0122-2439 B
    Mass:  0.0
    Radius:  0.0
    Period:  0.0
    Semi-Major Axis:  0.0
    Surface Temperature:  0.0
    
"""
import matplotlib.pyplot as plt

def read_data():
    filename = "exoplanets.csv"
    
    planet_list = []
    
    with open(filename,"r") as infile:
        all_lines = infile.readlines()
        
    for row in range(len(all_lines)):
        split_line = all_lines[row].strip().split(",")
        planet_traits = []
        
            
        if (row >= 34):
            #Only take necessary values for each planet and alter some
            planet_name = split_line[0]
            planet_traits.append(planet_name)
            for i in [2, 3, 4, 5, 11]: 
                if (split_line[i] == ''):
                    split_line[i] = 0.0
                split_line[i] = float(split_line[i])
            planet_mass = split_line[2] * 317.89
            planet_traits.append(planet_mass)
            planet_radius = split_line[3] * 10.97
            planet_traits.append(planet_radius)
            planet_period = split_line[4] / 365.2422
            planet_traits.append(planet_period)
            planet_axis = split_line[5]
            planet_traits.append(planet_axis)
            planet_temp = split_line[11]
            planet_traits.append(planet_temp)
            
            #Add the list of planet traits to the total planet list
            planet_list.append(planet_traits)
    return planet_list

def lookup_planet(planet_list, planet_name):
    list_of_traits = []
    empty_list = []
    for planet in planet_list:
        checking_name = planet[0]
        if (planet_name == checking_name):
            list_of_traits.append(planet[0:6])
    if(list_of_traits == empty_list):
        return "No planet of this name found in the list."
    else:
        return list_of_traits
    
def euclidean_distance(planet_list, planet_a, planet_b):
    
    a_traits = lookup_planet(planet_list, planet_a)
    b_traits = lookup_planet(planet_list, planet_b)
    combined_traits = []
    
    for i in range(1,6):
        combine = (a_traits[0][i] + b_traits[0][i]) ** 2
        combined_traits.append(combine)
    
    euclid_score = (sum(combined_traits)) ** 0.5   
    return euclid_score

def find_most_similar_planet(planet_list, planet_name):
    smallest_euclid_score = 100000000
    
    for planet in planet_list:
        checking_name = planet[0]
        if (checking_name != planet_name):
            score = euclidean_distance(planet_list, planet_name, checking_name)
            if (score < smallest_euclid_score):
                most_similar_planet = checking_name
                smallest_euclid_score = score
    return most_similar_planet

def generate_planet_report(planet_list, planet_name):
    most_similar_planet = find_most_similar_planet(planet_list, planet_name)
    planet_traits = lookup_planet(planet_list, most_similar_planet)
#write out the planet descriptors in a human-friendly way 
    print("MOST SIMILAR PLANET TO EARTH (based on euclidian score)", "\n")
    print("Name: ", planet_traits[0][0])
    print("Mass: ", planet_traits[0][1])
    print("Radius: ", planet_traits[0][2])
    print("Period: ", planet_traits[0][3])
    print("Semi-Major Axis: ", planet_traits[0][4])
    print("Surface Temperature: ", planet_traits[0][5])

def visualize_exoplanets(planet_list):
    axis_list = []
    mass_list = []
    
    for planet in planet_list:
        current_axis = planet[4]
        axis_list.append(current_axis)
        current_mass = planet[1]
        mass_list.append(current_mass)
    
    earth_traits = lookup_planet(planet_list, "Earth")
    
    plt.scatter(mass_list, axis_list, marker = '.', color = 'b')
    plt.plot(earth_traits[0][1], earth_traits[0][4], marker = "x", color = 'r')
    plt.xlabel("Mass in Earth masses")
    plt.ylabel("Axis in Astronomical Units")
    plt.title("Semimajor Axis vs. exoplanet Mass")
    plt.xscale('log')
    plt.yscale('log')
    plt.annotate("Earth", xy = (earth_traits[0][1], earth_traits[0][4]))
    plt.savefig("exoplanet", bbox_inches = "tight")
    plt.show()
    

def main():
    planet_list = read_data()
    
    lookup_planet(planet_list, "Saturn")
    
    euclidean_distance(planet_list, "Saturn", "Mars")
    
    generate_planet_report(planet_list, "Earth")
    
    visualize_exoplanets(planet_list)
    
main()