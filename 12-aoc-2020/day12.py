NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'
DIRS = [NORTH, EAST, SOUTH, WEST]
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'


def stream(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            direction, steps = line[:1], int(line[1:])
            yield direction, steps
            

def navigate(direction, steps, dirs_idx, x, y):
    if direction == NORTH:
        y += steps
    elif direction == SOUTH:
        y -= steps
    elif direction == EAST:
        x += steps
    elif direction == WEST:
        x -= steps
    elif direction == LEFT:
        turns = -(steps // 90)
        turns += len(DIRS)
        dirs_idx = (dirs_idx + turns) % len(DIRS)
    elif direction == RIGHT:
        turns = steps // 90
        dirs_idx = (dirs_idx + turns) % len(DIRS)
    elif direction == FORWARD:
        return navigate(DIRS[dirs_idx], steps, dirs_idx, x, y)
    else:
        print('ERROR: ', direction, steps)
    return dirs_idx, x, y


def move_waypoint(direction, steps, x, y):
    if direction == NORTH:
        y += steps
    elif direction == SOUTH:
        y -= steps
    elif direction == EAST:
        x += steps
    elif direction == WEST:
        x -= steps
    elif direction == LEFT:
        rotations = steps // 90
        for i in range(0, rotations):
            x, y = -y, x
    elif direction == RIGHT:
        rotations = steps // 90
        for i in range(0, rotations):
            x, y = y, -x
    else:
        print('ERROR: ', direction, steps)
    return x, y


def follow_waypoint(x, y, step_x, step_y, scale):
    x += scale * step_x
    y += scale * step_y
    
    return x, y

# ==== MAIN ====
# =========== PART 1 =============
x, y = 0, 0
dirs_idx = 1

for direction, steps in stream('input.txt'):
    dirs_idx, x, y = navigate(direction, steps, dirs_idx, x, y)
    
m_d_1 = abs(x) + abs(y)
print('1.) Manhattan Distance:', m_d_1)

# =========== PART 2 =============
x, y = 0, 0
wp_x, wp_y = 10, 1

for direction, steps in stream('input.txt'):
    if direction == FORWARD:
        x, y = follow_waypoint(x, y, wp_x, wp_y, steps)
    else:
        wp_x, wp_y = move_waypoint(direction, steps, wp_x, wp_y)
    
m_d_2 = abs(x) + abs(y)
print('2.) Manhattan Distance:', m_d_2)
        
        
    
            