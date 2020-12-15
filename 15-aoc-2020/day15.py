start_seq = [13,16,0,12,15,1]

sequence = {}

for idx, n in enumerate(start_seq):
    sequence[n] = [idx]
    
turn = len(sequence)
number = list(sequence)[-1]

while turn < 30000000:
    if number in sequence and len(sequence[number]) > 1:
        nn = turn - sequence[number][-2] - 1
        if nn in sequence:
            sequence[nn].append(turn)
        else:
            sequence[nn] = [turn]
        number = nn
    else:
        if 0 in sequence:
            sequence[0].append(turn)
        else:
            sequence[0] = [turn]
        number = 0
    turn += 1
    
print(number)
        
        
    
    