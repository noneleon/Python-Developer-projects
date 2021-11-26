'''
Description
It’s time to make our game interactive! Now we’re going to add the ability for a user to make a move.

To do this, we need to divide the grid into cells.

Suppose the top left cell has the coordinates (1, 1) and the bottom right cell has the coordinates (3, 3) like in this table:

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

The program should ask the user to enter the coordinates of the cell where they want to make a move.

In this stage, the user plays as X, not O. Keep in mind that the first coordinate goes from left to right and the second coordinate goes from top to bottom. Also note that coordinates start with 1 and can be 1, 2, or 3.

What happens if the user enters incorrect coordinates? The user could enter symbols instead of numbers, or enter coordinates representing occupied cells or cells that aren’t even on the grid. You need to check the user's input and catch possible exceptions.

Objectives
The program should work as follows:

Get the 3x3 grid from the input as in the previous stages.
Output this 3x3 grid as in the previous stages.
Prompt the user to make a move.
The user should input 2 numbers that represent the cell where they want to place their X. (the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
Analyze user input and show messages in the following situations:
This cell is occupied! Choose another one! if the cell is not empty.
You should enter numbers! if the user enters non-numeric symbols in the coordinates input.
Coordinates should be from 1 to 3! if the user enters coordinates outside the game grid.
Update the grid to include the user's move and print the updated grid to the console.
The program should also check the user’s input. If the input is unsuitable, the program should tell the user why their input was wrong, and prompt them to enter coordinates again.

To summarize, you need to output the game grid based on the first line of input, and then ask the user to enter a move. Keep asking until the user enters coordinates that represent an empty cell on the grid, update the grid to include that move, and then output it to the console. You should output the field only 2 times: once before the user’s move, and once after the user has entered a legal move.

Do not delete the code you already wrote that analyzes the game state; you will need it in the final step of this project.

The project was changed. Now the coordinates start from the upper left corner. Look closely at the examples.
Examples
The examples below show how your program should work.

Notice that after Enter cells: and Enter the coordinates: comes the user input.

Example 1:

Enter cells: X_X_O____
---------
| X   X |
|   O   |
|       |
---------
Enter the coordinates: 3 1
---------
| X   X |
|   O   |
| X     |
---------
Example 2:

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Example 3:

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 3 3
---------
|   X X |
| O O   |
| O X X |
---------
Example 4:

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 2 3
---------
|   X X |
| O O X |
| O X   |
---------
Example 5:

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 3 1
This cell is occupied! Choose another one!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Example 6:

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: one
You should enter numbers!
Enter the coordinates: one one
You should enter numbers!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Example 7:

Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------

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


\\


def display_grid(cell):
    print("---------")
    for i in range(0, len(cell), 3):
        print('| ' + ' '.join(cell[i:i + 3]) + ' |')
    print("---------")


cells = list(input("Enter cells: "))

coord_list = (
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
    )

display_grid(cell=cells)

while True:
    coord = input("Enter the coordinates: ")
    not_nums = [c for c in coord.split() if c.isalpha()]
    if len(not_nums) > 0:
        print('You should enter numbers!')
    else:
        nums = tuple([int(x) for x in coord.split(' ')])
        if (nums[0] > 3 or nums[1] > 3) or (nums[0] < 1 or nums[1] < 1):
            print('Coordinates should be from 1 to 3!')
        else:
            if cells[coord_list.index(nums)] == '_':
                cells[coord_list.index(nums)] = 'X'
                display_grid(cell=cells)

                break
            else:
                print('This cell is occupied! Choose another one!')

                
\\


def grid(cell):
    print("---------")
    for i in range(0, len(cell), 3):
        print('| ' + ' '.join(cell[i:i + 3]) + ' |')
    print("---------")


coord_list = (
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
)

cells = list(input("Enter cells: "))

grid(cell=cells)

while True:
    try:
        coord = tuple([int(x) for x in input("Enter the coordinates: ").split(' ')])

        if (coord[0] > 3 or coord[1] > 3) or (coord[0] < 1 or coord[1] < 1):
            print('Coordinates should be from 1 to 3!')

        if cells[coord_list.index(coord)] == '_':
            cells[coord_list.index(coord)] = 'X'
            grid(cell=cells)
            break
        else:
            print('This cell is occupied! Choose another one!')

    except ValueError:
        print('You should enter numbers!')
        

