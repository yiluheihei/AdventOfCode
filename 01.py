f = open('./input/01_input.txt')
dat = f.read().splitlines()
f.close()

# dat = [int(x) for x in dat]
dat = list(map(int, dat))

for i in range(len(dat)):
    for j in range(i + 1, len(dat)):
        s = dat[i] + dat[j]
        if s == 2020:
            entry = [dat[i], dat[j]]
            break

print("The two entries is", entry[0], entry[1])
print("Result is", entry[0]*entry[1])

from itertools import combinations

three_elements = combinations(dat, 3)
for element in three_elements:
    if sum(element) == 2020:
        entry = element
        print("The three enties is", element)
        break

print("Result is", entry[0]*entry[1]*entry[2])