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
        next_curr = cups_space[(cups_space.index(curr_cup) + 1) % 6]
        
        next_curr_idx = i % n
        double_new_cups = new_cups * 2
        idx = double_new_cups.index(next_curr, next_curr_idx)
        cups = double_new_cups[idx - next_curr_idx:idx + 9 - next_curr_idx]
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


        
        
    