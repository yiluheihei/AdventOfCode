import re
imporst string

with open("input/04_input.txt") as f:
    dat = f.read()

dat.split()

valid_vars = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
dat = re.split(r'\n\n', dat)
passports = [re.split(r'[\s\n]', x) for x in dat]

vars = []
n = 0
for passport in passports:
    vars = [re.split(r':', x)[0] for x in passport]
    diff_vars = set(valid_vars).difference(set(vars))
    if not len(diff_vars):
        n += 1



# part 2

def check_byr(ps):
    if 'byr' not in ps:
        return False
    if int(ps['byr']) in range(1920, 2003):
        return True
    else:
        False

def check_iyr(ps):
    if 'iyr' not in ps:
        return False
    if int(ps['iyr']) in range(2010, 2021):
        return True
    else:
        return False

def check_eyr(eyr):
    if 'eyr' not in ps:
        return False
    if int(ps['eyr']) in range(2020, 2031):
        return True
    else:
        return False

def check_hgt(ps):
    if 'hgt' not in ps:
        return False
    hgt = ps['hgt'] 
    if hgt[-2:] == "cm":
        if int(hgt[:-2]) in range(150, 194):
            return True
        else:
            return False
    if hgt[-2:] == "in":
        if int(hgt[:-2]) in range(59, 77):
            return True
        else:
            return False


def check_hcl(ps):
    if 'hcl' not in ps:
        return False 
    hcl = ps['hcl']
    if hcl[0:1] != "#":
        return False
    if len(hcl) != 7:
        return False
    
    valid_num = range(0, 10) 
    valid_char = [str(i) for i in valid_num] + list(string.ascii_lowercase[0:6])
    if set(hcl[1:]).difference(set(valid_char)):
        return False
    else:
        return True


def check_ecl(ps):
    if 'ecl' not in ps:
        return False 
    ecl = ps['ecl']
    
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(ps):
    if 'pid' not in ps:
        return False 
    pid = ps['pid']
    
    if len(pid) == 9:
        return True
    else:
        return False
    





n = 0
for passport in passports:
    # the last element of passorts contains '', since the last line is 
    # string is \n
    passport = list(filter(lambda x: x!="", passport))
    ps = dict([re.split(r':', x) for x in passport])
    if all([check_byr(ps), check_iyr(ps), check_eyr(ps), check_hgt(ps), check_hcl(ps), check_ecl(ps), check_pid(ps)]):
        n = n + 1
