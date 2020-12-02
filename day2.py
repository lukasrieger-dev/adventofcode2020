# Advent of Code - Day 2

import operator

valid_pws = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        policy, password = line.split(':')
        occurrences, letter = policy.split()
        first_occ, second_occ = map(int, occurrences.split('-'))
        f = password[first_occ] == letter
        s = password[second_occ] == letter
        
        xor = operator.xor(f, s)
        if xor:
            valid_pws += 1
    
print(valid_pws)
        