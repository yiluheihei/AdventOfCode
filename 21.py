import re
from itertools import combinations
from functools import reduce

def read_file(file):
    with open(file) as f:
      foods = f.read().splitlines()
    foods = [re.findall(r"(.*)\s\(contains\s(.*)\)", f) for f in foods]
    
    ingres = []
    allergs = []
    for fd in foods:
        ingres.append(set(fd[0][0].split(" ")))
        allergs.append(set(fd[0][1].split(", ")))
    
    return ingres, allergs


def get_ingre_allerg(ingres, allergs):
    all_allergs = reduce(lambda x, y: x | y, allergs)
    all_allergs = list(all_allergs)
    ingres = [list(i) for i in ingres]
    
    ingre_allergs = {}
    
    # allergen and the corresponding integs
    for alg in all_allergs:
        alg_idx = [i for i, term in enumerate(allergs) if alg in term]
        sub_ings = [t for i, t in enumerate(ingres) if i in alg_idx]
        alg_ings = reduce(lambda x, y: set(x).intersection(set(y)), sub_ings)
        ingre_allergs[alg] = alg_ings
        
    # each allergen is found in exactly one ingredient
    res = {}
    while len(res) < len(ingre_allergs):
        for k, v in ingre_allergs.items():
            v = [i for i in v if i not in res.values()]
            if len(v) == 1:
                res[k] = v[0]
                break
    
    return res
    

def part1():
    ingres, allergs = read_file("input/21_input.txt")
    ingre_allerg = get_ingre_allerg(ingres, allergs)
    all_ingres = [[i for i in ing if i not in ingre_allerg.values()] for ing in ingres]
    res = sum([len(ing) for ing in all_ingres])
    
    return res

def part2():
    ingres, allergs = read_file("input/21_input.txt")
    ingre_allerg = get_ingre_allerg(ingres, allergs)
    
    k_sort = sorted(ingre_allerg)
    v_sort = [ingre_allerg[x] for x in k_sort]
    
    return ",".join(v_sort)
    
    
# 2075
part1()

# zfcqk,mdtvbb,ggdbl,frpvd,mgczn,zsfzq,kdqls,kktsjbh
part2()




