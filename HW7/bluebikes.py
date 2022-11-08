# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Thu Nov  3 11:52:00 2022

File: bluebikes.py
    
Description: This program looks at data from many blue bikes trips and analyzes the
distances/speeds of the trips, as well as creating a histogram to show the most
common speeds/distances.
    
Number of trips ending at Forsyth St at Huntington Ave: 
Friday: 481
Saturday: 230
Sunday: 219
Monday: 250
Tuesday: 314
Wednesday: 296
Thursday: 277
"""
import matplotlib.pyplot as plt
import math

def trips_dictionary(filename):
    
    """
    This function reads the data from the input file and turns it into a list of
    dictionaries where the key is the header and the values are values in that 
    same column
    """
    delimiter = ","
    coltypes = {"duration" : int, "start_day" : int, "bike_id": int}
    data = []
    
    with open(filename, 'r') as infile:
        
        # read the header
        headers = infile.readline().strip().split(delimiter)
        
        # Read remaining lines
        for line in infile:
            pieces = line.strip().split(",")
        
            row_dict = {}
        # go through each column and link the value
        # to the appropriate header
            for i in range(len(pieces)):
        
                if headers[i] in coltypes:
                    cast_func = coltypes[headers[i]]
                    row_dict[headers[i]] = cast_func(pieces[i])
                else:
                    row_dict[headers[i]] = pieces[i]
                
            data.append(row_dict)
           
    return data;  

def stations_dictionary(filename):
    
    """
    This function reads the data from the stations input file and turns it into a single
    dictionary where the key is the station name and the values are longitude and
    latitude of that station
    """
    delimiter = ","

    data = {}
    
    with open(filename, 'r') as infile:
        
        # read the header
        header = infile.readline().strip().split(delimiter)
        
        # Read remaining lines
        for line in infile:
            pieces = line.strip().split(",")
         
            for i in range(len(pieces)):
                row_list = []
                name = pieces[0]
                row_list.append(float(pieces[1]))
                row_list.append(float(pieces[2]))

                data[name] = row_list
                    
    return data;  
  
def distance_and_time(trips_dict, stations_dict):
    """
    This function loops through all of the trips in trips.csv, gets the start and end
    stop, looks their latitude and longitude up and then sends them to the haversine
    distance function to calculate the distance between them. It then adds the distance
    as a key in each dictionary in the trips list of dictionaries. It also calculates the
    distance using the duration of each trip.
    """
    for i in range(len(trips_dict)):
        
        start_station = trips_dict[i]["start_station"]
        end_station = trips_dict[i]["end_station"]
        trip_time = trips_dict[i]["duration"]
     
        if start_station in stations_dict and end_station in stations_dict:
            start_coords = stations_dict[start_station]
            end_coords = stations_dict[end_station]
    
            haversine = haversine_distance(start_coords,end_coords)
            trips_dict[i]["distance"] = haversine
            trips_dict[i]["mph"] = haversine/(trip_time / 3600)
        else:
            trips_dict[i]["distance"] = "N/A"
            trips_dict[i]["mph"] = "N/A"
        
        
    return trips_dict

def haversine_distance(start, end):
    """
Calculates the distance in miles between two points on the earth's surface
described by latitude and longitude.
Parameters:
start: list
list of two floats—latitude and longitude
end: list
list of two floats—latitude and longitude
Return:
float - distance in miles between the two points
"""
# Use this number as it is considered the global average.
    EARTH_RADIUS = 3959

    lat1 = start[0]
    long1 = start[1]
    lat2 = end[0]
    long2 = end[1]
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)
    delta_lat = lat2 - lat1
    delta_long = long2 - long1
    # the earth's radius is a constant value
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long / 2)**2
    haversine = EARTH_RADIUS * 2 * math.asin(math.sqrt(a))
    
    return haversine

def get_dist_speed(trips_dict):
    '''
    This function creates a list of all of the distances and speeds for each trips
    from the list of all trips, and returns them for the graph.
    '''

    all_distances = []
    all_speeds = []
    
    for trip in trips_dict:
        if (trip["distance"] != "N/A"):
            all_distances.append(trip["distance"])
            all_speeds.append(trip["mph"])
    
    return all_distances, all_speeds

def histograms(all_distances, all_speeds):
    """
    This function creates two histograms, one of the distance of the trips and
    one of the speeds.
    """
    plt.hist(all_distances, bins = 100)
    plt.xlabel("Distance (miles)")
    plt.ylabel("Instances")
    plt.title("Blue Bike Trips: Distance Histogram")
    plt.savefig("distances")
    plt.show()
    plt.hist(all_speeds, bins = 100, color = "m")
    plt.xlabel("Speed (mph)")
    plt.ylabel("Instances")
    plt.title("Blue Bike Trips: Speed Histogram")
    plt.savefig("speeds")
    plt.show()

def trips_by_day(trips_dict):
    """
    This function seperates out the trips that end at Forsyth St at Huntington
    Ave and prints how many of those trips occured each day of the week
    """
    dotw = []
    
    for trip in trips_dict:
        if(trip["end_station"] == "Forsyth St at Huntington Ave"):
            dotw.append(trip["start_day_name"])

    print("Number of trips ending at Forsyth St at Huntington Ave: ")
    print("Friday:", dotw.count("Friday"))
    print("Saturday:", dotw.count("Saturday"))
    print("Sunday:", dotw.count("Sunday"))
    print("Monday:", dotw.count("Monday"))
    print("Tuesday:", dotw.count("Tuesday"))
    print("Wednesday:", dotw.count("Wednesday"))
    print("Thursday:", dotw.count("Thursday"))
    
def single_bike(trips_dict, stations_dict):
    """
    Did not have time to finish this function for the extra credit. Not sure if I will
    get partial credit but I left it in just in case.
    """

    for trip in trips_dict:
        bike_start_x = []
        bike_start_y = []
        bike_stop_x = []
        bike_stop_y = []
        if (trip["bike_id"] == 8184):
            start = trip["start_station"]
            end = trip["end_station"]
            if (start in stations_dict) and (end in stations_dict):
                bike_start_x.append(stations_dict[start][0])
                bike_start_y.append(stations_dict[start][1])     
                bike_stop_x.append(stations_dict[end][0])
                bike_stop_y.append(stations_dict[end][1])  
    
    plt.scatter(bike_start_x, bike_start_y, color = "black")
    plt.scatter(bike_stop_x, bike_stop_y, color = "black")
    plt.plot(42.3367, -71.0875, marker = "*", color = "r")
    
# your function code here
def main():
    trips_dict = trips_dictionary("trips.csv")
    stations_dict = stations_dictionary("stations.csv")
    distance_and_time(trips_dict, stations_dict)
    all_distances, all_speeds = get_dist_speed(trips_dict)
    histograms(all_distances, all_speeds)
    trips_by_day(trips_dict)

main()