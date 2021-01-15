from math import ceil
from numpy import prod

f = open('input/03_input.txt')
dat = f.read().splitlines()
f.close()

def new_extend_dat(right, down, dat):
    n_v = len(dat)
    n_h = len(dat[0])
    step_v = ceil(n_v/down)
    step_h = ceil(n_h/right)
    if step_h >= step_v:
        return dat
    else:
        n_extend_h = right * step_v
        time = ceil(n_extend_h/n_h)
        new_dat = [x * time for x in dat]
        return new_dat


new_dat = new_extend_dat(3, 1, dat)

locations = []
for i in range(len(dat)):
    locations.append(new_dat[i][i*3])

print("Number of trees:", locations.count("#"))

# part 2
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

n_tree = []
for i in range(len(right)):
    new_dat = new_extend_dat(right[i], down[i], dat)
    locations = []
    step = ceil(len(new_dat)/down[i])
    for j in range(step):
        if j * down[i] < len(dat):
            locations.append(new_dat[j * down[i]][j*right[i]])
        else:
            locations.append(new_dat[len(dat)][j*right[i]])
    n_tree.append(locations.count("#"))

print("multiple of trees:", prod(n_tree))