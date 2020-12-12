def find_row(code):
    lower, upper = 0, 127
    for c in code:
        if c == 'B':
            lower = (lower + upper)//2 + 1
        else: # c == 'F'
            upper = round((lower + upper)//2)            
    return lower


def find_col(code):
    lower, upper = 0, 7
    for c in code:
        if c == 'R':
            lower = (lower + upper)//2 + 1
        else: # c == 'L'
            upper = round((lower + upper)//2)   
    return lower


max_seat_id = -1
seat_ids = []
with open('input.txt', 'r') as file:
    codes = file.readlines()
    for code in codes:
        code = code.strip('\n')
        row_code = code[:-3]
        col_code = code[-3:]
        row = find_row(row_code)
        col = find_col(col_code)
        seat_id = row*8 + col
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        seat_ids.append(seat_id)

print('max seatid =', max_seat_id)
all_seat_ids = set(range(0, max_seat_id + 1))
x = all_seat_ids.difference(seat_ids)
# look at the output :) to find the solution
print(x)