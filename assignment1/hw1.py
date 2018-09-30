#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

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
    points = points.astype(float)

    #reflects the points over the line y = 1
    points[1] *= -1
    points[1] += 2
    
    #rotates the points Pi/2 radians about the origin
    rotation = np.array([ [math.cos(math.pi/2), -1 * math.sin(math.pi/2)],
                        [math.sin(math.pi/2), math.cos(math.pi/2)] ])
    points = np.dot(rotation,points)
    
    #projects the point onto the line y = 3x
    m = 3
    scalar = (m^2 + 1) ^ (-1)
    matrix = np.array( [ [1, m],
                        [m, m^2] ])
    points = np.dot(matrix,points)
    points *= scalar
    
    return points

def normalize(image):
    working = np.copy(image)
    working = working.astype(float)
    working -= image.min()
    working *= float(255 / (image.max() - image.min()))
    return working.astype(int)

def sigmoid_normalize(image, a):
    working = np.copy(image)
    working = working.astype(float)
    working -= 128
    working /= -a
    working = math.exp(working)
    working = 1/ (working + 1)
    working *= 255

    return working.astype(int)
