with open("input/05_input.txt") as f:
    dat = f.read().splitlines()


def get_seat_id(seat):
    assert len(seat) == 10, "seat由10个字符构成"
    assert not set(seat).difference({"F", "B", "L", "R"}), "字符必须为F , B, L,或 R"
    # F and L to 0, B and R to 1
    seat_chars = list(seat)
    new_seat = []
    for char in seat_chars:
        if char in ["F", "L"]:
            new_seat.append("0")
        else:
            new_seat.append("1")
    
    row = int("".join(new_seat[:7]), 2)
    col = int("".join(new_seat[7:]), 2)x
    
    id = row * 8 + col
    return id


seat_ids = [get_seat_id(x) for x in dat]

print("The highest seat ID is", max(seat_ids))


# part 2
id_sorted = sorted(seat_ids)

for i in range(len(id_sorted) - 1):
    step = id_sorted[i + 1] - id_sorted[i]
    if step != 1:
        idx = i

my_seat = id_sorted[idx] + 1
print("My seat ID is", my_seat)



    

