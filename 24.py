from collections import Counter
from collections import defaultdict

## test tiles
tiles_test = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.splitlines()

# Cube coordinates (pointy topped) 
# https://www.redblobgames.com/grids/hexagons/

# input tiles
def read_tiles(file):
    with open(file) as f:
        tiles = f.read().splitlines()
    
    return tiles

coord = {'w': (-1, 1, 0), 'e': (1, -1, 0), 
    'se': (0, -1, 1), 'sw': (-1, 0, 1), 
    'nw': (0, 1, -1), 'ne': (1, 0, -1)}


def get_flip_direc(tile):
    tile = list(tile)
    all_direcs = ['e', 'se', 'sw', 'w', 'nw', 'ne']
    tile_flip_direc = []
    
    while tile:
        if "".join(tile[:2]) in all_direcs:
            curr_direc = "".join(tile[:2])
            tile = tile[2:]
        else:
            curr_direc = tile[0]
            tile = tile[1:]
        tile_flip_direc.append(curr_direc)
    
    return tile_flip_direc

def get_flip(tile, coord = coord):
    tile_direcs = get_flip_direc(tile)
    x = y = z = 0
    
    for direc in tile_direcs:
        direc_coord = coord[direc]
        x = direc_coord[0] + x
        y = direc_coord[1] + y
        z = direc_coord[2] + z
    
    return (x, y, z)



def get_black_tile(tiles, coord = coord):
    tiles_flipped = [get_flip(tile, coord) for tile in tiles]
    c = dict(Counter(tiles_flipped))
    black_tile = []
    
    for k, v in c.items():
        if v % 2 == 1:
            black_tile.append(k)
            
    return black_tile


# 521
black_tiles = get_black_tile(read_tiles('input/24_input.txt'), coord)
len(black_tiles)

###### part 2

def part2(black_tiles, day = 100):
    for _ in range(day):
        nbr = defaultdict(int)
        for x, y, z in black_tiles:
            for dx, dy, dz in coord.values():
                nbr[(x + dx, y + dy, z + dz)] += 1
        
        new_black_tiles = set()
        for k, v in nbr.items():
            if ((k not in black_tiles and v == 2) or
                (k in black_tiles and v in (1,2))):
                    new_black_tiles.add(k)
        black_tiles = new_black_tiles
        
    return len(black_tiles)

# 4242
part2(black_tiles)






        
        
        
        
    
        
        
    