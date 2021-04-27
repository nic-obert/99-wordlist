#!/usr/bin/env python3

with open('wordlist.csv', 'r') as file:
    count = file.read().count(',')
print(count)
