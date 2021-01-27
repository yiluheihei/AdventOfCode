with open('input/12_input.txt') as f:
    instructions = f.read().splitlines()

# [east, west, north, south]
init = {"E": 0, "S": 0, "W": 0, "N": 0}
directions = ["E", "S", "W", "N"]
curr_direction = "E"

for instruc in instructions:
    curr_action = instruc[0]
    curr_value = int(instruc[1:])
    if curr_action == "F":
        init[curr_direction] += curr_value
    elif curr_action in ["E", "W", "N", "S"]:
        init[curr_action] += curr_value
    elif curr_action in ["R", "L"]:
        if curr_action == "L":
            curr_value = - curr_value
        curr_direction_ind = directions.index(curr_direction) + curr_value // 90
        if curr_direction_ind >= 4:
            curr_direction_ind -= 4
        curr_direction = directions[curr_direction_ind]
    else:
        raise AssertionError("error")
        

# 1441    
mahattan_dis = abs(init["E"] - init["W"]) + abs(init["N"]- init["S"])


## part2

ship = {"E": 0, "S": 0, "W": 0, "N": 0} 
wp = {"E": 10, "S":0, "W":0, "N":1}

def rotate_direction(wp, instruction):
    new_wp = wp.copy()
    directions = ["E", "S", "W", "N"]
    action = instruction[0]
    assert  action in ["L", "R"]
    
    value = int(instruction[1:])
    if action == "L":
        value = -value
    
    for k, v in wp.items():
        curr_direction_ind = directions.index(k) + value // 90
        if curr_direction_ind >= 4:
            curr_direction_ind -= 4
        new_wp[directions[curr_direction_ind]] = v
    
    return new_wp

for instruc in instructions:
    curr_action = instruc[0]
    curr_value = int(instruc[1:])
    
    if curr_action == "F":
        for k, v in ship.items():
            ship[k]  += curr_value * wp[k]
    elif curr_action in ["E", "W", "N", "S"]:
        wp[curr_action] +=  curr_value
    elif curr_action in ["R", "L"]:
        wp = rotate_direction(wp, instruc)
    else:
        raise AssertionError("error")

# 61616
mahattan_dis2 = abs(ship["E"] - ship["W"]) + abs(ship["N"]- ship["S"])
        
            
        
    


