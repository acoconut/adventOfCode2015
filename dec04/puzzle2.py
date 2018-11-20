#!/usr/bin/python3
# Advent of code
# Day 4 - Part 2

from hashlib import md5

# Input
my_input = 'bgvyzdsv'

cont = 0 
not_found = True
while not_found:
    md5_hash = md5((my_input+str(cont)).encode('utf-8')).hexdigest()
    if md5_hash.startswith('000000'):
        break
    cont = cont + 1


print (cont)
