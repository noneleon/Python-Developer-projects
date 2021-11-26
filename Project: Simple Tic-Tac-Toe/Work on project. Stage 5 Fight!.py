'''
Description
Our game is almost ready! Now let's combine what we’ve learned in the previous stages to make a game of tic-tac-toe that two players can play from the beginning (with an empty grid) through to the end (until there is a draw, or one of the players wins).

The first player has to play as X and their opponent plays as O.

Objectives
In this stage, you should write a program that:

Prints an empty grid at the beginning of the game.
Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
Ends the game when someone wins or there is a draw.
You need to output the final result at the end of the game.

Good luck!

The project was changed. Now the coordinates start from the upper left corner. Look closely at the examples.
Example
The example below shows how your program should work.
Notice that after Enter the coordinates: comes the user input.

---------
|       |
|       |
|       |
---------
Enter the coordinates: 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: 2 2
This cell is occupied! Choose another one!
Enter the coordinates: two two
You should enter numbers!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: 3 3
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: 2 1
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: 3 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: 2 3
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
'''

import sys

cells = list(input('Enter cells:'))
# Converting input string into nested list
cells_list = []
for i in range(3):
    cells_list.append([cells[3 * i], cells[3 * i + 1], cells[3 * i + 2]])


# Printing X_Os desk
def cells_print(desk):
    print('---------')
    for i in range(3):
        print('|', desk[3 * i], desk[3 * i + 1], desk[3 * i + 2], '|', sep=' ')
    print('---------')


# Move procedure
def move():
    global cells_list
    global cells
    while True:
        coords = input('Enter the coordinates:').split()
        if len(coords) != 2:
            print('You should enter numbers!')
        elif not coords[0].isnumeric() and not coords[1].isnumeric():
            print('You should enter numbers!')
        elif int(coords[0]) not in [1, 2, 3] or int(coords[1]) not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
        elif cells_list[int(coords[0]) - 1][int(coords[1]) - 1] != '_':
            print('This cell is occupied! Choose another one!')
        else:
            cells_list[int(coords[0]) - 1][int(coords[1]) - 1] = 'X'
            cells[(int(coords[0]) - 1) * 3 + int(coords[1]) - 1] = 'X'
            cells_print(cells)
            break


cells_print(cells)
move()



\\\


user = True
turns = 0

rows = '_ _ _ _ _ _ _ _ _'.split()
initial_grid = [rows[i: i + 3] for i in range(0, 7, 3)]
border = '-' * 9
def print_game():
  print(border)
  for i in range(3):
    print('|', ' '.join(initial_grid[i]), '|')
  print(border)  
coordinates = [11, 12, 13, 21, 22, 23, 31, 32, 33]
assign_coor = dict(zip(coordinates, rows ))

def is_empty(coordinate):
  if int(coordinate) in assign_coor:
    if assign_coor[int(coordinate)] == 'X' or assign_coor[int(coordinate)] == 'O':
      return True
    else:
      return False      
  else:
    return False

def is_number(coordinate):
  if coordinate.isnumeric():
    return True
  else:
    return False

def is_bounds(coordinate):
  x = [4, 5, 6, 7, 8, 9, 0]
  y = [int(i) for i in coordinate]
    
  if y[0] in x or y[1] in x:
    return True
  else:
    return False  


def current_user(user):
  if user: return True
  else: return False


def playerX_move(coordinate):
  assign_coor[int(coordinate)] = 'X'
  new_game_rows = list(assign_coor.values())
  game_row_2 = [x for l in new_game_rows for x in l]
  print('-' * 9)
  board = [game_row_2[i:i + 3] for i in range(0, 7, 3)]
  for i in range(3):
    print('| ' + ' '.join(board[i]) + ' |')
  print('-' * 9)
def playerO_move(coordinate):
  assign_coor[int(coordinate)] = 'O'
  new_game_rows = list(assign_coor.values())
  game_row_2 = [x for l in new_game_rows for x in l]
  print('-' * 9)
  board = [game_row_2[i:i + 3] for i in range(0, 7, 3)]
  for i in range(3):
    print('| ' + ' '.join(board[i]) + ' |')
  print('-' * 9)
def check_game():
  new_grid = [i for i in assign_coor.values()]  
  row_pos = [(0, 1, 2), (3, 4,5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
  game_rows = [''.join(new_grid[i] for i in pos) for pos in row_pos]
  if abs(new_grid.count('X') - new_grid.count('O')) > 1:
    return 'Impossible'
  if 'XXX' in game_rows and 'OOO' in game_rows:
    return 'Impossible'
  if 'XXX' in game_rows:
    return 'X wins'
  if 'OOO' in game_rows:
    return 'O wins'
  if '_' not in new_grid:
    return 'Draw'
  return 'Game not finished' 

print_game()
while turns < 9:

  active_user = current_user(user)
  coordinate = input('Enter coordinates: ').replace(' ','')
  if not is_number(coordinate):
    print('You should enter numbers!')
    continue
  if is_bounds(coordinate):
    print('Coordinates should be from 1 to 3!')
    continue  
  if is_empty(coordinate):
    print('This cell is occupied! Choose another one!')
    continue
  if active_user:
    playerX_move(coordinate)
  if not active_user:
    playerO_move(coordinate)
  check_game()
  if check_game() == 'X wins':
    print('X wins')
    break
  if check_game() == 'O wins':
    print('O wins')
    break
  if turns == 8:
    print('Draw')
    break    
  turns += 1
  user = not user      
    

    
\\

def print_grid(input_):
    with_space = ''
    for letter in input_:
        with_space = with_space + letter + ' '
    print('---------')
    print('|', with_space[:5], '|')
    print('|', with_space[6:11], '|')
    print('|', with_space[12:17], '|')
    print('---------')

def coordinates_to_index(x, y):
    index = (x-1)*3 + (y-1)
    return index

def replace_index(input_string, index, replacment):
    temp = list(input_string)
    temp[index] = replacment
    return_string = ''.join(temp)
    return return_string

input_ = '_________'
print_grid(input_)
line = ''
column = ''
x_y = 0

while True:
    coordinate_input = input('Enter the coordinates:')
    if len(coordinate_input) != 3:
        print('You should enter numbers!')
        continue
    line, column = coordinate_input.split()
    if line.isnumeric() == True:
        if int(line) < 1 or int(line) > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            line = int(line)
    else:
        print('You should enter numbers!')
    if column.isnumeric() == True:
        if int(column) < 1 or int(column) > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            column = int(column)
    else:
        print('You should enter numbers!')
    if type(column) is int and type(line) is int:
        index = coordinates_to_index(line, column)
        if input_[index] == 'X' or input_[index] == 'O':
            print('This cell is occupied! Choose another one!')
        else:

            index = coordinates_to_index(line, column)
            if x_y % 2 == 0:
                input_ = replace_index(input_, index, 'X')
            if x_y % 2 == 1:
                input_ = replace_index(input_, index, 'O')
            print_grid(input_)
            winner = set()
            if abs(input_.count('X') - input_.count('O')) > 1:
                print('Impossible')
                quit()

            # get diagonal
            middle = input_[4]
            if input_[0] == middle and input_[-1] == middle or input_[2] == middle and input_[-3] == middle:
                winner.add(middle)

            # get row
            if input_[0:3] == 'XXX' or input_[3:6] == 'XXX' or input_[6:9] == 'XXX':
                winner.add('X')
            if input_[0:3] == 'OOO' or input_[3:6] == 'OOO' or input_[6:9] == 'OOO':
                winner.add('O')

            # get column
            column1 = [item for index, item in enumerate(input_) if index % 3 == 0]
            column2 = [item for index, item in enumerate(input_) if index % 3 == 1]
            column3 = [item for index, item in enumerate(input_) if index % 3 == 2]
            x_column = ['X', 'X', 'X']
            o_column = ['O', 'O', 'O']
            if column1 == x_column or column2 == x_column or column3 == x_column:
                winner.add('X')
            if column1 == o_column or column2 == o_column or column3 == o_column:
                winner.add('O')

            if len(winner) < 1:
                if input_.find('_') == -1:
                    print('Draw')
                    quit()

            if len(winner) > 1:
                print('Impossible')

            if len(winner) == 1:
                if 'X' in winner:
                    print('X wins')
                    quit()
                if 'O' in winner:
                    print('O wins')
                    quit()
            x_y += 1