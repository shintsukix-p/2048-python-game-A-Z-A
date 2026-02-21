display(board)
#game-loop-and-game-over____________________________________________
def game_loop():
    global scorecopy
    global board
    global score
    highscore = read_highscore()
    print(f"Current Highscore: {highscore}")
    move = ''
    while move != 'q':
        board20 = copy.deepcopy(board)
        move = input('up/w down/s right/d left/a quit/q undo/u ')
        if move == 'a':
            board = left_aka_a(board)
        elif move == 'd':
            board = right_aka_d(board)
        elif move == 'w':
            board = up_aka_w(board)
        elif move == 's':
            board = down_aka_s(board)
        else :
            print('invalid')
            continue
        flaggg = game_over(board)
        if flaggg == 4:
            print('there is no more move left, game over!')
            break

        if board != board20:
            random_adding(board)
        if score > highscore:
            highscore = score
            save_highscore(highscore)
            print(f" new record: {highscore}")
        display(board)
        print('your current score :%d' %(score))
        print('best record: (%d)' %(highscore))