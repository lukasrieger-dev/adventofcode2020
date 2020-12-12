
def load_data(path):
    adapters = []
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            adapters.append(int(line))
            
    adapters.append(max(adapters)+3)
    adapters.sort()
    return adapters

    
def compute_diffs(adapters):
    adapters.sort()
    diffs = [0, 0, 0]
    jolts = 0
    
    for adapter in adapters:
        idx = (adapter - jolts) - 1
        diffs[idx] += 1
        jolts = adapter
        
    return diffs
            
adapters = load_data('input.txt')
diffs = compute_diffs(adapters)
print('Solution 1:', diffs[0] * diffs[2])