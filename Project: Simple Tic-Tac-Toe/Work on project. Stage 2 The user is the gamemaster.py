'''

Description
Our program should be able to display the grid at all stages of the game. Now we’re going to write a program that allows the user to enter a string representing the game state and correctly prints the 3x3 game grid based on this input. We’ll also add some boundaries around the game grid.

Objectives
In this stage, you will write a program that:

Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid. The grid can contain only X, O and _ symbols.
Outputs a line of dashes --------- above and below the grid, adds a pipe | symbol to the beginning and end of each line of the grid, and adds a space between all characters in the grid.
Examples
Examples below show how your output should look.
Notice that after Enter cells: comes the user input.

Example 1:

Enter cells: O_OXXO_XX
---------
| O _ O |
| X X O |
| _ X X |
---------
Example 2:

Enter cells: OXO__X_OX
---------
| O X O |
| _ _ X |
| _ O X |
---------
Example 3:

Enter cells: _XO__X___
---------
| _ X O |
| _ _ X |
| _ _ _ |
---------
'''

# write your code here
selection = tuple(input("Enter cells:"))
print("---------")
print("| "  + selection[0] + " " + selection[1] + " " + selection[2] + " |")
print("| "  + selection[3] + " " + selection[4] + " " + selection[5] + " |")
print("| "  + selection[6] + " " + selection[7] + " " + selection[8] + " |")
print("---------")


\\

input = input('Enter cells: ')


class tic_tac_toe():
    
    def __init__(self):
        self.colons = dict()
        self.lst = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']

    def create_dictionary(self):
        for x in self.lst:
            self.colons[x] = self.colons.get(x, '0')
        
    def assign_variable(self):
        x = 0
        for m in input:
            self.colons[self.lst[x]] = m
            x += 1
                
    def print_array(self):
        print('---------')
        print('|' + ' ' + self.colons['x1'] + ' ' + self.colons['x2'] + ' ' + self.colons['x3'] + ' ' + '|')
        print('|' + ' ' + self.colons['x4'] + ' ' + self.colons['x5'] + ' ' + self.colons['x6'] + ' ' + '|')
        print('|' + ' ' + self.colons['x7'] + ' ' + self.colons['x8'] + ' ' + self.colons['x9'] + ' ' + '|')
        print('---------')
    
    def main(self):
        self.create_dictionary()
        self.assign_variable()
        self.print_array()

play = tic_tac_toe()
play.main()

\\
def print_board(in_lst):
    top_bott = '---------'
    print(top_bott)
    for i in range(0, len(in_lst), 3):
        print('| ' + ' '.join(in_lst[i:i + 3]) + ' |')
    print(top_bott)

in_str = list(input('Enter board values: '))

print_board(in_str)

\\

current_board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'X', 'O']
]

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


def print_board(board):
    print(top_bottom)
    for line in board:
        print(f"| {' '.join(line)} |")
    print(top_bottom)


def main():
    user_board = get_board_from_line(input("Enter cells: "))
    print_board(user_board)


if __name__ == "__main__":
    main()
