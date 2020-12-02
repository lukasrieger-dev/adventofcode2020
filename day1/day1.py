# Advent of Code - Day 1

all_numbers = set()

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        n = int(line)
        all_numbers.add(n)
        
stop = False
for n1 in list(all_numbers):
    if stop:
        break
    diff1 = 2020 - n1
    for n2 in list(all_numbers):
        diff2 = diff1 - n2
        if diff2 in all_numbers:
            print(n1, n2, diff2)
            result = n1 * n2 * diff2
            stop = True
            break
        
print(result)