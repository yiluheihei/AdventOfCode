import re
from collections import Counter

f = open("input/02_input.txt")
dat = f.read().splitlines()
f.close()

n = 0
for pwd in dat:
    elements = re.split(r'[:\-\s]', pwd)
    elements = [x for x in elements if x!= ""]
    char_count = Counter(elements[3])
    if elements[2] in char_count:
        given_letter_count = char_count[elements[2]] 
        print(given_letter_count)
        if (given_letter_count >= int(elements[0])) & (given_letter_count <= int(elements[1])):
            n += 1

print(n, "passwords are valid")

# part 2
n = 0
for pwd in dat:
    elements = re.split(r'[:\-\s]', pwd)
    elements = [x for x in elements if x!= ""]
    c1 = elements[3][int(elements[0]) - 1]
    c2 = elements[3][int(elements[1]) - 1]
    if (c1 != c2) & (elements[2] in [c1, c2]):
        n += 1

print(n, "passwords are valid")