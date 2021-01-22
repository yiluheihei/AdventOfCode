
from itertools import combinations

with open('input/09_input.txt') as f:
    dat = f.read().splitlines()

dat = [int(x) for x in dat]

for i in range(25, len(dat)):
    two_sums = [sum(x) for x in combinations(dat[:i], 2)]
    if dat[i] in two_sums:
        continue
    else:
        res = dat[i]
        pos = i
        break

print("First invalid number is", res)


# part 2
for i in range(pos - 1):
    for j in range(i+1, pos - 1):
        sub_dat = dat[i:j]
        if sum(sub_dat) < res:
            continue
        elif sum(sub_dat) == res:
            weak_dat = sub_dat
        else: 
            break

encry_weakness = min(weak_dat) + max(weak_dat)
print("Encryption weakness is", encry_weakness)

