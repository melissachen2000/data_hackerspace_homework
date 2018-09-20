#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    crashes_per_hour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    with open(filename) as data:
        csv_reader = csv.reader(data)
        data_list = list(csv_reader)
        for crash in data_list[1:]:
            if crash[1]:
                time = crash[1]
                hour = ""
                
                for letter in time:
                    if letter in "0123456789":
                        hour += letter
                        
                hour = hour.zfill(4)
                hour = hour[:2]
                
                crashes_per_hour[int(hour)] += 1
                
    return crashes_per_hour

def weigh_pokemons(filename, weight):
    pokemons = []
    with open(filename) as data:
        pokedex_json = json.load(data)
        all_pokemon = pokedex_json["pokemon"]
        
        for index in range(len(all_pokemon)):
            if all_pokemon[index]["weight"] == (str(weight) + " kg"):
                pokemons.append(all_pokemon[index]["name"])
    return pokemons

def single_type_candy_count(filename):
    total = 0
    with open(filename) as data:
        pokedex_json = json.load(data)
        all_pokemon = pokedex_json["pokemon"]
        
        for index in range(len(all_pokemon)):
            if (len(all_pokemon[index]["type"]) == 1):
                try: total += all_pokemon[index]["candy_count"]
                except (KeyError): pass

    return total

def reflections_and_projections(points):
    pass

def normalize(image):
    pass

def sigmoid_normalize(image):
    pass
