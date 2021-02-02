from functools import reduce

def read_input(file):
    with open(file) as f:
        input = f.read().splitlines()
    
    blank_indx = [i for i, item in enumerate(input) if item == ""]
    valid_data = input[:blank_indx[0]]
    my_ticket_data = input[blank_indx[1] - 1]
    nearby_ticket_data = input[blank_indx[1] + 2:]
    
    # valid range
    field_range = {}
    for valid in valid_data:
        valid_split = valid.split(":")
        field = valid_split[0]
        rg_split = valid_split[1].split("or")
        rg_split = [item.rstrip().lstrip().split("-") for item in rg_split]
        rg = [range(int(item[0]), int(item[1]) + 1) for item in rg_split]
        rg = list(rg[0]) + list(rg[1])
        field_range[field] = rg
    
    # my_ticket
    my_ticket = my_ticket_data.split(",")
    my_ticket = [int(item) for item in my_ticket]
    
    # nearby_tkt
    nearby_ticket = [[int(item) for item in ticket.split(",")] for ticket in nearby_ticket_data]
    
    return field_range, my_ticket, nearby_ticket
    
    
field_range, my_ticket, nearby_ticket = read_input("input/16_input.txt")

all_range = [i for x in field_range.values() for i in x]

def in_all_range(all_range, number):
    if number not in all_range:
        return False
    else:
        return True
    

error = {}
for i, tkt in enumerate(nearby_ticket):
    for number in tkt:
        if not in_all_range(all_range, number):
            error[i] = number

# 20060
sum(error.values())

## part 2
nearby_ticket_correct = nearby_ticket[:]
for i in reversed(list(error.keys())):
    del nearby_ticket_correct[i]

ticket_correct = nearby_ticket_correct + [my_ticket]


def get_correct_position(ticket, field_range):
    ticket = zip(*ticket)
    ps = {}
    for i, dat in enumerate(ticket):
        for k, v in field_range.items():
            if all([x in v for x in dat]):
                if k in ps:
                    ps[k] = ps[k] + [i]
                else:
                    ps[k] = [i]
    
    # sort
    ps = zip(ps.keys(), ps.values())
    ps_sorted = sorted(ps, key = lambda x: len(x[1]))
    ps_id = [item[1] for item in ps_sorted]
    ps_id_correct = []
    ps_id_correct.append(ps_id[0])
    
    for i in range(1, len(ps_id)):
        ps_id_correct.append(list(set(ps_id[i]) - set(ps_id[i - 1])))
        
    ps_id_correct = [x for item in ps_id_correct for x in item]
    
    return [item[0] for item in ps_sorted], ps_id_correct
    
field, ps = get_correct_position(ticket_correct, field_range)
departure = [ps[i] for i, item in enumerate(field) if "departure" in item]
my_departure = [my_ticket[i] for i in departure]

# 2843534243843
reduce(lambda x, y: x*y, my_departure)

