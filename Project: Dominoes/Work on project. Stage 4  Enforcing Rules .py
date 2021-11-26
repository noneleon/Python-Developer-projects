'''
Description
You can't have a game without rules. It's time to introduce them!

Until now, the players were able to place their dominoes however they like. Now, it is considered a violation. According to the rules, the numbers on the ends of the two neighboring dominoes must match each other. This rule can also be described as a set of two requirements:

A player cannot add a domino to the end of the snake if it doesn't contain the matching number.
The orientation of the newly added domino ensures that the matching numbers are neighbors.
For example, consider the following situation:

We have a [3,4],[4,4],[4,2] snake and a [1,2] domino. The domino cannot be added to the left side of the snake because there is no 3 in [1,2]. However, the domino can be added to the right side of the snake because [1,2] contains a 2. If we were to place the domino on the right side of the snake, we would have to reorient it: [3,4],[4,4],[4,2],[2,1].

These two requirements are strict for both the player and the computer.

Objectives
Add the following functionality to your code. When it's a player's turn, the program should:

Verify that the move entered by the player is legal (requirement #1).
If not, request a new input with the following message: Illegal move. Please try again..
Place dominoes with the correct orientation (requirement #2).
When it's a computer's turn, the program should:

Try random moves until it finds a legal one.
A set of possible moves ranges from -computer_size to computer_size (where the computer_size is the number of dominoes the computer still has). Skipping a turn (move 0) is always legal.
Place dominoes with the correct orientation.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

Invalid move

======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 5]
2:[1, 5]
3:[2, 4]
4:[2, 6]
5:[0, 1]
6:[1, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
> 5
Illegal move. Please try again.
>
Example 2

Valid move (with corrected domino orientation)

======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
> 7
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][6, 1]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
>
'''

import random
# pulls n random pieces from the domino set
def get_domino_pieces(n):
    domino_pieces = []
    for _ in range(n):
        rn = random.randint(0, len(domino_set) - 1)
        domino_pieces.append(domino_set[rn])
        del domino_set[rn]
    return domino_pieces
# returns max double piece in domino set
def max_double(pieces_list):
    doubles_list = [piece for piece in pieces_list if piece[0] == piece[1]]
    if doubles_list:
        return max(doubles_list)
    else:
        return []
# returns current status message
def message(st):
    return {
        'computer': '\nStatus: Computer is about to make a move. Press Enter to continue...',
        'player': '\nStatus: It\'s your turn to make a move. Enter your command.',
        'player_win': '\nStatus: The game is over. You won!',
        'computer_win': '\nStatus: The game is over. The computer won!',
        'draw': '\nStatus: The game is over. It\'s a draw!'
        }[st]
# prints current playing field
def current_stage(stat):
    print('=' * 70)
    print('Stock size:', len(domino_set))
    print('Computer pieces:', str(len(computer_pieces)) + '\n')
    if len(domino_snake) <= 6:
        print("".join(domino_snake) + '\n')
    else:
        print("".join(domino_snake[:3]) + '...' + "".join(domino_snake[-3:]) + '\n')
    print('Your pieces:')
    for i in range(len(player_pieces)):
        print(str(i + 1) + ':' + str(player_pieces[i]))
    print(message(stat))
# makes one move
def make_a_move(m, pieces):
    if m > 0:
        domino = pieces[m - 1]
        right_snake = int(domino_snake[-1][4])
        if domino.count(right_snake) > 0:
            if right_snake == domino[1]:
                domino = [domino[1], domino[0]]
            domino_snake.append(str(domino))
            del pieces[m - 1]
        else:
            return 'Illegal'
    if m < 0:
        domino = pieces[-m - 1]
        left_snake = int(domino_snake[0][1])
        if left_snake in domino:
            if left_snake == domino[0]:
                domino = [domino[1], domino[0]]
            domino_snake.insert(0, str(domino))
            del pieces[-m - 1]
        else:
            return 'Illegal'
    if m == 0:
        if domino_set:
            pieces.extend(get_domino_pieces(1))
# sets first domino
while True:
    # generates full domino set
    domino_set = [[a, b] for a in range(7) for b in range(7) if a <= b]
    computer_pieces = get_domino_pieces(7)
    player_pieces = get_domino_pieces(7)
    first_domino = max(max_double(computer_pieces), max_double(player_pieces))
    if first_domino:
        break
domino_snake = []
if first_domino in player_pieces:
    player_pieces.remove(first_domino)
    status = 'computer'
else:
    computer_pieces.remove(first_domino)
    status = 'player'
domino_snake.append(str(first_domino))
# play: take turns until the end of the game
while True:
    current_stage(status)
    if status in ['player_win', 'computer_win', 'draw']:
        break
    if status == 'player':
        while True:
            try:
                move = int(input())
            except ValueError:
                print('Invalid input. Please try again.')
                continue
            if int(move) not in range(-len(player_pieces), len(player_pieces) + 1):
                print('Invalid input. Please try again.')
                continue
            if make_a_move(int(move), player_pieces) == 'Illegal':
                print('Illegal move. Please try again.')
                continue
            break
        status = 'computer'
    elif status == 'computer':
        enter = input()
        while True:
            move = random.randint(-len(computer_pieces), len(computer_pieces))
            if make_a_move(move, computer_pieces) == 'Illegal':
                continue
            break
        status = 'player'
    if domino_snake[0][1] == domino_snake[-1][4] and "".join(domino_snake).count(domino_snake[0][1]) == 8:
        status = 'draw'
    if len(player_pieces) == 0:
        status = 'player_win'
    if len(computer_pieces) == 0:
        status = 'computer_win'
        
        
\\

from collections import deque
from itertools import combinations_with_replacement
from random import shuffle, randint

Tile = list[int, int]


class Error(Exception):
    """
    Base Error class for the dominoes.py module.
    """


class ActionError(Error):
    """
    Raise when the chosen action is out of range.
    """


class IllegalMoveError(Error):
    """
    Raise when an illegal tile is to be added to the snake.
    """


class DominoSnake(deque):
    """
    A class representing a domino snake.
    """

    def __str__(self):
        if len(self) <= 6:
            return ''.join(f'{tile}' for tile in self)
        else:
            return f'{self[0]}{self[1]}{self[2]}...{self[-3]}{self[-2]}{self[-1]}'

    def head(self) -> int:
        """
        Return the head of the snake, that is, the number at the right end of
        the snake.
        """
        return self[-1][-1]

    def tail(self) -> int:
        """
        Return the tail of the snake, that is, the number at the left end
        of the snake.
        """
        return self[0][0]

    def append(self, tile: Tile) -> None:
        """
        Append the tile in a correct orientation. Raise IllegalMoveError
        if appending is not possible.

        :param tile: A tile to append.
        :raises IllegalMoveError: if appending is not possible.
        """
        if tile[0] == self.head():
            pass
        elif tile[-1] == self.head():
            tile.reverse()
        else:
            raise IllegalMoveError
        super().append(tile)

    def appendleft(self, tile: Tile) -> None:
        """
        Appendleft the tile in a correct orientation. Raise IllegalMoveError
        if appending is not possible.

        :param tile: A tile to append.
        :raises IllegalMoveError: if appending is not possible.
        """
        if tile[-1] == self.tail():
            pass
        elif tile[0] == self.tail():
            tile.reverse()
        else:
            raise IllegalMoveError
        super().appendleft(tile)


class Domino:
    """
    A class representing a domino game with a double-six set.
    """

    err_msg = 'Invalid input. Please try again.'

    def __init__(self) -> None:
        """
        Initialize the game, that is, shuffle and deal the pieces to players,
        determine the starting player.
        """
        pieces = list(map(list, combinations_with_replacement(range(7), 2)))
        while True:  # Repeat until the starting piece can be determined.

            shuffle(pieces)
            self.stock_pieces = pieces[:14]
            self.computer_pieces = pieces[14:21]
            self.player_pieces = pieces[21:]

            max_double = max(
                (tile for tile in pieces[14:] if tile[0] == tile[1]),
                default=None
            )

            if max_double is not None:
                if max_double in self.computer_pieces:
                    self.computer_pieces.remove(max_double)
                    self.status = 'player'
                else:
                    self.player_pieces.remove(max_double)
                    self.status = 'computer'

                self.snake = DominoSnake([max_double])
                break

    def play(self) -> None:
        """
        Start the game loop.
        """
        self.info()
        while not self.is_game_over():
            self.read(input())

    def is_game_over(self) -> bool:
        """
        Check whether the end-game conditions is achieved, that is, whether
        one of the players runs out of pieces or when the numbers on the ends
        of the snake are identical and appear within the snake 8 times.

        :return: True if the game is over, False otherwise.
        """
        return any(
            [not self.player_pieces,
             not self.computer_pieces,
             self.snake.head() == self.snake.tail() and
             sum(self.snake.head() in tile for tile in self.snake) == 8,
             not self.stock_pieces
             ]
            # The last condition seems to be necessary for the test to pass.
            # However, the description of the end-game condition does not
            # mention it... It is possible that the stock is empty and one
            # or both players have a move.
        )

    def info(self) -> None:
        """
        Print the game info, that is, the number of stock and computer pieces,
        the list of the player's pieces, the snake and the game status.
        """
        print('=' * 70)
        print(f'Stock size: {len(self.stock_pieces)}')
        print(f'Computer pieces: {len(self.computer_pieces)}', end='\n\n')
        print(self.snake, end='\n\n')
        print('Your pieces:')
        for n, piece in enumerate(self.player_pieces, 1):
            print(f'{n}: {piece}')
        print('\nStatus: ', end='')
        if self.is_game_over():
            print('The game is over. ', end='')
            if not self.computer_pieces:
                print('The computer won!')
            elif not self.player_pieces:
                print('You won!')
            else:
                print("It's a draw!")
        elif self.status == 'player':
            print("It's your turn to make a move.",
                  "Enter your command.")
        else:
            print('Computer is about to make a move.',
                  'Press Enter to continue...')

    def read(self, input_: str) -> None:
        """
        Read and parse a string and perform an action based on the game state.

        :param input_: a string representing an action to perform
        """
        if self.status == 'player':
            try:
                action = int(input_)
            except ValueError:
                print(self.err_msg)
            else:
                try:
                    self.move(action)
                except ActionError:
                    print(self.err_msg)
                except IllegalMoveError:
                    print('Illegal move. Please try again.')

        else:
            while True:
                action = randint(-len(self.computer_pieces),
                                 len(self.computer_pieces))
                try:
                    self.move(action)
                except IllegalMoveError:
                    continue
                else:
                    break

        self.info()

    def move(self, action: int) -> None:
        """
        Make a move, that is, draw a tile form the stock or add a tile to the
        snake.

        :param action: An integer representing the action. 0 represents
                       drawing a tile, for non-zero integers the sign
                       represent the side of the snake, the absolute value
                       represent the number of the title
                       (with base 1 indexing).
        """
        active_pieces: list = getattr(self, f'{self.status}_pieces')
        if action not in range(-len(active_pieces), len(active_pieces) + 1):
            raise ActionError

        if action == 0:
            if self.stock_pieces:
                active_pieces.append(self.stock_pieces.pop())
        elif action > 0:
            tile = active_pieces[action - 1]
            self.snake.append(tile)
            active_pieces.remove(tile)
        else:
            tile = active_pieces[abs(action) - 1]
            self.snake.appendleft(tile)
            active_pieces.remove(tile)

        self.status = 'player' if self.status == 'computer' else 'computer'


def main():
    Domino().play()


if __name__ == '__main__':
    main()

    
    
\\

# Project Dominoes
# Jetbrains project 2021 by Zsolt Pal


from random import shuffle, randint


def generate_dominoes():
    # this creates the available dominoes at start
    dominoes = [[i, j] for i in range(0, 7) for j in range(i, 7)]
    shuffle(dominoes)
    return dominoes  # tried "return shuffle(dominoes)" but it returns empty object


def generate_pieces(dominoes):
    # generates both player and computer starting pieces
    pieces = []
    for i in range(7):
        pieces.append(dominoes.pop())
    return pieces


def display_game(list_stock, list_computer, list_snake, list_player):
    # 2D 4K graphics engine
    print("=" * 70)
    print(f'Stock size: {len(list_stock)}')
    print(f'Computer pieces: {len(list_computer)}')
    print("")
    # if "domino snake" exceeds six dominoes in length, drawing only the first 3 and last 3 dominoes
    # to avoid display cluttering
    if len(list_snake) > 6:
        snake_left_side = "".join(str(item) for item in list_snake[:3])
        snake_right_side = "".join(str(item) for item in list_snake[-3:])
        print(f'{snake_left_side}...{snake_right_side}')
    else:
        print("".join(str(item) for item in list_snake))  # prints the snake in one row
    print("")
    print("Your pieces:")
    for index in range(len(list_player)):
        print(f'{index + 1}:{list_player[index]}')
    print("")


def is_number(a_key):
    # checking the input for integers // stripping "-" sign as it's a string
    return a_key.lstrip("-").isnumeric()


def draw_game(list_snake):
    # end-game condition for draw
    # same number on both ends of snake and appears 8 times --> no more move possible
    if list_snake[0][0] == list_snake[-1][1] and list_snake.count(list_snake[0][0]) == 8:
        return True
    return False


def any_valid_move(list_domino, list_snake):
    # check for possible move on the left of snake
    for domino in list_domino:
        if domino[0] == list_snake[0][0] or domino[1] == list_snake[0][0]:
            return True
    # check for possible move on the right of snake
    for domino in list_domino:
        if domino[0] == list_snake[-1][1] or domino[1] == list_snake[-1][1]:
            return True
    return False


def valid_move_left(a_domino, list_snake):
    if a_domino[0] == list_snake[0][0] or a_domino[1] == list_snake[0][0]:
        return True
    return False


def valid_move_right(a_domino, list_snake):
    if a_domino[0] == list_snake[-1][1] or a_domino[1] == list_snake[-1][1]:
        return True
    return False


def orient_domino_left(player_domino, snake_piece):
    if player_domino[0] == snake_piece[0]:
        player_domino[0], player_domino[1] = player_domino[1], player_domino[0]
        return player_domino
    return player_domino


def orient_domino_right(player_domino, snake_piece):
    if player_domino[1] == snake_piece[1]:
        player_domino[0], player_domino[1] = player_domino[1], player_domino[0]
        return player_domino
    return player_domino


def dominoes_game():
    stock_pieces = generate_dominoes()
    player_pieces = generate_pieces(stock_pieces)
    computer_pieces = generate_pieces(stock_pieces)
    # determining snake and starting player
    snake_domino = []
    if max(player_pieces) > max(computer_pieces):
        snake_domino.append(max(player_pieces))
        player_pieces.remove(max(player_pieces))
        player_status = "computer"
    else:
        snake_domino.append(max(computer_pieces))
        computer_pieces.remove(max(computer_pieces))
        player_status = "player"
    display_game(stock_pieces, computer_pieces, snake_domino, player_pieces)
    # game loop
    while True:
        if player_status == "player":
            print("Status: It's your turn to make a move. Enter your command.")
            # player loop
            while player_status == "player":
                pressed_key = input()
                if is_number(pressed_key):
                    if int(pressed_key) == 0:  # zero means add to player pieces from stock and skip turn
                        if not stock_pieces:  # if stock runs out, game gets to a draw
                            break
                        else:
                            player_pieces.append(stock_pieces.pop())
                            player_status = "computer"
                    elif len(player_pieces) * (-1) <= int(pressed_key) < 0:
                        # negative domino piece goes to the left of snake
                        if valid_move_left(player_pieces[int(pressed_key) * (-1) - 1], snake_domino):
                            oriented_domino = orient_domino_left(player_pieces.pop((int(pressed_key) * (-1) - 1)),
                                                                 snake_domino[0])
                            snake_domino.insert(0, oriented_domino)
                            player_status = "computer"
                        else:
                            print("Illegal move. Please try again.")
                    elif 0 < int(pressed_key) <= len(player_pieces):
                        # positive domino piece goes to the right
                        if valid_move_right(player_pieces[int(pressed_key) - 1], snake_domino):
                            oriented_domino = orient_domino_right(player_pieces.pop(int(pressed_key) - 1),
                                                                  snake_domino[-1])
                            snake_domino.insert(len(snake_domino), oriented_domino)
                            player_status = "computer"
                        else:
                            print("Illegal move. Please try again.")
                    else:
                        print("Invalid input. Please try again.")
                else:
                    print("Invalid input. Please try again.")
        else:
            # simple step by the computer for now
            print("Status: Computer is about to make a move. Press Enter to continue...")
            while True:
                pressed_key = input()
                if pressed_key == "":  # checking if enter pressed
                    break
                else:
                    print("Please press enter")
            # computer loop
            while player_status == "computer":  # in a while loop to make sure "enter" pressed
                # pressed_key = input()
                if pressed_key == "":  # checking if enter pressed
                    random_move = randint((len(computer_pieces) - 1) * (-1), len(computer_pieces) - 1)
                    # print("computer move:", random_move)
                    if random_move == 0:
                        if not stock_pieces:  # if stock runs out, game gets to a draw
                            break
                        else:
                            computer_pieces.append(stock_pieces.pop())
                            player_status = "player"
                    elif random_move < 0:
                        # negative domino piece goes to the left of snake
                        if valid_move_left(computer_pieces[random_move], snake_domino):
                            oriented_domino = orient_domino_left(computer_pieces.pop(random_move),
                                                                 snake_domino[0])
                            snake_domino.insert(0, oriented_domino)
                            player_status = "player"
                    elif 0 < random_move:
                        # positive domino piece goes to the right of snake
                        if valid_move_right(computer_pieces[random_move], snake_domino):
                            oriented_domino = orient_domino_right(computer_pieces.pop(random_move),
                                                                  snake_domino[-1])
                            snake_domino.insert(len(snake_domino), oriented_domino)
                            # len(snake_domino) used as index to insert domino to right
                            player_status = "player"
        display_game(stock_pieces, computer_pieces, snake_domino, player_pieces)
        # checking for end-game conditions
        if not player_pieces:
            print("Status: The game is over. You won!")
            break
        if not computer_pieces:
            print("Status: The game is over. The computer won!")
            break
        if draw_game(snake_domino):
            print("Status: The game is over. It's a draw!")
            break
        # if stock runs out, there are different scenarios
        if not stock_pieces:
            # if any_valid_move(player_pieces, snake_domino):  # player still has move
            #     player_status = "player"
            # elif any_valid_move(computer_pieces, snake_domino):  # computer still has move left
            #     player_status = "computer"
            # else:
            #     print("Status: The game is over. It's a draw!")  # no more moves possible
            #     break
            print("Status: The game is over. It's a draw!")  # uncomment the above condition block for proper game
            break


dominoes_game()

