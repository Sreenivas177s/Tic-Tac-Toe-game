from past.builtins import raw_input
board = [['-a','-b','-c'],
         ['-d','-e','-f'],
         ['-g','-h','-i']]
def reset(board):
    board = [['-a', '-b', '-c'],
             ['-d', '-e', '-f'],
             ['-g', '-h', '-i']]
def check(marker,plyr):
    final = False
    if marker == board[0][0] and marker == board[1][1] and marker == board[2][2]:
        final = True
    if marker == board[0][2] and marker == board[1][1] and marker == board[2][0]:
        final = True
    else:
        for i in range(0,3):
            if marker == board[i][0] and marker == board[i][1] and board[i][2] == marker:
                final = True
            elif board[0][i] and board[1][i] and board[2][i] == marker:
                final =True
    if final:
        print(plyr,"Won the game")
        reset(board)
        exit(0)
def put(marker):
    place = raw_input("Enter the position in alphabets(a-i)")
    if place == 'a':
        board[0][0] = marker
    elif place == 'b':
        board[0][1] = marker
    elif place == 'c':
        board[0][2] = marker
    elif place == 'd':
        board[1][0] = marker
    elif place == 'e':
        board[1][1] = marker
    elif place == 'f':
        board[1][2] = marker
    elif place == 'g':
        board[2][0] = marker
    elif place == 'h':
        board[2][1] = marker
    elif place == 'i':
        board[2][2] = marker
    else:
        print("enter valid spot")
        put(marker)
def display():
    print(board[0][0],"  |  ",board[0][1],"  |  ",board[0][2])
    print("------------")
    print(board[1][0], "  |  ", board[1][1], "  |  ", board[1][2])
    print("------------")
    print(board[2][0], "  |  ", board[2][1], "  |  ", board[2][2])
ch = True
while(ch):
    print("TIC TAC TOE \n1.Start\t2.exit")
    choice = int(input("Enter choice \n 0 to exit \n 1 to continue"))
    if ch:
        pyr_1 = raw_input("Enter name of player 1")
        pyr_2 = raw_input("Enter name of player 2")
        print(pyr_1, "assigned with O\n", pyr_2, "assigned with X\n")
        if choice == 0:
            ch = False
        if choice == 1:
            for i in range(0,9):
                if i%2 ==0:

                    marker = 'X'
                    put(marker)
                    display()
                    check(marker,pyr_1)
                else:
                    marker = 'O'
                    put(marker)
                    display()
                    check(marker,pyr_2)

