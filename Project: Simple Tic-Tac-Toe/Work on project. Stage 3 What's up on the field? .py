'''
Description
In this stage, we’re going to analyze the game state to determine if either player has already won the game or it is still ongoing, if the game is a draw, or if the user has entered an impossible game state (two winners, or with one player having made too many moves).

Objectives
In this stage, your program should:

Take a string entered by the user and print the game grid as in the previous stage.
Analyze the game state and print the result. Possible states:
Game not finished when neither side has three in a row but the grid still has empty cells.
Draw when no side has a three in a row and the grid has no empty cells.
X wins when the grid has three X’s in a row.
O wins when the grid has three O’s in a row.
Impossible when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).
In this stage, we will assume that either X or O can start the game.

You can choose whether to use a space or underscore _ to print empty cells.

Examples
The examples below show outputs and analysis results for different game states. Your program should work in the same way.

Notice that after Enter cells: comes the user input.

Example 1:

Enter cells: XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
Example 2:

Enter cells: XOXOXOXXO
---------
| X O X |
| O X O |
| X X O |
---------
X wins
Example 3:

Enter cells: XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins
Example 4:

Enter cells: XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw
Example 5:

Enter cells: XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished
Example 6:

Enter cells: XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible
Example 7:

Enter cells: _O_X__X_X
---------
|   O   |
| X     |
| X   X |
---------
Impossible
Example 8:

Enter cells: _OOOO_X_X
---------
|   O O |
| O O   |
| X   X |
---------
Impossible

'''
# write your code here
cells = list(input())


def wins(array):
    is_empty = "_" in array
    if (array[0] != "_") and (array[0] == array[1]) and (array[1] == array[2]):
        print(array[0] + " " + "wins")
    elif (array[3] != "_") and (array[3] == array[4]) and (array[4] == array[5]):
        print(array[3] + " " + "wins")
    elif (array[6] != "_") and (array[6] == array[7]) and (array[7] == array[8]):
        print(array[6] + " " + "wins")
    elif (array[0] != "_") and (array[0] == array[3]) and (array[3] == array[6]):
        print(array[0] + " " + "wins")
    elif (array[1] != "_") and (array[1] == array[4]) and (array[4] == array[7]):
        print(array[1] + " " + "wins")
    elif (array[2] != "_") and (array[2] == array[5]) and (array[5] == array[8]):
        print(array[2] + " " + "wins")
    elif (array[0] != "_") and (array[0] == array[4]) and (array[4] == array[8]):
        print(array[0] + " " + "wins")
    elif (array[2] != "_") and (array[2] == array[4]) and (array[4] == array[6]):
        print(array[2] + " " + "wins")
    elif not is_empty:
        print("Draw")
    elif is_empty:
        print("Game not finished")


def impossible(array):
    x_count = 0
    o_count = 0
    wins_count = 0
    for i in array:
        if i == "X":
            x_count += 1
        elif i == "O":
            o_count += 1
    if (array[0] != "_") and (array[0] == array[1]) and (array[1] == array[2]):
        wins_count += 1
    if (array[3] != "_") and (array[3] == array[4]) and (array[4] == array[5]):
        wins_count += 1
    if (array[6] != "_") and (array[6] == array[7]) and (array[7] == array[8]):
        wins_count += 1
    if (array[0] != "_") and (array[0] == array[3]) and (array[3] == array[6]):
        wins_count += 1
    if (array[1] != "_") and (array[1] == array[4]) and (array[4] == array[7]):
        wins_count += 1
    if (array[2] != "_") and (array[2] == array[5]) and (array[5] == array[8]):
        wins_count += 1
    if x_count - o_count >= 2 or o_count - x_count >= 2:
        print("Impossible")
        return True
    elif wins_count > 1:
        print("Impossible")
        return True
    else:
        return False


print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")

is_impossible = impossible(cells)
if not is_impossible:
    wins(cells)


    
\\

top_bottom = "---------"


def get_board_from_line(user_input):
    outer_counter = 0
    inner_counter = 0
    board = [
        [],
        [],
        []
    ]
    for c in list(user_input):
        # print(c)
        board[outer_counter].append(c)
        inner_counter += 1
        if inner_counter == 3:
            inner_counter = 0
            outer_counter += 1
    return board


def check_line(line, player):
    # print(set(line))
    if len(set(line)) == 1 and set(line) == {player}:
        return True
    else:
        return False


def check_diagonal(board, player):
    if check_line([board[0][0], board[1][1], board[2][2]], player):
        return True
    if check_line([board[0][2], board[1][1], board[2][0]], player):
        return True
    return False


def check_win(board, player):
    if check_diagonal(board, player):
        return True
    for i in range(0, 3):
        if check_line(board[i], player):
            return True
        elif check_line([board[i][i], board[i-1][i], board[i-2][i]], player):
            return True
    return False


def print_board(board):
    print(top_bottom)
    for line in board:
        print(f"| {' '.join(line)} |")
    print(top_bottom)


def check_error(board):
    x_count = 0
    o_count = 0
    for line in board:
        x_count += line.count('X')
        o_count += line.count('O')
    if x_count - o_count >= 2 or o_count - x_count >= 2:
        return True
    else:
        return False


def check_dash(board):
    for line in board:
        if "_" in line:
            return True
    return False


def main():
    user_board = get_board_from_line(input("Enter cells: "))
    print_board(user_board)
    o_win = check_win(user_board, 'O')
    x_win = check_win(user_board, 'X')
    if (x_win and o_win) or check_error(user_board):
        print("Impossible")
    elif x_win:
        print("X wins")
    elif o_win:
        print("O wins")
    elif check_dash(user_board):
        print("Game not finished")
    else:
        print("Draw")


if __name__ == "__main__":
    main()

    
\\

# write your code here
print("Enter cells:")
user_input = input() #_XO__X___
print("---------")
print("|", user_input[0], user_input[1], user_input[2], "|")
print("|", user_input[3], user_input[4], user_input[5], "|")
print("|", user_input[6], user_input[7], user_input[8], "|")
print("---------")

flag_impossible = False

if user_input.count("X") - user_input.count("O") > 1:
    print("Impossible")
elif user_input.count("O") - user_input.count("X") > 1:
    print("Impossible")
elif user_input[0:2] == user_input[3:5]:
    print("Impossible")
    flag_impossible = True
elif user_input[3:5] == user_input[6:8]:
    print("Impossible")
    flag_impossible = True
elif user_input[0] == user_input[3] and user_input[3] == user_input[6] and user_input[1] == user_input[4] and user_input[4] == user_input[7]:
    print("Impossible")
    flag_impossible = True
elif user_input[1] == user_input[4] and user_input[4] == user_input[7] and user_input[2] == user_input[5] and user_input[5] == user_input[8]:
    print("Impossible")
    flag_impossible = True
elif user_input[0] == user_input[1] and user_input[1] == user_input[2] and flag_impossible is False:
    print(user_input[0], "wins")
elif user_input[3] == user_input[4] and user_input[4] == user_input[5] and flag_impossible is False:
    print(user_input[3], "wins")
elif user_input[6] == user_input[7] and user_input[7] == user_input[8] and flag_impossible is False:
    print(user_input[6], "wins")
elif user_input[0] == user_input[3] and user_input[3] == user_input[6] and flag_impossible is False:
    print(user_input[0], "wins")
elif user_input[1] == user_input[4] and user_input[4] == user_input[7] and flag_impossible is False:
    print(user_input[1], "wins")
elif user_input[2] == user_input[5] and user_input[5] == user_input[8] and flag_impossible is False:
    print(user_input[2], "wins")
elif user_input[0] == user_input[4] and user_input[4] == user_input[8] and flag_impossible is False:
    print(user_input[0], "wins")
elif user_input[2] == user_input[4] and user_input[4] == user_input[6] and flag_impossible is False:
    print(user_input[2], "wins")
elif "_" in user_input and flag_impossible is False:
    print("Game not finished")
else:
    print("Draw")



