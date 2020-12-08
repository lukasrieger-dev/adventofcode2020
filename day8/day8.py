code_dict = {}
accumulator = 0
line_nr = 0
do_substitute = True

saved_code_dict = 0
saved_accumulator = 0
saved_line_nr = 0

def load_code():
    code_dict = {}
    line_nr = 0
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            code_dict[line_nr] = line, False
            line_nr += 1
    return code_dict
        
        
def save_state():
    global line_nr
    global code_dict
    global accumulator
    global saved_code_dict
    global saved_accumulator
    global saved_line_nr
    
    #print('SAVED: ', line_nr, accumulator)
    saved_line_nr = line_nr
    saved_accumulator = accumulator
    saved_code_dict = dict(code_dict)
    
    
def reset_state():
    global line_nr
    global code_dict
    global accumulator
    global saved_code_dict
    global saved_accumulator
    global saved_line_nr
    global do_substitute
    
    do_substitute = True
    line_nr = saved_line_nr
    accumulator = saved_accumulator
    code_dict = dict(saved_code_dict)
    #print('RESET TO:', line_nr, accumulator)


def substitute(code):
    global do_substitute
    
    if not substitute:
        return code
    
    op, arg = code.split()
    if op in {'nop', 'jmp'}:
        if do_substitute:
            save_state()
            next_line_nr = int(arg) + line_nr
            if op == 'nop':
                code = 'jmp ' + arg
            elif op == 'jmp':
                code = 'nop ' + arg
            do_substitute = False
    return code


def execute(code):
    op, arg = code.split()
    if op == 'nop':
        return 0, 1
    if op == 'jmp':
        return 0, int(arg)
    if op == 'acc':
        return int(arg), 1
    raise Exception('Unknown code: ' + code)
      
 

# === MAIN ===
code_dict = load_code()

END_LINE_NR = len(code_dict)
line_nr = 0    
fixed = False

while not fixed:
    code, was_executed = code_dict[line_nr]
    code = substitute(code)
    
    if was_executed:
        reset_state()
        code, _ = code_dict[line_nr]
    
    acc_inc, line_inc = execute(code)
    code_dict[line_nr] = code, True
    accumulator += acc_inc
    line_nr += line_inc
        
    if line_nr == END_LINE_NR:
        fixed = True
        print('### FIXED ###')
    

print(accumulator)
        
        