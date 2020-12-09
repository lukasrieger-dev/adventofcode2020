def stream(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            yield(int(line))
        
# ---- part 1 ----
lookahead_size = 25
lookahead = []
ready = False
bad_number = -1

for number in stream('input.txt'):
    if not ready:
        lookahead.append(number)
        if len(lookahead) == lookahead_size:
            ready = True
        continue
    lookahead_set = set(lookahead)
    valid = False
    for n in lookahead:
        diff = (number - n)
        if (diff in lookahead_set) and not (diff == n):
            valid = True
            break       
    if not valid:
        print(number)
        bad_number = number
        break
    lookahead.pop(0)
    lookahead.append(number)
    
# ---- part 2 ----
ranges = []
stop = False

for number in stream('input.txt'):
    if stop:
        break
    ranges.append(number)
    
    for i in range(len(ranges)):
        r = ranges[i:]
        if sum(r) == bad_number:
            print(min(r) + max(r))
            stop = True
            break