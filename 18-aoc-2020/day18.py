def stream(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = '(' + line.strip('\n').replace(' ', '') + ')'
            yield line


def set_parenthesis_left_to_right(sub_exercise):
    tmp = ['(']
    cnt = 0
    for c in sub_exercise:
        if c in '+*':
            tmp.append(')' + c)
            cnt += 1
        else:
            tmp.append(c)
    tmp = ''.join([cnt * '('] + tmp) + ')'
    return tmp


def set_parenthesis_plus_first(sub_exercise):
    tmp = ['(']
    is_open = True
    for c in sub_exercise:
        if c == '*':
            tmp.append(')*(')
        else:
            tmp.append(c)
    tmp.append(')')
    tmp = ''.join(tmp)
    return tmp


def solve(exercise, pre_type):
    stack = []
    open_idx = []
    idx = 0
    
    for c in exercise:
        if c == '(':
            open_idx.append(idx)
        elif c == ')':
            start = open_idx.pop()
            sub_exercise = ''.join(stack[start+1:idx])
            stack = stack[:start+1]
            if pre_type == 1:
                sub_exercise = set_parenthesis_left_to_right(sub_exercise)
            else:
                sub_exercise = set_parenthesis_plus_first(sub_exercise)
                
            sub_result = str(eval(sub_exercise))
            stack.append(sub_result)
            idx = len(stack)
            
        stack.append(c)
        idx += 1
        
    return int(stack[1])


# === MAIN ===
result1 = 0
result2 = 0
for exercise in stream('input.txt'):
    r = solve(exercise, 1)
    result1 += r
    
    r = solve(exercise, 2)
    result2 += r
    
print(result1)
print(result2)