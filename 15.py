input = [11, 0, 1, 10, 5, 19]

def next_number(input):
    last_number = input[-1]
    previous_input = input[:-1]
    
    if last_number in previous_input:
        curr_number = list(reversed(previous_input)).index(last_number) + 1
    else:
        curr_number = 0
    
    return curr_number

# maximum recursion depth exceeded while
# def get_curr_input(input, n):
#     curr_number = next_number(input)
#     curr_in = input + [curr_number]
    
#     if len(curr_in) <= n:
#         curr_in = get_curr_input(curr_in, n)
    
#     return curr_in

## use iterative
def get_curr_input(input, n):
    n = n - len(input)
    for i in range(n):
        input = input + [next_number(input)]
    
    return input
        


# 870
# [11, 0, 1, 10, 5, 19, 0, 5, 3, 0, 3, 2, 0, 3, 3, 1,....]
get_curr_input(input, 2020)[-1]


## part 2

# use cache
cache = {}

for i, item in enumerate(input):
    cache[item] = i
    
def get_curr(input, cache, n):
    new_cache = cache.copy()
    prev = input[-1]
    for i in range(len(input), n):
        if prev in new_cache.keys():
            curr_number = i - 1 - new_cache[prev]
            new_cache[prev] = i - 1
        else:
            curr_number = 0
    
        if curr_number not in new_cache.keys():
            new_cache[curr_number] = i
        prev = curr_number
    
    return prev

# 9136
get_curr(input, cache, 30000000)    
