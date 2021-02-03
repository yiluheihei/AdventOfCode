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

rules_msgs = {}
for k, v in rules.items():
    if v in ['"a"', '"b"']:
        rules_msgs[k] = v.replace('"', "")

# rules_msgs used for saving the rule messages which have been parsed


def get_msg(id, rules, rules_msgs):
    value = rules[id]
    if id in rules_msgs:
        msg = rules_msgs[id]
    else:
        if "|" not in value:
            child_ids = [item for item in re.split("\||\s+", value) if item != ""]
            if len(child_ids) == 1:
                msg = get_msg(child_ids[0], rules, rules_msgs)
                rules_msgs[id] = msg
            else:
                v1 = get_msg(child_ids[0], rules, rules_msgs)
                v2 = get_msg(child_ids[1], rules, rules_msgs)
                msg = [i + j for i in v1 for j in v2]
                rules_msgs[id] = msg
        else:
            child_ids = [item for item in re.split("\||\s+", value) if item != ""]
            if len(child_ids) == 2:
                v1 = get_msg(child_ids[0], rules, rules_msgs)
                v2 = get_msg(child_ids[1], rules, rules_msgs)
                msg = [i for i in v1] + [j for j in v2] 
                rules_msgs[id] = msg
            elif len(child_ids) == 4:
                vs = [get_msg(x, rules, rules_msgs) for x in child_ids]
                v1 = [i + j for i in vs[0] for j in vs[1]]
                v2 = [i + j for i in vs[2] for j in vs[3]]
                msg = [i for i in v1] + [j for j in v2]
                rules_msgs[id] = msg
            else:
                AssertionError("error")
    
    return msg
            
rule0 = get_msg("0", rules, rules_msgs)
match_rule = set(rule0).intersection(set(msgs))
### 111    
len(match_rule)

