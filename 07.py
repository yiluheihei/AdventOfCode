import re

with open("input/07_input.txt") as f:
    rules = f.read().splitlines()

bag_parents = [re.findall(r'^(.*?) bags?', x)[0] for x in rules]
bag_childs = [re.findall(r'\d+ (.*?) bags?', x) for x in rules]

def get_parent(bag, bag_childs, bag_parents):
    bag_direct_parents = [bag_parents[i] for i in range(len(bag_childs)) if bag in bag_childs[i]]
    
    res = [get_parent(x, bag_childs, bag_parents) for x in bag_direct_parents]
    res = [i for r in res for i in r]
    return bag_direct_parents + res

shiny_gold_parents = get_parent('shiny gold', bag_childs, bag_parents)
print(len(set(shiny_gold_parents)), 'bag colors contain at least one shiny gold bag')

# part 2
bag_childs_count = [re.findall(r'(\d+)', x) for x in rules]

def get_bag_counts(bag, bag_childs, bag_parents, bag_childs_count):
    idx = bag_parents.index(bag)
    childs = bag_childs[idx]
    childs_count = bag_childs_count[idx]
    childs_count = [int(x) for x in childs_count]
    return sum(childs_count) + sum([childs_count[i] * get_bag_counts(child, bag_childs, bag_parents, bag_childs_count) for i, child in enumerate(childs)])

count = get_bag_counts("shiny gold", bag_childs, bag_parents, bag_childs_count)
print("shiny gold contain", count, "bags")



