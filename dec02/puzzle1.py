#!/usr/bin/python3
# Advent of code
# Day 2 - Part 1

# Read and parse input
fo = open("input.txt", "r+")
lines = fo.readlines()

total = 0
for present in lines:
    (l, w, h) = present.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    area1 = l * w
    area2 = w * h
    area3 = h * l 
    total = total + ((2 * area1) + (2 * area2) + (2 * area3) + min(area1, area2, area3))

print (total)
