from itertools import combinations
from functools import reduce

COMB_SIZES = [2, 3]

def get_result(input_list, comb_size):
    count = 1
    output_prod = 1

    all_combs = combinations(input_list, comb_size)
    output_comb = next(filter(lambda comb: sum(comb) == 2020, all_combs))
    for num in output_comb:
        output_prod *= num
        print(f'Number {count}: {num}')
        count += 1
    
    print(f'\n-------Start of Solution for combination with size {comb_size}-------')
    print(f'The product is: {output_prod}')
    print(f'--------End of Solution for combination with size {comb_size}--------\n')


with open("./input") as f:
    lines = f.readlines()
input_list = list(map(int, lines))

for comb_size in COMB_SIZES:
    get_result(input_list, comb_size)
