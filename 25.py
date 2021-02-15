def transform(value=1, sn=7, ls = 1):
    for _ in range(ls):
        value = (value * sn) % 20201227
    return value

key1 = 16915772
key2 = 18447943

value = 1
ls1 = 0
while value != key1:
    ls1 += 1
    value = (value * 7) % 20201227

# 6011069
transform(1, key2, ls1)