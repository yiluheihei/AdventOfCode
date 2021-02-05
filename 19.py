import re

def read_file(file):
    with open(file) as f:
        input = f.read().splitlines()
    blank_idx = input.index("")
    
    return input[:blank_idx], input[blank_idx + 1:]
    
rules_orig, msgs = read_file("input/19_input.txt")

rules = {}
for rule in rules_orig:
    rule_splited = rule.split(":")
    rule_id = rule_splited[0]
    rule_value = rule_splited[1].lstrip()
    rules[rule_id] = rule_value

for k, v in rules.items():
    if v in ['"a"', '"b"']:
        rules[k] = v.replace('"', "")
        
rules_msgs = {}
rules_msgs['13'] = "b"
rules_msgs['7'] = 'a'

def get_msg2(id, rules, rules_msgs):
    value = rules[id]
    if id in rules_msgs:
        msg = rules_msgs[id]
    else:
        if "|" not in value:
            child_ids = [item for item in re.split("\||\s+", value) if item != ""]
            if len(child_ids) == 1:
                msg = get_msg2(child_ids[0], rules, rules_msgs)
                rules_msgs[id] = msg
            else:
                v1 = get_msg2(child_ids[0], rules, rules_msgs)
                v2 = get_msg2(child_ids[1], rules, rules_msgs)
                msg = [i + j for i in v1 for j in v2]
                rules_msgs[id] = msg
        else:
            child_ids = [item for item in re.split("\||\s+", value) if item != ""]
            if len(child_ids) == 2:
                v1 = get_msg2(child_ids[0], rules, rules_msgs)
                v2 = get_msg2(child_ids[1], rules, rules_msgs)
                msg = [i for i in v1] + [j for j in v2] 
                rules_msgs[id] = msg
            elif len(child_ids) == 4:
                vs = [get_msg2(x, rules, rules_msgs) for x in child_ids]
                v1 = [i + j for i in vs[0] for j in vs[1]]
                v2 = [i + j for i in vs[2] for j in vs[3]]
                msg = [i for i in v1] + [j for j in v2]
                rules_msgs[id] = msg
            else:
                AssertionError("error")
    
    return msg
    
msg_0 = get_msg2("0", rules, rules_msgs)
# 111
len(set(msg_0).intersection(set(msgs)))



######################## part 2 ######################

def get_msg(id, rules):
    rule = rules[id]
    rule = f" {rule} "
    sub_id = rule.split()
    
    while sub_id:
        value = sub_id.pop(0)
        if value in ['a', 'b']:
           rule = rule.replace(value, value.replace('"', ''))
        elif value not in ["|", "(", ")", ")+"]:
            value_msg = rules[value]
            # add space around value
            if "|" in value_msg:
                replace = "( " + value_msg + " )"
            else:
                replace = value_msg
            rule = rule.replace(f" {value} ", f" {replace} ")
        sub_id = [x for x in rule.split() if x not in ["(", "|", "a", "b", ")", ")+"]]
    
    return rule.replace(" ", "")
    

def part1(rules, msgs):
    pattern = get_msg("0", rules)
    count = sum([bool(re.fullmatch(pattern, msg)) for msg in msgs])
    
    return count

# 111
# part1(rules, msgs)

def part2(rules, msgs, rep_count):
    new_rules = rules.copy()
    new_rules["8"] = "( 42 )+"
    new_rules["11"] = "|".join(" 42 "*i + " 31 "*i for i in range(1, rep_count))
    pattern = get_msg("0", new_rules)
    count = sum([bool(re.fullmatch(pattern, msg)) for msg in msgs])
    
    return count
    
lp_42 = rules_msgs['42']
lp_31 = rules_msgs['31']
min_42 = min([len(x) for x in lp_42])
min_31 = min([len(x) for x in lp_31])
max_msg = max([len(x) for x in msgs])
rep_count = max_msg // (min_31 + min_42)
    
part2(rules, msgs, rep_count = rep_count)

