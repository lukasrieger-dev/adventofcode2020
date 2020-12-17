
def init(path):
    active_cubes = []
    with open(path, 'r') as file:
        lines = file.readlines()
        y = 0
        for line in lines:
            x = 0
            line = line.strip('\n')
            for cube in line:
                if cube == '#':
                    active_cubes.append((x, y, 0, 0))
                x += 1
            y += 1
    return active_cubes
            

def update_grid(active_cubes):
    updated_active_cubes = []
    active_cubes = set(active_cubes)
    
    # min dimensions of grid containing all active cubes
    grid_max_x = max(active_cubes, key=lambda x:x[0])[0]
    grid_min_x = min(active_cubes, key=lambda x:x[0])[0]
    grid_max_y = max(active_cubes, key=lambda x:x[1])[1]
    grid_min_y = min(active_cubes, key=lambda x:x[1])[1]
    grid_max_z = max(active_cubes, key=lambda x:x[2])[2]
    grid_min_z = min(active_cubes, key=lambda x:x[2])[2]
    grid_max_w = max(active_cubes, key=lambda x:x[3])[3]
    grid_min_w = min(active_cubes, key=lambda x:x[3])[3]
    
    # iterate cubes of smallest grid containing all active cubes
    for x in range(grid_min_x-1, grid_max_x+2):
        for y in range(grid_min_y-1, grid_max_y+2):
            for z in range(grid_min_z-1, grid_max_z+2):
                for w in range(grid_min_w-1, grid_max_w+2):
                
                    current_cube = (x, y, z, w)
                    active_neighbours = []

                    # iterate neighbours of current cube
                    for xn in range(x-1, x+2):
                        for yn in range(y-1, y+2):
                            for zn in range(z-1, z+2):
                                for wn in range(w-1, w+2):
                                    neighbour = (xn, yn, zn, wn)
                                    if neighbour == current_cube:
                                        continue
                                    if neighbour in active_cubes:
                                        active_neighbours.append(neighbour)

                    # switch state of current cube
                    cnt_active_neighbours = len(active_neighbours)
                    is_active = current_cube in active_cubes
                    if is_active and (cnt_active_neighbours in {2, 3}):
                        updated_active_cubes.append(current_cube)
                    elif not is_active and cnt_active_neighbours == 3:
                        updated_active_cubes.append(current_cube)
                    
    return updated_active_cubes
                    
                            
    
# ==== Main ====        
active_cubes = init('input.txt')

for cycle in range(1, 7):
    active_cubes = update_grid(active_cubes)
    
print(len(active_cubes))

