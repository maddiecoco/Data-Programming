# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Nov 16 15:36:07 2022

File: final_proj.py
    
Description: A project that analyzes Uber and Lyft data in Boston neighborhoods
"""

import matplotlib.pyplot as plt

def read_cab():
    """
    This function reads in the data from the file and strips commas. Then, the data is
    stored in a list of dictionaries.
    
    Parameters: 
        N/A
        
    Returns:
        data = list of dictionaries with ride information
    """

    file_name = "cab_rides.csv"
    delimiter = ","
    coltypes = {"distance": float, "price" : float}
    data = []

    with open(file_name, 'r') as infile:
        headers = infile.readline().strip().split(delimiter)
        
        # Read remaining lines
        for line in infile:
            pieces = line.strip().split(",")
        
            row_dict = {}
        # go through each column and link the value
        # to the appropriate header
            for i in range(len(pieces)):
                if(pieces[i] == ''):
                    pieces[i] = 0
                if headers[i] in coltypes:
                    cast_func = coltypes[headers[i]]
                    row_dict[headers[i]] = cast_func(pieces[i])
                else:
                    row_dict[headers[i]] = pieces[i]
                
            data.append(row_dict)
            
    return data

def uber_lyft_lists(dicts_cab):
    """
    This function takes in the list from the previous function and seperates it into
    a list of uber dictionaries and a list of lyft dictionaries.
    
    Parameters: 
        dicts_cab = list of dictionaries which each store information about a specific
        lyft or uber ride
        
    Returns:
        uber_list - a list of dictionaries that has rides with just uber
        lyft_list - a list of dictionaries that has rides with just lyft
    """
    
    uber_list = []
    lyft_list = []
    
    for ride in dicts_cab:
        if (ride["cab_type"] == "Uber"):
            uber_list.append(ride)
        elif (ride["cab_type"] == "Lyft"):
            lyft_list.append(ride)
    return uber_list, lyft_list

def price_dist_list(cab_list):
    """
    This function takes in either the uber or lyft list and makes a list of 
    the prices and a list of the distances for a graph. It also calculates the
    average price per mile.
    
    Parameters: 
        cab_list = list of dictionaries which each store information about a specific
        rides (can send either uber_list or lyft_list)
        
    Returns:
        price_list = list of prices for each ride in the list
        distance_list = list of distances for each ride in the list
        price_per_mile = average price per mile for the list
    """
    
    price_list = []
    dist_list = []
    
    for ride in cab_list:
        if (ride["price"] == " "):
            ride["price"] = 0
        else:
            price_list.append(ride["price"])
            dist_list.append(ride["distance"])
    
    avg_price = sum(price_list)/len(price_list)
    avg_dist = sum(dist_list)/len(dist_list)
    
    price_per_mile = avg_price / avg_dist
    
    return price_list, dist_list, price_per_mile
    
    
def plot_prices(uber_prices, uber_dists, lyft_prices, lyft_dists):
    """
    This function reads in the price and distance lists and makes scatter
    plots with them.
    
    Parameters: 
        uber_prices = Takes in list of uber prices to make a graph
        uber_dists = Takes in list of uber distances to make a graph
        lyft_prices = Takes in list of lyft prices to make a graph
        lyft_dists = Takes in list of lyft distances to make a graph
        
    """
    plt.scatter(uber_dists, uber_prices, label = "Uber", marker = ".", color = "r", alpha = 0.5)
    plt.xlabel("Distance (in miles)")
    plt.ylabel("Price (in dollars)")
    plt.title("Price vs. Distance, Uber Rides")
    plt.xlim(0.1,8)
    plt.ylim(1, 100)
    plt.show()
    plt.scatter(lyft_dists, lyft_prices, label = "Lyft", marker = ".", color = "pink", alpha = 0.5)
    plt.xlabel("Distance (in miles)")
    plt.ylabel("Price (in dollars)")
    plt.title("Price vs. Distance, Lyft Rides")
    plt.xlim(0.1,8)
    plt.ylim(0.5, 100)
    plt.show()

def unique_neighborhoods(cab_list):
    """
    This function takes in the list of all rides and returns a list of unique
    neighborhood names
    
    Parameters: 
        cab_list = list of dictionaries which each store information about a specific
        rides (can send either uber_list or lyft_list)
        
    Returns:
        unique_neighborhoods = a list of unique neighborhood names
    """
    unique_neighborhoods = []
    for ride in cab_list:
        if ride["source"] not in unique_neighborhoods:
            unique_neighborhoods.append(ride["source"])
        if ride["destination"] not in unique_neighborhoods:
            unique_neighborhoods.append(ride["destination"])
    unique_neighborhoods.sort()
    return unique_neighborhoods

def neighborhood_counts(cab_list, unique_neighborhoods):
    """
    This function takes in the list of all rides and unique neighborhood names 
    and returns a list of number of rides in each neighborhood
    
    Parameters: 
        cab_list = list of dictionaries which each store information about a specific
        rides (can send either uber_list or lyft_list)
        unique_neighborhoods = a list of unique neighborhood names
        
    Returns:
        neighborhood_counts = a list the number of rides in each nieghborhood
    """
    #Count number of reports for each neighborhood
    neighborhood_counts = []
    for hood in unique_neighborhoods:
        ride_count = 0
        for ride in cab_list:
            if (hood == ride["source"]) or (hood == ride["destination"]):
                ride_count = ride_count + 1
            
        neighborhood_counts.append(ride_count)
    return(neighborhood_counts)
 
def neighborhood_visual(lyft_hoods, lyft_counts, uber_hoods, uber_counts):
    """
    This function takes the lists of neighborhoods and their ride counts and 
    makes two different bar graphs with the data.
    
    Parameters: 
        lyft_hoods = Takes in list of lyft neighborhoods to make a graph
        lyft_counts = Takes in list of lyft ride counts to make a graph
        uber_hoods = Takes in list of uber neighborhoods to make a graph
        uber_counts = Takes in list of uber ride counts to make a graph
        
    """
    plt.bar(uber_hoods, uber_counts, label = "Uber", color = 'r')
    plt.xticks(rotation = 90)
    plt.xlabel("Neighborhoods")
    plt.ylabel("Number of rides")
    plt.title("Frequency of Uber Rides in Different Boston Neighborhoods")
    plt.savefig("uber_counts.png", bbox_inches = "tight")
    plt.show()
    plt.bar(lyft_hoods, lyft_counts, label = "Lyft", color = 'pink')
    plt.xticks(rotation = 90)
    plt.xlabel("Neighborhoods")
    plt.ylabel("Number of rides")
    plt.title("Frequency of Lyft Rides in Different Boston Neighborhoods")
    plt.savefig("lyft_counts.png", bbox_inches = "tight")
    plt.show()
 
def main():
    dicts_cab = read_cab()
    uber_list, lyft_list = uber_lyft_lists(dicts_cab)
    print("Number of total uber rides:", len(uber_list))
    print("Number of total lyft rides:", len(lyft_list))
    uber_prices, uber_dists, avg_price_uber = price_dist_list(uber_list)
    print("Average price per mile, Uber:", avg_price_uber)
    lyft_prices, lyft_dists, avg_price_lyft = price_dist_list(lyft_list)
    print("Average price per mile, Lyft:", avg_price_lyft)
    plot_prices(uber_prices, uber_dists, lyft_prices, lyft_dists)
    uber_hoods = unique_neighborhoods(uber_list)
    lyft_hoods = unique_neighborhoods(lyft_list)
    uber_counts = neighborhood_counts(uber_list, uber_hoods)
    lyft_counts = neighborhood_counts(lyft_list, lyft_hoods)
    neighborhood_visual(lyft_hoods, lyft_counts, uber_hoods, uber_counts)
    
main()