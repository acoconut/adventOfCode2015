#!/usr/bin/python3
# Advent of code
# Day 3 - Part 2

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read()

location_robo = (0,0)
location_santa = (0,0)
houses = {(0,0): 1} 
turn = 0 

for direction in my_input:
    if direction == 'v': 
        if turn%2:
            location_robo = (location_robo[0], location_robo[1]-1)
        else:
            location_santa = (location_santa[0], location_santa[1]-1)
    elif direction == '>': 
        if turn%2:
            location_robo = (location_robo[0]+1, location_robo[1])
        else:
            location_santa = (location_santa[0]+1, location_santa[1])
    elif direction == '<':
        if turn%2:
            location_robo = (location_robo[0]-1, location_robo[1])
        else:
            location_santa = (location_santa[0]-1, location_santa[1])
    else:
        if turn%2:
            location_robo = (location_robo[0], location_robo[1]+1)
        else:
            location_santa = (location_santa[0], location_santa[1]+1)

    if turn%2:
        if location_robo in houses: 
            houses[location_robo] = houses[location_robo] + 1
        else:
            houses[location_robo] = 1
    else:
        if location_santa in houses:
            houses[location_santa] = houses[location_santa] + 1
        else:
            houses[location_santa] = 1

    turn = turn + 1

print(len(houses))

            
