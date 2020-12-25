with open("./input", "r") as f:
    file_input=f.readlines()

input_lines = [line.replace('\n', '') for line in file_input]

part_1_valid_count = 0
part_2_valid_count = 0

for line in input_lines:
    # 1-3 a: abcde
    rule, pwd = line.split(": ")
    char_to_count = rule.split(" ")[1]
    lower_limit, upper_limit = map(int, rule.split(" ")[0].split("-"))

    if lower_limit <= pwd.count(char_to_count) <= upper_limit:
        part_1_valid_count += 1

    count = 0
    try:

        if pwd[int(lower_limit) - 1] == char_to_count:
            count += 1
        if pwd[int(upper_limit) - 1] == char_to_count:
            count += 1
        if count == 1:
            part_2_valid_count += 1
    except:
        pass

print(f"Part 1 Count: {part_1_valid_count}\nPart 2 Count: {part_2_valid_count}")