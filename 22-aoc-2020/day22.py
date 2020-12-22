player_1 = []
player_2 = []

with open('input.txt') as file:
    lines = file.readlines()
    read_1 = False
    for line in lines:
        line = line.strip()
        if 'Player 1' in line:
            read_1 = True
        elif 'Player 2' in line:
            read_1 = False
        elif len(line) > 0:
            if read_1:
                player_1.append(int(line))
            else:
                player_2.append(int(line))
                

while(player_1 and player_2):
    p1 = player_1.pop(0)
    p2 = player_2.pop(0)
    
    if p1 > p2:
        player_1.append(p1)
        player_1.append(p2)
    else:
        player_2.append(p2)
        player_2.append(p1)
        
if player_1:
    winner = player_1
else:
    winner = player_2
    
score = 0
multiplier = len(winner)
for card in winner:
    score += card * multiplier
    multiplier -= 1
    
print('SCORE:', score)    