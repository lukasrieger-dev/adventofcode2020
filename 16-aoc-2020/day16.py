import pandas as pd

allowed_values = set()
av_dict = {}
total = 0
valid_tickets = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'or' in line:
            field_values = set()
            field_name, values_range = line.split(':')
            range_1, range_2 = values_range.split(' or ')
            start_1, end_1 = range_1.split('-')
            start_2, end_2 = range_2.split('-')
            allowed_values.update(range(int(start_1), int(end_1)+1))
            allowed_values.update(range(int(start_2), int(end_2)+1))
            field_values.update(range(int(start_1), int(end_1)+1))
            field_values.update(range(int(start_2), int(end_2)+1))
            key = field_name.replace(' ', '_')
            av_dict[key] = field_values
        if ',' in line:
            discard_line = False
            values = list(map(int, line.split(',')))
            for v in values:
                if not (v in allowed_values):
                    total += v
                    discard_line = True
            if not discard_line:
                valid_tickets.append(values)

                
fields = [set() for f in valid_tickets[0]]

for ticket in valid_tickets:
    for idx, value in enumerate(ticket):
        fields[idx].add(value)
    
field_idx = 0
matrix = {}
for key in av_dict:
    matrix[key] = []
    
for field_values in fields:
    for key, allowed_vals in av_dict.items():
        intersection = len(field_values.intersection(allowed_vals)) == len(field_values)
        if intersection:
            matrix[key].append(True)
        else:
            matrix[key].append(False)         
    field_idx += 1
    
df = pd.DataFrame(matrix.values(), index=matrix)
indeces = list(df.sum().sort_values().index)
odf = df[indeces].sort_values(by=indeces)
i, j = 0, 0
my_ticket = [191, 139, 59, 79, 149, 83, 67, 73, 167, 181, 173, 61, 53, 137, 71, 163, 179, 193, 107, 197]
total = 1



for i, j in zip(range(len(df)), range(len(df)-1, -1, -1)):
    print(odf.columns[j], '->', odf.index[i], ':', my_ticket[j], end='')
    if 'departure' in odf.index[i]:
        print('\t\tx')
        # convert number from column label to int
        idx = int(odf.columns[j])
        total *= my_ticket[idx]
    else:
        print()
        
print('Solution:', total)

