#!/usr/bin/python3
# Advent of code
# Day 3 - Part 1

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read()

location = (0,0)
houses = {(0,0): 1} 
for direction in my_input:
    if direction == 'v': 
        location = (location[0], location[1]-1)
    elif direction == '>': 
        location = (location[0]+1, location[1])
    elif direction == '<':
        location = (location[0]-1, location[1])
    else:
        location = (location[0], location[1]+1)

    if location in houses: 
        houses[location] = houses[location] + 1
    else:
        houses[location] = 1

print(len(houses))

            
