def init_tiles(path):
    tiles = {}
    with open(path) as file:
        lines = file.readlines()
        start = False
        current_tile = '0' 

        for line in lines:
            line = line.strip('\n').strip()
            if len(line) == 0:
                continue

            if 'Tile' in line:
                _, no = line.replace(':', '').split(' ')
                current_tile = int(no)
                start = True
            else:
                if start:
                    tiles[current_tile] = {
                        'top':line, 
                        'left':line[0], 
                        'right':line[-1],
                        'bottom':line,
                        'neighbours': set()        
                    }
                    start = False
                else:
                    tiles[current_tile]['left'] += line[0]
                    tiles[current_tile]['right'] += line[-1]
                    tiles[current_tile]['bottom'] = line
        return tiles


def fit(pt, tt):
    s_pt = {
                pt['bottom'], pt['top'], pt['left'], pt['right']
            }
    s_tt = {
                tt['bottom'], tt['top'], tt['left'], tt['right'],
                tt['bottom'][::-1], tt['top'][::-1],
                tt['left'][::-1], tt['right'][::-1]      
           }    
    intersection = s_pt.intersection(s_tt)
    if len(intersection) > 0:
        tt['neighbours'].add(pno)
        
        
# ================    
tiles = init_tiles('input.txt')

for no, tt in tiles.items():
    for pno, pt in tiles.items():
        if pno == no:
            continue    
        fit(pt, tt)
    

total = 1
for key, tile in tiles.items():
    if len(tile['neighbours']) == 2:
        total *= key
        print('Edge:', key)
print(total)