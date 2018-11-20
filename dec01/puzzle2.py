#!/usr/bin/python3
# Advent of code
# Day 1 - Part 2

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read().rstrip()

floor_count = 0
cont = 0
for bracket in my_input:
    if bracket == '(':
        floor_count = floor_count + 1
    else:
        floor_count = floor_count - 1
    cont = cont + 1 
    if floor_count == -1: 
        print (cont)
        break

