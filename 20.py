from itertools import combinations
from functools import reduce
import regex as re

def read_file(file):
    with open(file) as f:
        tiles = f.read().split("\n\n")
    tiles = [tile.splitlines() for tile in tiles if tile != '']
    tile_ids = [tile[0][tile[0].index(" ") + 1:tile[0].index(":")] for tile in tiles]
    tile_imgs = [tile[1:] for tile in tiles]
    
    return dict(zip(tile_ids, tile_imgs))

# t, b, l, r, tr, br, lr, rr
def get_border(tile_img):
    border = []
    border = border + [tile_img[0]] + [tile_img[-1]]
    tile_flip = list(zip(*tile_img))
    border = border + ["".join(tile_flip[0])] + ["".join(tile_flip[-1])]
    
    border += ["".join(reversed(b)) for b in border]
    
    return border
    


tiles = read_file("input/20_input.txt")

tile_borders = {}
for k, v in tiles.items():
    tile_borders[k] = get_border(v)


def get_share_borders(tiles, tile_borders):
    new_tiles = tiles.copy()
    id_combs = combinations(new_tiles.keys(), 2)
    share_edges = {}
    for comb in id_combs:
        share_edges[comb] = set(tile_borders[comb[0]]).intersection(set(tile_borders[comb[1]]))
    share_edges = {k: v for k, v in share_edges.items() if v} 
    ids = [id for k in share_edges.keys() for id in k]
    share_count = {x:ids.count(x) for x in set(ids)}
    
    # corners have two adjacents
    corner = {k: v for k, v in share_count.items() if v == 2}
    
    return share_edges, corner

def part1():
    _, corner = get_share_borders(tiles, tile_borders)
    c = 1
    for k in corner.keys():
        c = c * int(k)
    
    return c

# 18482479935793
part1()


## part 2

# rotate or flip the tile
def transformers(tile):
    trans = [list(tile), list(tile[::-1])]
    trans = trans + [[line[::-1] for line in tran] for tran in trans]
    trans = trans + [["".join(line) for line in zip(*tran)] for tran in trans]
    
    return trans
    

def get_adj_id(tile_id, share_edges):
    adj_ids = [i for k, v in share_edges.items() if tile_id in k for i in k if i != tile_id]
    return adj_ids
    
def init_tiles(left = '3229', tiles = tiles):
    new_tiles = []
    remain_tiles = tiles.copy()
    init_trans = transformers(tiles[left])
    break_flag = False
    adj_ids = get_adj_id(left, share_edges)
    
    for l_tran in init_trans:
        right_border = get_border(l_tran)[3]
        for adj in adj_ids:
            right_trans = transformers(tiles[adj])
            for r_tran in right_trans:
                left_border = get_border(r_tran)[2]
                if left_border == right_border:
                    new_tiles.append((left, l_tran))
                    new_tiles.append((adj, r_tran))
                    remain_tiles.pop(left)
                    remain_tiles.pop(adj)
                    right_adj = adj
                    break_flag = True
                    break
            if break_flag:
                break
        if break_flag:
            break
    
    
    # the direction of the other adj
    other_adj = list(set(adj_ids).difference(set(right_adj)))[0]
    borders = get_border([t[1] for t in new_tiles if t[0] == left][0])
    
    # if top border in the adj, the direction is up, which means new_tiles is 
    # the last row tiles
    top_bd = borders[0]
    if top_bd in get_border(tiles[other_adj]):
        direction = "up"
    
    return new_tiles, direction, remain_tiles
    

def get_row_tiles(curr_tiles, tiles, n_row = 12, share_edges = share_edges):
    row_tiles = curr_tiles.copy()
    remain_tiles = tiles.copy()
    # n_row = int(len(tiles) ** 0.5)
    
    while len(row_tiles) < n_row:
        curr_tile = row_tiles[-1]
        right_border = get_border(curr_tile[1])[3]
        adj_ids = get_adj_id(curr_tile[0], share_edges)
        # remove the tiles have been positioned
        adj_ids = [i for i in adj_ids if i in remain_tiles.keys()]
        
        break_flag = False
        for adj in adj_ids:
            right_trans = transformers(remain_tiles[adj])
            for r_tran in right_trans:
                left_border = get_border(r_tran)[2]
                if left_border == right_border:
                    row_tiles.append((adj, r_tran))
                    remain_tiles.pop(adj)
                    break_flag = True
                    break
            if break_flag:
                break
            
    return row_tiles, remain_tiles
    

def get_next_row_tiles(row_tiles, direction, tiles, share_edges):
    remain_tiles = tiles.copy()
    # row_ids = [term[0] for term in row_tiles]
    # remain_tiles = {k: v for k, v in remain_tiles.items() if k not in row_ids}
    
    curr_row_tiles = row_tiles.copy()
    next_row_tiles = []
    
    for tile in curr_row_tiles:
        adj_ids = get_adj_id(tile[0], share_edges)
        
        # should be length one 
        adj_id = [i for i in adj_ids if i in remain_tiles.keys()]
        if len(adj_id) == 1:
            AssertionError("adj_id must be length one")
        next_tile = tiles[adj_id[0]]
        
        curr_borders = get_border(tile[1])
        if direction == "up":
            bd = curr_borders[0]
        elif direction == "down":
            bd = curr_borders[1]
        else:
            AssertionError("direction must be up or down")
            
        next_tile_trans = transformers(next_tile)
        
        for t in next_tile_trans:
            next_bds = get_border(t)
            if direction == "up":
                next_bd = next_bds[1]
            else:
                next_bd = next_bds[0]
            if next_bd == bd:
                next_row_tiles.append((adj_id[0], t))
                remain_tiles.pop(adj_id[0])
                break
                
            
    return next_row_tiles, remain_tiles
    

def get_all_tiles(curr_row_tiles, tiles, share_edges, direction = "up", n_col = 12):
    all_tiles = [curr_row_tiles]
    remain_tiles = tiles.copy()
    
    while len(all_tiles) < n_col:
        curr_row_tiles, remain_tiles = get_next_row_tiles(
            curr_row_tiles, 
            direction, 
            remain_tiles, 
            share_edges)
        all_tiles = [curr_row_tiles] + all_tiles
    
    return all_tiles


def remove_border(tile):
    new_tile = tile.copy()
    # remove the first and last element
    del new_tile[-1]
    del new_tile[0]
    
    # remove the first and last elment of each element
    return [line[1:-1] for line in new_tile]

def merge_tiles_in_row(tile1, tile2):
    res = []
    for i in range(len(tile1)):
        res.append("".join([tile1[i], tile2[i]]))
        
    return res
    
def merge_rows(row_tiles):
    return reduce(merge_tiles_in_row, row_tiles)
    
def merge_tiles(all_tiles):
    res = []
    for t in all_tiles:
        res = res + merge_rows(t)
        
    return res
    
def find_monster(img, pattern):
    img_trans = transformers(img)
    # the python internal re.findall return all non-overlapping matches of pattern in string
    # use regex.findall instead
    trans_flatten = [reduce(lambda x, y: "\n".join([x, y]), t) for t in img_trans] 
    for t in trans_flatten:
        monsters = re.findall(pattern, t, overlapped=True)
        if monsters:
            break
    
    return monsters
    
    
share_edges, corner = get_share_borders(tiles, tile_borders)
curr_tiles, direction, remain_tiles = init_tiles()
row_tiles, remain_tiles = get_row_tiles(curr_tiles, remain_tiles)
# next_row_tiles, remain_tiles = get_next_row_tiles(row_tiles, direction, tiles, share_edges)
all_tiles = get_all_tiles(row_tiles, remain_tiles, share_edges)

all_tiles_corrected = [[remove_border(t[1]) for t in row] for row in all_tiles]
tiles_final = merge_tiles(all_tiles_corrected)

# tiles_final_trans = transformers(tiles_final)
# trans_flattened = [reduce(lambda x, y: "\n".join([x, y]), t) for t in tiles_final_trans]
# pattern = re.compile(r'#.{77}#.{4}##.{4}##.{4}###.{77}(?:#.{2}){6}')
pattern = re.compile(r"(?:[.#]){18}#[.#](?:.|\n){77}#(?:[.#]){4}##(?:[.#]){4}##(?:[.#]){4}###(?:.|\n){77}[.#](?:#(?:[.#]){2}){5}#(?:[.#]){3}")

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
 
monsters = find_monster(tiles_final, pattern)
part2_res = sum([t.count("#") for t in tiles_final]) - len(monsters) * monster.count("#")
print(part2_res)

###================================ test

test_image = '''.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
'''.splitlines()