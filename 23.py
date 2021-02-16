################################## first version    

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


############################################ second version use dictionary

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


############################ third version for better performance
# https://github.com/aribchowdhury/AdventOfCode2020/blob/master/day23/day23.py

class Node:
    __slots__ = ['val', 'next']
    
    def __init__(self, val, next):
        self.val = val
        self.next = next

def move3(cups, step):
    n = len(cups)
    
    # node dict
    node_dict = {i: Node(i, None) for i in range(1, n + 1)}
    for i in range(n):
        node_dict[cups[i]].next = node_dict[cups[(i + 1) % n]]
    
    curr_cup = node_dict[cups[0]]
    
    for _ in range(step):
        next_1 = curr_cup.next
        next_2 = next_1.next
        next_3 = next_2.next
        curr_cup.next = next_3.next
        
        destination = curr_cup.val
        while destination in (curr_cup.val, next_1.val, next_2.val, next_3.val):
            if destination > 1:
                destination = destination - 1
            else:
                destination = n
        destination = node_dict[destination]
        next_3.next = destination.next
        destination.next = next_1
        
        curr_cup = curr_cup.next
        
    
    return curr_cup, node_dict
        

def update_part1(cups, step):
    _, node_dict = move3(cups, step)
    p = node_dict[1]
    res = []
    for _ in range(len(cups) - 1):
        p = p.next
        res.append(str(p.val))
        
    return "".join(res)
        

cups = [int(x) for x in list('219347865')]
# 36472598
update_part1(cups, 100)


def part2(cups, step):
    _, node_dict = move3(cups, step)
    p = node_dict[1]
    
    return p.next.val * p.next.next.val


new_cups =  cups + list(range(max(cups) + 1, 10 ** 6 + 1))
# 90481418730
part2(new_cups, 10 ** 7)
        