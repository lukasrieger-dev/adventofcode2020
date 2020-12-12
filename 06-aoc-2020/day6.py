import string

path = 'input.txt'
anyone_yes = 0
everyone_yes = 0
all_answers = set(string.ascii_lowercase)

with open(path, 'r') as file:
    lines = file.readlines()
    group = set()
    for line in lines:
        line = line.strip('\n').strip()
        if len(line) > 0:
            group.update(line)
            all_answers = all_answers.intersection(line)
        else:
            anyone_yes += len(group)
            everyone_yes += len(all_answers)
            group = set()
            all_answers = set(string.ascii_lowercase)
anyone_yes += len(group)
everyone_yes += len(all_answers)
            
print('Anyone yes:', anyone_yes)
print('Everyone yes:', everyone_yes)