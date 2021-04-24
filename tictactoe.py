board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

game_still_going = True

winner = None

current_player = "X"

#---------------------


def game():

    display_board()

    while game_still_going:

        coordinates(current_player)

        check_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner, "wins")
    elif winner == None:
        print("Draw")


def display_board():
    p = 9 * "-"
    print(p)
    print("|", board[0], board[1], board[2], "|", "    1 1 | 1 2 | 1 3")
    print("|", board[3], board[4], board[5], "|", "    2 1 | 2 2 | 2 3")
    print("|", board[6], board[7], board[8], "|", "    3 1 | 3 2 | 3 3")
    print(p)


def coordinates(player):

    print(player + "'s turn")

    while True:

        n = input("Enter the coordinates: ").split()

        if (n[0].isnumeric() and n[1].isnumeric()) != True:
            print("You should enter numbers!")
            continue
        elif int(n[0]) > 3 or int(n[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif board[(int(n[0])-1)*3 + (int(n[1])-1)] in ["X", "O"]:
            print("This cell is occupied! Choose another one!")
            continue
        break

    board[(int(n[0])-1)*3 + (int(n[1])-1)] = player

    display_board()


def check_game_over():
  check_winner()
  check_draw()


def check_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():

    global game_still_going

    row1 = board[0] == board[1] == board[2] != " "
    row2 = board[3] == board[4] == board[5] != " "
    row3 = board[6] == board[7] == board[8] != " "

    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():

    global game_still_going

    column1 = board[0] == board[3] == board[6] != " "
    column2 = board[1] == board[4] == board[7] != " "
    column3 = board[2] == board[5] == board[8] != " "

    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[1]
    elif column2:
        return board[2]
    elif column3:
        return board[6]
    else:
        return None


def check_diagonals():

    global game_still_going

    diagonal1 = board[0] == board[4] == board[8] != " "
    diagonal2 = board[2] == board[4] == board[6] != " "

    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None


def check_draw():

    global game_still_going

    if " " not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():

  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"


game()
