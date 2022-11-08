# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Oct  5 09:44:43 2022

File: rodent_reports.py
    
Description: Read in a file with data on rodent reports in the boston area
and create a scatter plot and bar graph based on the data
"""

def main():
    
    filename = "rodents_311_2021.csv"
    import matplotlib.pyplot as plt
    
    with open(filename,"r") as infile:
        header = infile.readline()
        lines = infile.readlines()
        
    index = 0
    neighborhood = []
    latitude = []
    longitude = []
    
    while index < len(lines):
        vals = lines[index].split(",")
            
        if len(vals[0]) != 0 and vals[0] != " ":
            neighborhood.append((vals[0]))
            latitude.append(float(vals[1]))
            longitude.append(float(vals[2]))
        
        index = index + 1
        
    #Plot all reports
    plt.scatter(latitude, longitude, marker = '.', color = 'blue')
    
    #Plot northeastern
    plt.plot(42.340082,-71.089488, marker = '*', color = 'r')
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Map of rodent reports in Boston 2021")
    plt.savefig("boston_rodents", bbox_inches = "tight")
    plt.show()
    
    #make list of unique neighborhoods
    unique_neighborhoods = []
    
    for neighborhood_name in neighborhood:
        if neighborhood_name not in unique_neighborhoods:
            unique_neighborhoods.append(neighborhood_name)
    unique_neighborhoods.sort()
    
    #Count number of reports for each neighborhood
    total_reports = []
    for neighborhood_name in unique_neighborhoods:
        neighborhood_reports = 0

        for i in range(len(neighborhood)):
        
            if neighborhood_name == neighborhood[i]:
                neighborhood_reports = neighborhood_reports + 1
            
        total_reports.append(neighborhood_reports)
    report_avg = sum(total_reports)/len(total_reports)
    
    #Make bar plot
    plt.bar(unique_neighborhoods, total_reports, color = ['sandybrown', 'steelblue', 'darkseagreen', 'orchid', 'mediumpurple'])
    plt.xticks(rotation = 90)
    plt.xlabel("Neighborhood")
    plt.ylabel("Number of reports")
    plt.title("Rodent reports in each neighborhood")
    plt.savefig("neighborhoods", bbox_inches = "tight")
    plt.show()
    
    #Print important information to the screen
    print("Total reports assigned to a valid neighborhood: ", len(neighborhood), "\n")
    print("Neighborhoods:")
    for unique_neighborhood in unique_neighborhoods:
        print(unique_neighborhood)
    
    print("\n","Average number of reports per neighborhood: ", report_avg)
    
main()