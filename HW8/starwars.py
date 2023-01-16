# -*- coding: utf-8 -*-
"""
Madeline Coco
Programming with Data
Created on Wed Nov 16 16:19:17 2022

File: starwars.py
    
Description: This program analyzes the dialogue of the first star wars
movie by sentiment score and creates visuals based on the results.

Most positive line:
Character:  BIGGS
Dialogue:  I feel for you, Luke, you're going to have to learn what seems to 
be important or what really is important.  What good is all your uncle's work 
if it's taken over by the Empire?...  You know they're starting to nationalize 
commerce in the central systems...it won't be long before your uncle is merely 
a tenant, slaving for the greater glory of the Empire.
Score:  5


Most negative line:
Character:  LEIA
Dialogue:  General Kenobi, years ago you served my father in the Clone Wars.  
Now he begs you to help him in his struggle against the Empire.  I regret that 
I am unable to present my father's request to you in person, but my ship has 
fallen under attack and I'm afraid my mission to bring you to Alderaan has 
failed.  I have placed information vital to the survival of the Rebellion 
into the memory systems of this R2 unit.  My father will know how to retrieve 
it.  You must see this droid safely delivered to him on Alderaan.  This is our 
most desperate hour.  Help me, Obi-Wan Kenobi, you're my only hope.
Score:  -6
"""
import matplotlib.pyplot as plt

#global variables
script = "starwars.txt"
pos_words = "positive-words.txt"
neg_words = "negative-words.txt"

def read_script():
    """This function reads in the star wars script data and creates a list
        of dictionaries with the headers as keys"""
    delimiter = "|"
    coltypes = {int, str, str}
    data = []
    
    filename = script
    
    with open(filename, 'r') as infile:
        
    # read the header
        headers = infile.readline().strip().split(delimiter)
        
    # Read remaining lines
        for line in infile:
            pieces = line.strip().split("|")
        
            row_dict = {}
            
    # go through each column and link the value to the appropriate header
            for i in range(len(pieces)):
        
                if headers[i] in coltypes:
                    cast_func = coltypes[headers[i]]
                    row_dict[headers[i]] = cast_func(pieces[i])
                else:
                    row_dict[headers[i]] = pieces[i]
                
            data.append(row_dict)
    return data

    
def read_words(filename):
    """This function reads a text file and turns it into a list of words. It
        is used for the positive and negative word files."""
    data = []
    
    with open(filename, 'r') as infile:   
    # Read remaining lines
        for line in infile:
            line = line.strip()
    # Go through each column and add to the list
            data.append(line)
    
    return data

def text_to_words(text):
    """ Convert a string to a list of cleaned words """
    
    words = text.split()
    for i in range(len(words)):
        words[i] = clean_word(words[i])
    return words

def clean_word(word):
    """ Clean a word, converting to lowercase and removing punctuation
    
    Parameters: word - A word to be cleaned
    Return: cleaned up word
    """
    
    punctuation = "',?;:!.’\""
    for c in punctuation:
        word = word.replace(c,'')
        
       
    word = word.lower()
    return word

def list_of_words(script_dict):
    """This function sends each line of dialogue to the "clean word" function
        and stores the list of clean words in a list.
        word_list: list of lists, all words in each line of dialogue
        """
        
    word_list = []
    
    for line in script_dict:
        words = text_to_words(line["dialogue"])
        word_list.append(words)
    return word_list

def sentiment(word_list, script_dict, pos_list, neg_list):
    """The sentiment function calculates the sentiment score for each line of 
        dialogue and stores it under the "sentiment" key in each dictionary
        counter: counter variable that increases once per loop
        """
        
    counter = 0
    
    for line in word_list:
        sentiment_score = 0
        for word in line:
            if word in pos_list:
                sentiment_score += 1
            elif word in neg_list:
                sentiment_score -= 1
        script_dict[counter]["sentiment"] = sentiment_score
        counter += 1
    
def most_least(script_dict):
    """This function finds the dialogue line with the lowest and highest sentiment scores.
    It also keeps track of their placement in the list of dictionaries.
    
    low: stores the lowest sentiment score
    high: stores the highest sentiment score
    high_place: stores the index placement of the highest sentiment score
    low_place: stores the index placement of the lowest sentiment score
    """
    
    low = 0
    high = 0
    for i in range(len(script_dict)):
        if (script_dict[i]["sentiment"] > high):
            high = script_dict[i]["sentiment"]
            high_place = i
        if (script_dict[i]["sentiment"] < low):
            low = script_dict[i]["sentiment"]
            low_place = i

    return high_place, low_place

def print_out(script_dict, high_place, low_place):
    """This function prints the information for the lines with the highest
        and lowest sentiment scores"""
        
    print("Most positive line:")
    print("Character: ", script_dict[high_place]["character"])
    print("Dialogue: ", script_dict[high_place]["dialogue"])
    print("Score: ", script_dict[high_place]["sentiment"])
    print("\n")
    print("Most negative line:")
    print("Character: ", script_dict[low_place]["character"])
    print("Dialogue: ", script_dict[low_place]["dialogue"])
    print("Score: ", script_dict[low_place]["sentiment"])
    
def luke_leia_data(script_dict):
    """This function gets two lists from the script dictionary, one with
        Luke's scores and one with Leia's
        luke_scores: list of Luke's sentiment scores
        leia_scores: list of Leia's sentiment scores"""
        
    luke_scores = []
    leia_scores = []
    
    for line in script_dict:
        sent = line["sentiment"]
        if (line["character"] == "LUKE"):
            luke_scores.append(sent)
        elif (line["character"] == "LEIA"):
            leia_scores.append(sent)
    return luke_scores, leia_scores
  
def luke_leia_vis(luke_scores, leia_scores):
    """This function uses the lists from the previous function to make overlapping
        histograms of Luke and Leia's sentiment score distributions."""
    plt.hist(luke_scores, bins=10, alpha = 0.5)
    plt.xlim(-6,6)
    plt.hist(leia_scores, bins=10, alpha = 0.5)
    plt.xlim(-6,6)
    plt.xlabel("Sentiment score")
    plt.ylabel("Occurences")
    plt.title("Distribution of sentiment scores in dialogue, Luke vs. Leia")
    plt.legend(["Luke", "Leia"])
    plt.savefig("luke_leia.pdf")
    plt.show()

def sentiment_list(script_dict):
    """This function makes a list of all sentiment scores, which will be 
        used to find the moving average
        sentiment_list: list of all sentiment scores"""
    sentiment_list = []
    for line in script_dict:
        sentiment_list.append(line["sentiment"])
    return sentiment_list

def story_arc(sentiments):
    """This function called the moving average function and then uses it to create
        a plot of the story arc based on sentiment scores. There are two labels
        for the high and low points of the movie.
        avgs: stores the moving averages in a list"""
    avgs = moving_average(sentiments, window_size=20)
    plt.plot(avgs, color = "m")
    plt.xlabel("Line number")
    plt.ylabel("Average sentiment score")
    plt.title("Story Arc of Star Wars: Average Sentiment Scores")
    plt.text(280, -0.72, "Tarkin's Conference")
    plt.text(810, 0.95, "Attack!")
    plt.savefig("story_arc.pdf")
    plt.show()
    pass

def avg(L):
    """ Compute the numerical average of a list of numbers. If list is empty, return 0.0 """
    
    if len(L) > 0:
        return sum(L) / len(L)
    else:
        return 0.0

def get_window(L, idx, window_size=1):
    """ Extract a window of values of specified size centered on the specified index
    L: List of values
    idx: Center index
    window_size: window size
    """
    minrange = max(idx - window_size // 2, 0)
    maxrange = idx + window_size // 2 + (window_size % 2)
    return L[minrange:maxrange]

def moving_average(L, window_size=20):
     """ Compute a moving average over the list L using the specified window size
     L: List of values
     window_size - The window size (default=1)
     return - A new list with smoothed values
     """
     mavg = []
     for i in range(len(L)):
         window = get_window(L, i, window_size)
         mavg.append(avg(window))
     return mavg
    
def main():
    script_dict = read_script()
    pos_list = read_words(pos_words)
    neg_list = read_words(neg_words)
    word_list = list_of_words(script_dict)
    sentiment(word_list, script_dict, pos_list, neg_list)
    high, low = most_least(script_dict)
    print_out(script_dict, high, low)
    luke_scores, leia_scores = luke_leia_data(script_dict)
    luke_leia_vis(luke_scores, leia_scores)
    sentiments = sentiment_list(script_dict)
    story_arc(sentiments)
main()