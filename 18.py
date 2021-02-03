import ast
import re

def read_file(file):
    with open(file) as f:
        exps = f.read().splitlines()
    
    return exps

# for expressions enclosed by parentheses, no recrusive
def evaluate_simple(simple_exp):
    values = re.split(r"\*|\+", simple_exp) 
    operators = [item for item in simple_exp if item in ["*", "+"]]
    exp = "".join(["(" for _ in operators]) + values[0]
    for i, item in enumerate(values[1:]):
        # if i < len(operators):
        exp = exp + operators[i] + item + ")"
    return eval(exp)
    
def find_neighbor_prt(exp):
    syms = [item for item in exp if item != " "]
    prt = []
    for i, sym in enumerate(syms):
        if sym == "(":
            curr_prts_idx = i
            next_prts_idx = i + syms[i+1:].index(")") + 1
            curr_syms = syms[curr_prts_idx + 1:next_prts_idx]
            if "(" not in curr_syms:
                prt.append((curr_prts_idx, next_prts_idx))
    return prt


def parse(exp):
    syms = [item for item in exp if item != " "]
    n_parts = find_neighbor_prt(exp)
    if len(n_parts):
        single_exps = ["".join(syms[np[0] + 1:np[1]]) for np in n_parts]
        single_value = [evaluate_simple(x) for x in single_exps]
        new_exp = "".join(syms)
        for i, np in enumerate(n_parts):
            new_exp = new_exp.replace("".join(syms[np[0]:np[1] + 1]), str(single_value[i]), 1)
        return parse(new_exp)
    else:
        return exp

exps = read_file("input/18_input.txt")
exps_value = [evaluate_simple(parse(exp)) for exp in exps]

# 7293529867931
sum(exps_value)


# # https://stackoverflow.com/questions/2154249/identify-groups-of-continuous-numbers-in-a-list
# from itertools import groupby
# from operator import itemgetter
# def get_continous_discrete_idx(ls):
#     ranges = []
#     for k, g in groupby(enumerate(ls), lambda x:x[0] - x[1]):
#         group = (map(itemgetter(1), g))
#         group = list(map(int,group))
#         ranges.append((group[0], group[-1]))
    
#     return ranges
            
    

# part 2
def evaluate_simple2(simple_exp, plus_first = True):
    values = re.split(r"\*|\+", simple_exp) 
    operators = [item for item in simple_exp if item in ["*", "+"]]
    if not plus_first:
        exp = "".join(["(" for _ in operators]) + values[0]
        for i, item in enumerate(values[1:]):
            exp = exp + operators[i] + item + ")"
    else:
        # plus = re.findall(r"([^*]+\+[^*]+)", simple_exp)
        # plus_new = ["(" + item + ")" for item in plus]
        exp = simple_exp
        # add parentheses in expressions whose operator is plus, e.g. 
        # a + b, or a + b + c
        exp = re.sub(r"([^*]+\+[^*]+)", r"(\1)", exp) 
    return eval(exp)
    
def parse2(exp, plus_first = True):
    syms = [item for item in exp if item != " "]
    n_parts = find_neighbor_prt(exp)
    if len(n_parts):
        single_exps = ["".join(syms[np[0] + 1:np[1]]) for np in n_parts]
        single_value = [evaluate_simple2(x, plus_first) for x in single_exps]
        new_exp = "".join(syms)
        for i, np in enumerate(n_parts):
            new_exp = new_exp.replace("".join(syms[np[0]:np[1] + 1]), str(single_value[i]), 1)
        return parse2(new_exp, plus_first)
    else:
        return exp


# part 1
exps_value1 = [evaluate_simple2(parse2(exp, False), False) for exp in exps] 
# 7293529867931
sum(exps_value1)

# part 2
sum([evaluate_simple2(parse2(exp)) for exp in exps])