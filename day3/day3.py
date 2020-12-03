# Advent of Code - Day 3

def init_map(file_path):
    m = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            m.append(list(line))
    return m


def slide_down(step_size_x, step_size_y):
    map_ = init_map('input.txt')
    tree_count = 0
    pos_x, pos_y = 0, 0
    step_x, step_y = step_size_x, step_size_y    
    map_width = len(map_[0])
    map_height = len(map_)
    
    while pos_y < map_height:
        if map_[pos_y][pos_x] == '#':
            tree_count += 1
            map_[pos_y][pos_x] = 'X'
        else:
            map_[pos_y][pos_x] = 'O'   
       # print(''.join(map_[pos_y]))
        pos_x += step_x    
        if pos_x >= map_width:
            pos_x = pos_x % map_width        
        pos_y += step_y
        
    return tree_count

# === Main ===
toboggans = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1

for toboggan in toboggans:
    crashes = slide_down(*toboggan)
    total *= crashes

print(total)