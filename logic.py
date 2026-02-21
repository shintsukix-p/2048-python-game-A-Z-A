#lib___________________________________________________________

import random
import copy
import os

#board-display_________________________________________________

length = 4
board =[[0] * length for item in range(length)]

def display(board1):
    for satr in board1:
        for item in satr:
            if item == 0:
                print( '.  ',end='')
            else:
                print(item+'  ', end='')
        print()
    print()
    print('-' * 19)

#score-files____________________________________________________
score = 0

def read_highscore(filename="highscore.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read().strip()
            if content.isdigit():
                return int(content)
    return 0
def save_highscore(new_score, filename="highscore.txt"):
    with open(filename, "w") as f:
        f.write(str(new_score))

  
#random-finding-0s______________________________________________


def finding_empty(board2):
    empty = []
    for i in range(length):
        for j in range(length):
            if board2[i][j] == 0:
                empty.append((i, j))
    return empty

def A90_B10():
    if random.random() < 0.9 :
        return 'A'
    return 'B'

def random_adding(board3):
    empty_deraye = finding_empty(board3)
    random_empty_deraye = random.choice(empty_deraye)
    i = random_empty_deraye[0]
    j = random_empty_deraye[1]
    chosen_deraye = A90_B10()
    board3[i][j] = chosen_deraye

for i in range(2):
    random_adding(board)

#move-lef_____________________________________________________

def left_del_zeros(board4):
    for i in range(length):
        new_satr = [j for j in board4[i] if j != 0]
        board4[i] = new_satr
    return board4

def left_add_zeros(board5):
    for i in range(length):
        while len(board5[i]) != 4:
            board5[i].append(0)
    return board5

def left_merg(board6):
    for satr in board6:
        for j in range(length - 1):
            if satr[j] == satr[j + 1] and satr[j] != 0:
                satr[j] = chr(ord(satr[j]) + 1)
                satr[j + 1] = 0
                global score
                score += (ord(satr[j]) - 64)
    return board6


def left_aka_a(board7):
    board7 = left_del_zeros(board7)
    board7 = left_add_zeros(board7)
    board7 = left_merg(board7)
    board7 = left_del_zeros(board7)
    board7 = left_add_zeros(board7)
    return board7

#move-right______________________________________________________

def right_rutate(board8):
    for i in range(length):
        satr = board8[i]
        new_satr = satr[: :-1]
        board8[i] = new_satr
    return board8


def right_aka_d(board9):
    board9 = right_rutate(board9)
    board9 = left_aka_a(board9)
    board9 = right_rutate(board9)
    return board9

#move-up_________________________________________________________

def up_rutate(board10):
    board10_copy = copy.deepcopy(board10)
    for i in range(length):
        for j in range(length):
            board10[i][j] = board10_copy[j][i]
    return board10

def up_aka_w(board11):
    board11 = up_rutate(board11)
    board11 = left_aka_a(board11)
    board11 = up_rutate(board11)
    return(board11)

#move-down_________________________________________________________


def down_aka_s(board13):
    board13 = up_rutate(board13)
    board13 = right_rutate(board13)
    board13 = left_aka_a(board13)
    board13 = right_rutate(board13)
    board13 = up_rutate(board13)
    return board13


#game-over___________________________________________________________

def game_over(board15):
    global scorecopy
    global score
    scorecopy = score
    flagg = 0
    board16 = copy.deepcopy(board15)
    board17 = copy.deepcopy(board15)
    board18 = copy.deepcopy(board15)
    board19 = copy.deepcopy(board15)
    board16 = left_aka_a(board16)
    if board16 == board15:
        flagg +=1
    board17 = right_aka_d(board17)
    if board17 == board15:
        flagg += 1
    board18 = up_aka_w(board18)
    if board18 == board15:
        flagg += 1
    board19 = down_aka_s(board19)
    if board19 == board15:
        flagg += 1
    score = scorecopy
    return flagg