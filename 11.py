from copy import deepcopy
from collections import Counter
from operator import eq

with open("input/11_input.txt") as f:
    seats = f.read().splitlines()

seats = [list(x) for x in seats]

def get_adjacent(seats, i, j):
    m = len(seats)
    n = len(seats[0])
    # adj coordinates
    row = [i - 1, i, i + 1]
    col = [j - 1, j, j + 1]
    row = [x for x in row if 0 <= x < m]
    col = [x for x in col if 0 <= x < n]
    adj = []
    for a in row:
        for b in col:
            adj.append([a, b])
    
    adj.remove([i, j])
    res = [seats[x[0]][x[1]] for x in adj]
    return res

def next_round(seats):
    m = len(seats)
    n = len(seats[0])
    next_seats = deepcopy(seats)
    for i in range(m):
        for j in range(n):
            curr = seats[i][j]
            curr_adj = get_adjacent(seats, i, j)
            curr_adj_occup = Counter(curr_adj)["#"]
            if curr == "L" and curr_adj_occup == 0:
                next_seats[i][j] = "#"
            if curr == "#" and curr_adj_occup >= 4:
                next_seats[i][j] = "L"
    return next_seats

curr_seats = deepcopy(seats)
while True:
    next_seats = next_round(curr_seats)
    if eq(next_seats, curr_seats):
        break
    else:
        curr_seats = next_seats

ct = Counter([b for a in next_seats for b in a])
print("part 1", ct["#"])


## part 2
def get_directions(seats, i, j):
    m = len(seats)
    n = len(seats[0])
    directions = []
    
    if j > 0:
        l = seats[i][:j]
        l = list(reversed(l))
        directions.append(l)
        if i < m - 1:
            lb = [seats[i + x][j - x] for x in range(1, min(j+1, m - i))]
            directions.append(lb)
        if i > 0:
            lt = [seats[i-x][j-x] for x in range(1, min(i+1, j+1))]
            directions.append(lt)
    if j < n - 1:
        r = seats[i][j+1:]
        directions.append(r)
        if i < m - 1:
            rb = [seats[i + x][j + x] for x in range(1, min(m - i, n - j))]
            directions.append(rb)
        if i > 0:
            rt = [seats[i - x][j + x] for x in range(1, min(i+1, n - j))]
            directions.append(rt)
    if i > 0:
        t = [seats[x][j] for x in range(i)]
        t = list(reversed(t))
        directions.append(t)
    if i < m - 1:
        b = [seats[x][j] for x in range(i + 1, m)]
        directions.append(b)
        
    
    return directions

def next_round2(seats):
    m = len(seats)
    n = len(seats[0])
    next_seats = deepcopy(seats)
    for i in range(m):
        for j in range(n):
            curr = seats[i][j]
            directions = get_directions(seats, i, j)
            curr_directions_occup = 0
            for direc in directions:
                if "#" in direc:
                    if "L" in direc:
                        if direc.index("#") < direc.index("L"):
                            curr_directions_occup += 1
                    else:
                        curr_directions_occup += 1
            if curr == "#"  and curr_directions_occup >= 5:
                next_seats[i][j] = "L"
            if curr == "L" and curr_directions_occup == 0:
                next_seats[i][j] = "#"
    return next_seats

test_dat = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''
test_dat = test_dat.splitlines()
test_dat = [list(x) for x in test_dat]

def part2(seats):
    curr_seats = deepcopy(seats)
    while True:
        next_seats = next_round2(curr_seats)
        if eq(next_seats, curr_seats):
            break
        else:
            curr_seats = next_seats
    
    return curr_seats


curr_states = part2(seats)
print("part 2", sum([row.count("#") for row in curr_states]))

