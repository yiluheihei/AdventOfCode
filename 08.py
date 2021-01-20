import re
from functools import reduce
import copy

with open("input/08_input.txt") as f:
    insts = f.read().splitlines()
    insts = [inst.split() for inst in insts]

acc = 0

instructions_visited = [0]

i = 0
while True: 
    ins = insts[i]
    if "acc" == ins[0]:
        acc = acc + int(ins[1])
        i = i + 1
    elif "nop" == ins[0]:
        i = i + 1
    elif "jmp" == ins[0]:
        i = i + int(ins[1])
    
    if i in instructions_visited:
        break
    else:
        instructions_visited.append(i)

    
print("accumulator is", acc)


# part2

def run_inst(insts):
    visit = [0]
    i = 0
    acc = 0
    while True:
        ins = insts[i]
        if 'acc' == ins[0]:
            acc = acc + int(ins[1])
            i = i + 1
        elif 'nop' in ins[0]:
            i = i + 1
        elif 'jmp' in ins:
            i = i + int(ins[1])
        
        if i >= len(insts):
            break
        if i in visit:
           break
        else:
            visit.append(i)
    return acc, visit


def change_insts(idx, insts):
    new_inst = copy.deepcopy(insts)
    if "nop" == new_inst[idx][0]:
        new_inst[idx][0] = "jmp"
    elif "jmp" == new_inst[idx][0]:
        new_inst[idx][0] = "nop"
    else:
        raise AssertionError("must be nop or jmp")
    
    return new_inst


# part 1 using get_run_instructions
part1 = run_inst(insts)[0]

nop_idx = [i for i, inst in enumerate(insts) if 'nop' == inst[0]]
jmp_idx = [i for i, inst in enumerate(insts) if 'jmp' == inst[0]]
idxes = nop_idx + jmp_idx

for idx in idxes:
    new_insts = change_insts(idx, insts)
    res_inst = run_inst(new_insts)
    print(idx)
    if res_inst[1][-1] == len(insts) - 1:
        part2_acc = res_inst[0]

print("part 2 accumulator is", part2_acc)

