from itertools import combinations

def read_file(file):
    with open(file) as f:
        tiles = f.read().split("\n\n")
    tiles = [tile.splitlines() for tile in tiles if tile != '']
    tile_ids = [tile[0][tile[0].index(" ") + 1:tile[0].index(":")] for tile in tiles]
    tile_imgs = [tile[1:] for tile in tiles]
    
    return dict(zip(tile_ids, tile_imgs))
    
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




