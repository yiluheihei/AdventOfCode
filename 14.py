import re
from itertools import product

with open("input/14_input.txt") as f:
    input = f.read().splitlines()
    
def int2bit(x, n):
    res = format(x, "b").zfill(n)
    return res

memory = {}

for dat in input:
    curr = dat.split(" = ")
    if curr[0] == "mask":
        curr_bitmask = curr[1]
    else:
        adress = re.findall(r'\[(.*)\]', curr[0])[0]
        value = int2bit(int(curr[1]), 36)
        curr_value = []
        for i, item in enumerate(curr_bitmask):
            if item == "X":
                curr_value.append(value[i])
            else:
                curr_value.append(item)
    
        memory[adress] = int("".join(curr_value), 2)
    
    

# 7440382076205
sum(memory.values())

# part 2

def get_address(mask, address, value):
    new_addr = [mask[i] if mask[i] != "0" else address[i] for i in range(len(mask))]
    
    x_indx = [i for i, item in enumerate(new_addr) if item == "X"]
    if len(x_indx) == 0:
        return "".join(new_addr)
        
    all_comb = product(["0", "1"], repeat = len(x_indx))
    
    addrs = {}
    
    for comb in all_comb:
        addr_may = new_addr[:]
        for i, item in enumerate(x_indx):
            addr_may[item] = comb[i]
        
        addrs["".join(addr_may)] = value
    
    return addrs
    

    
memory2 = {}
for dat in input:
    curr = dat.split(" = ")
    if curr[0] == "mask":
        curr_bitmask = curr[1]
    else:
        address = re.findall(r'\[(.*)\]', curr[0])[0]
        address = int2bit(int(address), 36) 
        value = int(curr[1])
        
        addresses = get_address(curr_bitmask, address, value)
        memory2.update(addresses)

# 4200656704538
sum(memory2.values())