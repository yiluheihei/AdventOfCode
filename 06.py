import re
from functools import reduce

with open("input/06_input.txt") as f:
    dat = f.read()

dat_groups = re.split(r"\n\n", dat)

def get_group_count(group):
    return len(set(group.replace("\n", "")))

count = sum([get_group_count(group) for group in dat_groups])
print("The sum of counts is", count)


# part 2
def get_group_count2(group):
    person = group.splitlines()
    person = [list(x) for x in person]
    all_yes = reduce(set.intersection, [set(item) for item in person])
    
    return len(all_yes)

count2 = sum([get_group_count2(group) for group in dat_groups])
print("The sum of counts is", count2, "in part 2")