import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def pt1_passport_check(passport_data):
    return all(field in passport_data.keys() for field in required_fields)

def part1():
    valid_passport_count = 0
    valid_passports = []

    with open(file='input') as f: # Open input file for reading
        lines = f.read().split('\n\n')
        passport_raw_data = []
        passports = []

        for line in lines:
            line = line.replace('\n',' ').split()
            passport_dict = {}
            for key_value in line:
                key_value = key_value.split(':')
                key = key_value[0]
                value = key_value[1]
                passport_dict.update({key:value})
            passports.append(passport_dict)

    for passport in passports:
        if pt1_passport_check(passport):
            valid_passports.append(passport)
    
    return valid_passports

print("\n----------- Start of Part 1 Result -----------")
print(f"There are {len(part1())} valid passports")
print("------------ End of Part 1 Result ------------\n")


def is_valid(passport):
    validation_list = []
    validation_list.append(1920 <= int(passport["byr"]) <= 2002)
    validation_list.append(2010 <= int(passport["iyr"]) <= 2020)
    validation_list.append(2020 <= int(passport["eyr"]) <= 2030)
    validation_list.append(((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) 
                    or (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76)))        
    validation_list.append(re.match(r'#[\da-f]{6}$', passport['hcl']))
    validation_list.append(passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    validation_list.append(re.match(r'\d{9}$', passport['pid']))
        
    return all(validation_list)

def part2():
    return len([passport for passport in part1() if is_valid(passport)])

print("\n----------- Start of Part 2 Result -----------")
print(part2())
print("------------ End of Part 2 Result ------------\n")
