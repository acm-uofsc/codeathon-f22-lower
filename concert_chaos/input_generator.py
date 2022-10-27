import random
import numpy as np
from solver import Solver

val = 52
nums_arr = [0] + [2*x + 1 for x in range((val))]

def random_letter_generator(values):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return random.sample(letters, values)


def dict_to_2d_arr(d):
    arr = [[0 for _ in range(int(final_size**(1/2)))]
           for _ in range(int(final_size**(1/2)))]

    for n1, i in enumerate(arr):
        for n2, j in enumerate(i):
            letter = random.choice(list(d.keys()))
            arr[n1][n2] = letter
            if d[letter] == 1:
                del d[letter]
            else:
                d[letter] = d[letter] - 1
    return arr


for file_number in range(60):
    i = random.randint(5, 26)
    d = {}
    index = 1
    final_size = 0
    for j in random_letter_generator(i):
        random_number = random.randint(0, 1)
        d[j] = nums_arr[index] + nums_arr[index+1]*random_number
        final_size = final_size + d[j]
        index = index + 1 + random_number

    matrix_size = int(final_size**(1/2))

    dict_file = open(f'dict_vals/dict{file_number}.txt', 'w+')
    dict_file.write(f"{str(d)}   {final_size}",)

    input_file = open(f'input/input{file_number}.txt', 'w+')
    input_file.write(f"{matrix_size}\n")

    arr = dict_to_2d_arr(d)
    for n1, row in enumerate(arr):
        for n2, element in enumerate(row):
            space = ' '*(n2+1 != matrix_size)
            input_file.write(f'{element}{space}')
        end = '\n'*(n1+1 != matrix_size)
        input_file.write(end)

    solve = Solver(arr)
    output = solve.main()
    output_file = open(f'output/output{file_number}.txt', 'w+')

    for n1, row in enumerate(output):
        for n2, element in enumerate(row):
            space = ' '*(n2+1 != matrix_size)
            output_file.write(f'{element}{space}')
        end = '\n'*(n1+1 != matrix_size)
        output_file.write(end)
