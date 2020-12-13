def load(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        arrival_time = int(lines[0])
        raw_data = lines[1]
        bus_ids = [int(bus_id) for bus_id in raw_data.split(',') if not (bus_id == 'x')]
        return arrival_time, bus_ids, raw_data
    

def get_next_bus(arrival_time, bus_ids):
    min_wait_time = 999999999
    min_bus_id = -1

    for bus_id in bus_ids:
        wait_time = bus_id - (arrival_time % bus_id)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_bus_id = bus_id
    print('Solution 1: ', min_wait_time * min_bus_id)
    return min_wait_time, min_bus_id


def find_deperatures_sequence(raw_data):
    time = 0
    tt = {}
    multiples = set()
    for x in raw_data.split(','):
        if not (x == 'x'):
            tt[int(x)] = time
        time += 1
    
    print(tt)
    max_id = max(tt)
    time = max_id - tt[max_id] + (100000000000000 // max_id) * max_id
    incr = max_id
    print('start time', time)
    while True:
        found = True
        for bus_id, tp in tt.items():
            next_arrival = (bus_id - (time % bus_id)) % bus_id 
            found = found and (next_arrival == tp)
            if not found:
                break
        if found:
            print('==> ', time)
            break
        time += incr
             
arrival_time, bus_ids, raw_data = load('input.txt')
get_next_bus(arrival_time, bus_ids)
# too slow...
find_deperatures_sequence(raw_data)
