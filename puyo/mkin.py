#!/usr/local/bin/python3.9

from random import randint, choice
from enum import Enum
case_num = int(input())


class Moves(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3 
    RIGHT = 4

def random_stroke(brd):
    color = randint(1, 7)
    size = randint(1,9)
    r = randint(0, len(brd) - 1)
    c = randint(0, len(brd[0]) - 1)
    possible_moves = list(Moves)
    

    # unroll first iteration to initialize
    # only later did I realize last_direction=null initally might be more pythonic
    direction = choice(possible_moves)

    tr = r   
    tc = c

    # move stroke
    if (direction == Moves.UP): tr -= 1
    elif (direction == Moves.DOWN): tr += 1
    elif (direction == Moves.LEFT): tc -= 1
    elif (direction == Moves.RIGHT): tc += 1
    
    # bounds check
    if tr <  len(brd) and tr >= 0 and tc < len(brd[0]) and tc >= 0:
         r = tr
         c = tc

    # paint stroke 
    brd[r][c] = color
    
    last_direction = direction
    possible_moves.remove(direction)

    for _ in range(size - 1):
         direction = choice(possible_moves)

         # move stroke
         if (direction == Moves.UP): tr -= 1
         elif (direction == Moves.DOWN): tr += 1
         elif (direction == Moves.LEFT): tc -= 1
         elif (direction == Moves.RIGHT): tc += 1

         # bounds check
         if tr <  len(brd) and tr >= 0 and tc < len(brd[0]) and tc >= 0:
             r = tr
             c = tc
         else:
             tr = r
             tc = c

         # paint stroke 
         brd[r][c] = color

         possible_moves.remove(direction)
         possible_moves.append(last_direction)
         last_direction = direction
    return brd


if case_num == 0:
    print(7,6)
    board = [
                [ 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0],
                [ 0, 4, 4, 0, 0, 0],
                [ 0, 3, 3, 0, 0, 0],
                [ 0, 2, 3, 0, 0, 0],
                [ 2, 2, 3, 0, 0, 0],
                [ 1, 1, 1, 1, 1, 0]
             ] 
    for row in board:
        print(*row, sep=' ')

else:
    n = randint(12,2 ** 6)
    m = randint(6, 2 ** 5)
    print(n,m)
    board = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(n * m + randint(-6, m)):
        board = random_stroke(board)

    for row in board:
       print(*row, sep=' ')
