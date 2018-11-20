#!/usr/bin/python3
# Advent of code
# Day 1 - Part 1

# Read and parse input
fo = open("input.txt", "r+")
my_input = fo.read().rstrip()

cont = 0
for bracket in my_input:
    if bracket == '(':
        cont = cont + 1
    else:
        cont = cont - 1

print (cont)
