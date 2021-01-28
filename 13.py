with open("input/13_input.txt") as f:
    dat = f.read().splitlines()

depart_time = int(dat[0])
bus_id = dat[1].split(",")
bus_id = [int(x) for x in bus_id if x != "x"]
bus_mod = [depart_time % x for x in bus_id]

wait = [bus_id[i] - bus_mod[i] for i in range(len(bus_id))]
wait_min = min(wait)
ind = wait.index(wait_min)

# 1915
bus_id[ind] * wait_min


## part 2
bus_seq = dat[1].split(',')
bus_seq = [int(x) if x != "x" else x for x in bus_seq]
bus_id = [{"id": bus, "index": i} for i, bus in enumerate(bus_seq) if busb != "x"] 

t = 0
step = bus_id[0]["id"]

for bus in bus_id:
    while (t + bus['index']) % bus["id"] != 0:
        t = t + step
    step = step * bus['id']

# 294354277694107
t