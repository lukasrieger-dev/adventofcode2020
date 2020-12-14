def stream(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            command, value = line.split(' = ')
            yield command, value

# === Part 1 ===
def apply_mask_1(mask, value):
    new_val = []
    value = bin(int(value))[2:]
    value = (len(mask) - len(value) - 1) * '0' + value

    for m, v in zip(mask, value):
        if m == 'X':
            new_val.append(v)
        else:
            new_val.append(m)
            
    value = ''.join(new_val)
    value = int(value, 2)  
    return value


memory = {}
mask = '' 
for command, value in stream('input.txt'):    
    if 'mask' in command:
        mask = value
    elif 'mem' in command:
        address = int(command[4:-1])
        value = apply_mask_1(mask, value)
        memory[address] = value

print(sum(list(memory.values())))

# ======== Part 2 ========
def apply_mask_2(mask, address):
    new_addr = []
    address = bin(int(address))[2:]
    address = (len(mask) - len(address) - 1) * '0' + address
    for m, a in zip(mask, address):
        if m == 'X':
            new_addr.append('X')
        elif m == '1':
            new_addr.append('1')
        else:
            new_addr.append(a)
    address = ''.join(new_addr)
    return address


def unfold(address):
    addresses = []
    x = address.count('X')
    end = x * '1'
    i = 0
    addr = 'start'
    while not (addr == end):
        addr = bin(i)[2:]
        addr = (x - len(addr)) * '0' + addr
        addr_idx = 0
        new_addr = []
        for bit in address:
            if bit == 'X':
                new_addr.append(addr[addr_idx])
                addr_idx += 1
            else:
                new_addr.append(bit)
        addresses.append(''.join(new_addr))
        i += 1
    return addresses
    
    
memory = {}
mask = '' 
for command, value in stream('input.txt'):    
    if 'mask' in command:
        mask = value
    elif 'mem' in command:
        address = int(command[4:-1])
        address = apply_mask_2(mask, address)
        addresses = unfold(address)
        for a in addresses:
            idx = int(a)
            memory[idx] = int(value)

print(sum(list(memory.values())))