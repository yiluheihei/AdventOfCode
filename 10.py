from collections import Counter

with open("input/10_input.txt") as f:
    dat = f.read().splitlines()
dat = [int(x) for x in dat]
dat.sort()
dat.append(max(dat) + 3)

def next_adpt(curr_adpt, adpts):
    adpts.sort()
    if curr_adpt + 1 in adpts:
        n_adpt = curr_adpt + 1
        diff_jolt = 1
    elif curr_adpt + 2 in adpts:
        n_adpt = curr_adpt + 2
        diff_jolt = 2
    elif curr_adpt + 3 in adpts:
        n_adpt = curr_adpt + 3
        diff_jolt = 3
    else:
        raise AssertionError("different jolt must be one of 1,2, and 3")
    return n_adpt, diff_jolt

curr = 0
jolt_1_diff = 0
jolt_3_diff = 0

while True:
    curr, diff_jolt = next_adpt(curr, dat)
    if diff_jolt == 1:
        jolt_1_diff += 1
    if diff_jolt == 3:
        jolt_3_diff += 1
    if curr == max(dat):
        break

print("The result of part 1 is", jolt_3_diff * jolt_1_diff)


# part2

def get_jolt(dat):
    curr = 0
    # jolt_diff_1 = 0
    # jolt_diff_3 = 0
    diff_jolt = []
    
    while True:
        curr, jolt = next_adpt(curr, dat)
        diff_jolt.append(jolt) 
        if curr == max(dat):
            break
    return diff_jolt

jolt = get_jolt(dat)

# part 1
# jolt_n = Counter(jolt)
# jolt_n[1] * jolt_n[3]

# use recrusive directly, too too too slow
# def distinct_ways(chain, curr):
#     if curr == chain[0]:
#         return 1
#     elif curr == chain[1]:
#         return 1
#     elif curr == chain[2]:
#         return 2
#     elif curr == chain[3]:
#         return 4
#     else:
#         return sum([distinct_ways(chain, i) for i in range(curr-3, curr) if i in chain])

# distinct_ways(chain, 163)

# use cache
def distinct_ways2(chain, curr, cache):
    if curr in cache:
        return cache[curr]
    cache[curr] = sum([distinct_ways2(chain, i, cache) for i in range((curr-3), curr) if i in chain])
    return cache[curr]

cache = {chain[0]:1, chain[1]:1, chain[2]:2, chain[3]:4}

part2 = distinct_ways2(chain, chain[-1], cache)
print("part2", part2)

    

        
    
    


