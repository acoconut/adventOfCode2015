#!/usr/bin/python3
# Advent of code
# Day 2 - Part 2

# Read and parse input
fo = open("input.txt", "r+")
lines = fo.readlines()

total = 0
for present in lines:
    sizes = present.split('x')
    int_sizes = [ int(x) for x in sizes ]
    int_sizes = sorted(int_sizes)
    
    total = total + int_sizes[0] + int_sizes[0] + int_sizes[1] + int_sizes[1] + (int_sizes[0] * int_sizes[1] * int_sizes[2])


print (total)
