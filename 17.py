from itertools import product
    

def read_input(file):
    with open(file) as f:
        input = f.read().splitlines()
    
    input = [list(x) for x in input]
    return input

input = read_input("input/17_input.txt")

# neighbor step
neighbor_step = product([0, 1, -1], repeat = 3)
neighbor_step = [x for x in neighbor_step if x != (0, 0, 0)]

# active cubes
active = set()
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == "#":
            active.add((i, j, 0))


for _ in range(6):
    next_active = set()
    inactive_neighbors = set()
    # check active cubes      
    for cb in active:
        count = 0
        neighbors = [tuple([cb[i] + ns[i] for i in range(len(ns))]) for ns in neighbor_step]
        for nb in neighbors:
            if nb in active:
               count = count + 1
            else:
                inactive_neighbors.add(nb)
    
        if  2 <= count <= 3:
            next_active.add(cb)
    
    # check inactive neighbors of active cubes
    for nb in inactive_neighbors:
        count = 0
        nb_nb = [tuple([nb[i] + ns[i] for i in range(len(ns))]) for ns in neighbor_step] 
        for n in nb_nb:
            if n in active:
                count = count + 1
        if count == 3:
            next_active.add(nb)
        
    active = next_active

# 306
len(active)


## part 2            
def get_active(input, dimension = 4):
    active = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "#":
                active_coord = [i, j] + [0 for _ in range(dimension - 2)]
                active.add(tuple(active_coord))
    
    return active
    

def run(active, dimension = 4, cycle = 6):
    # neighbor step
    neighbor_step = product([0, 1, -1], repeat = dimension)
    no_step = tuple([0 for _ in range(dimension)])
    neighbor_step = [x for x in neighbor_step if x != no_step]
    
    for _ in range(cycle):
        next_active = set()
        inactive_neighbors = set()
        # check active cubes      
        for cb in active:
            count = 0
            neighbors = [tuple([cb[i] + ns[i] for i in range(len(ns))]) for ns in neighbor_step]
            for nb in neighbors:
                if nb in active:
                    count = count + 1
                else:
                    inactive_neighbors.add(nb)
    
            if  2 <= count <= 3:
                next_active.add(cb)
    
        # check inactive neighbors of active cubes
        for nb in inactive_neighbors:
            count = 0
            nb_nb = [tuple([nb[i] + ns[i] for i in range(len(ns))]) for ns in neighbor_step] 
            for n in nb_nb:
                if n in active:
                    count = count + 1
            if count == 3:
                next_active.add(nb)
        
        active = next_active
    
    return len(active)
    
# part 1
# 306
active = get_active(input, 3)
run(active, 3, 6)

# 2572
active = get_active(input, 4)
run(active, 4, 6)