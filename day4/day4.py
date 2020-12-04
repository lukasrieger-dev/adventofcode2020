# Advent of Code - Day 4
valid_passport_data = {
    'ecl', 'pid', 'eyr', 'hcl',
    'byr', 'iyr', 'hgt',
}
count_required_data = len(valid_passport_data)

def ecl_rule(value):
    return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def pid_rule(value):
    try:
        int(value)
        isnumber = True
    except:
        isnumber = False
    return (len(value) == 9) and isnumber

def eyr_rule(value):
    try:
        year = int(value)
    except:
        return False
    return year >= 2020 and year <= 2030

def hcl_rule(value):
    try:
        int(value[1:], 16)
    except:
        return False
    return value[0] == '#' and len(value) == 7

def byr_rule(value):
    try:
        year = int(value)
    except:
        return False
    return year >= 1920 and year <= 2002

def iyr_rule(value):
    try:
        year = int(value)
    except:
        return False
    return year >= 2010 and year <= 2020

def hgt_rule(value):
    units = value[-2:]
    try:
        height = float(value[:-2])
    except:
        return False
    if units == 'cm':
        return height >= 150.00 and height <= 193.00
    if units == 'in':
        return height >= 59.00 and height <= 76.00
    return False

validation_rules = {
    'ecl': ecl_rule, 
    'pid': pid_rule,
    'eyr': eyr_rule,
    'hcl': hcl_rule,
    'byr': byr_rule,
    'hgt': hgt_rule,
    'iyr': iyr_rule
}
    
def load_passports(path):
    with open(path, 'r') as file:
        lines = file.readlines()  
        passports = []
        passport_data = {}

        for line in lines:  
            if ':' in line:
                key_value_list = line.split()
                for key_value in key_value_list:
                    key, value = key_value.split(':')
                    passport_data[key] = value          
            else:
                passports.append(passport_data)
                passport_data = {}
        passports.append(passport_data)
    return passports

def validate_passport(passport):
    keys = set(passport)
    common_data = valid_passport_data.intersection(keys)
    if len(common_data) == count_required_data:
        is_valid = True
        for key in keys:
            if key == 'cid':
                continue
            try:
                value = passport[key]
                is_valid = (is_valid and validation_rules[key](value))
            except Exception as e:
                print(f'ValidationError: {e}')
        return int(is_valid)
    return 0


# === MAIN ===
valid_passports_count = 0
passports = load_passports('input.txt')

for p in passports:
    valid_passports_count += validate_passport(p)
    
print(valid_passports_count)