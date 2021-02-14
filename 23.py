## part 1    

def move(cups, step):
    # curr_cup = cups[0]
    n = len(cups)
    curr_cup = cups[0]
    
    for i in range(1, step + 1):
        curr_cup_idx = cups.index(curr_cup)
        pick_up = (cups*2)[curr_cup_idx + 1:curr_cup_idx + 4]
        cups_space = [x for x in cups if x not in pick_up]
        destination = curr_cup - 1
        
        # left_cups = [cup for cup in cups if cup not in pick_up]
        if destination < min(cups_space):
            destination = max(cups_space)
        else:
            while destination not in cups_space:
                destination = destination - 1
    
        destination_idx = cups_space.index(destination)
        new_cups = cups_space[:destination_idx + 1] + pick_up + cups_space[destination_idx + 1:]
        next_curr = cups_space[(cups_space.index(curr_cup) + 1) % (n - 3)]
        
        next_curr_idx = i % n
        double_new_cups = new_cups * 2
        idx = double_new_cups.index(next_curr, next_curr_idx)
        cups = double_new_cups[idx - next_curr_idx:idx + n - next_curr_idx]
        curr_cup = next_curr
        
    return cups
    
        

def part1():        
    cups = [int(x) for x in list("219347865")]
    cups_100 = move(cups, 100)
    idx = cups_100.index(1)
    after_1 = (cups_100 * 2)[idx + 1: idx + 9]
    
    return "".join([str(x) for x in after_1])

# 36472598
part1()


### part 2
def move2(cups, step, part1 = True):
    if not part1:
        cups = cups + list(range(max(cups) + 1, 10 ** 6 + 1))
    n = len(cups) 
    # create cups dictionary
    cups_dic = {}
    for i, cup in enumerate(cups):
        if i == len(cups) - 1:
            cups_dic[cup] = cups[0]
        else:
            cups_dic[cup] = cups[i + 1]
            
    curr_cup = cups[0]
    for i in range(step):
        next_1 = cups_dic[curr_cup]
        next_2 = cups_dic[next_1]
        next_3 = cups_dic[next_2]
        pick_up = [next_1, next_2, next_3]
        
        cups_space = [x for x in cups if x not in pick_up]
        destination = curr_cup - 1
        if destination < min(cups_space):
            destination = max(cups_space)
        else:
            while destination not in cups_space:
                destination = destination - 1
        
        
        # cups_dic[next_1] = next_2
        # cups_dic[next_2] = next_3
        cups_dic[curr_cup] = cups_dic[next_3]
        cups_dic[next_3] = cups_dic[destination]
        cups_dic[destination] = next_1
        
        curr_cup = cups_dic[curr_cup]
        
    if part1:
        res = []
        n = cups_dic[1]
        while n != 1:
            res.append(n)
            n = cups_dic[n]
        return "".join([str(x) for x in res])
    else:
        return cups_dic[1] * cups_dic[cups_dic[1]]
        
        
        
        

cups = [int(x) for x in list("219347865")] 
# part1: 36472598
move2(cups, 100)
# part 2:
move2(cups, 10 ** 7, False)

        
        
    