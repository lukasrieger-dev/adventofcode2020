bag_rules = {}
start_rules = []
my_bag = 'shiny gold'

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        if line[:10] == my_bag:
            start_rules.append(line)
        symbol, rule = line.split('bags contain')
        symbol = symbol.strip()
        rule = rule.strip('bags.')
        rule = rule.replace('bags', '').replace('bag', '')
        s = rule.split(', ')
        s = [rule.strip() for rule in s]
        bag_rules[symbol] = s

# ------ part 1 ------- 
next_level = [my_bag]
bags = set()
colors_count = 0

while True:
    c = next_level.pop(0)
    for symbol, rule in bag_rules.items():
        #print(symbol, '->', rule, 'c = ', c)
        replaceable = sum([c in ri for ri in rule])
        if replaceable:
            next_level.append(symbol)
            bags.add(symbol)
    if not next_level:
        break
    next_level = list(set(next_level))
        
print(len(bags))

if not len(start_rules) == 1:
    print('too many start rules')
    
# ------ part 2 -------    
next_level = [my_bag]
bag_count = 0
while next_level:
    c = next_level.pop(0)
    next_bags = bag_rules[c]
    for bag in next_bags:
        if bag == 'no other':
            continue
        number, color = bag.split(' ', 1)
        number = int(number)
        for i in range(number):
            next_level.append(color)
        bag_count += number
        
print(bag_count)