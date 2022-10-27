import random
import numpy as np
from solver import Solver


def random_letter_generator(values):
    letters = [1, 2, 3] # 1 is add, 2 is sub, 3 is multiply
    return random.int





for file_number in range(80):
    random_number = random.randint(0, 1)
    limit = random.randint(1, 64) + 1


    input_file = open(f'input/input{file_number}.txt', 'w+')

    sol = 0
    for _ in range(int(limit/2)):
        i = random.randint(-32768, 32767)

        opcode = random.randint(1, 3)
        opcode = random.randint(1, 3)
        if opcode == 1:
            sol = (sol+i) & 65535
        elif opcode == 2:
            sol = (sol - i) & 65535
        else:
            sol = (sol*i) & 65535

        input_file.write(f'{opcode}\n{i}\n')
    output_file = open(f'output/output{file_number}.txt', 'w+')
    output_file.write(f"{sol}\n")

    print(file_number)
    input_file.write(f'0')

        
