'''
Description
It's time to bring the game to life. In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.

In dominoes, you can make a move by taking one of the following actions:

Select a domino and place it on the right side of the snake.
Select a domino and place it on the left side of the snake.
Take an extra piece from the stock (if it's not empty) and skip a turn.
To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: {side_of_the_snake (+/-), domino_number (integer)} or {0}. For example:
-6 : Take the sixth domino and place it on the left side of the snake.
6 : Take the sixth domino and place it on the right side of the snake.
0 : Take an extra piece from the stock (if it's not empty) and skip a turn.

When it's time for the player to make a move, your program must prompt the user for a number. If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. Once the valid input is received, your program must apply the move.

For now, don't bother about the AI, our goal is just to make the game playable. So, when it's time for the computer to make a move, make it choose a random number between -computer_size and computer_size (where the computer_size is the number of dominoes the computer has).

The end-game condition can be achieved in two ways:

One of the players runs out of pieces. The first player to do so is considered a winner.
The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake below will satisfy this condition:
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]
These two snakes, however, will not:
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]
[6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]
If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.

When the game ends, your program should print the result.

Throughout the gameplay, the snake will grow in length. If it gets too large, the interface might get ugly. To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, ..., for example, [3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4].

Objectives
Modify your Stage 2 code:

At the end of the game, print one of the following phrases:
Status: The game is over. You won!
Status: The game is over. The computer won!
Status: The game is over. It's a draw!

Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.

Add a game loop that will repeat the following steps until the game ends:

Display the current playing field (stage 2).

If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: Invalid input. Please try again..

If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.

Switch turns.

Keep in mind that at this stage we have no rules! Both the player and the computer can place their dominoes however they like.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

Typical gameplay.

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
> 4
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][4, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 5

[6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: It's your turn to make a move. Enter your command.
> -6
======================================================================
Stock size: 14
Computer pieces: 5

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
>
Example 2

Invalid input.

======================================================================
Stock size: 14
Computer pieces: 5

[4, 4][2, 3][3, 4]

Your pieces:
1:[1, 2]
2:[2, 6]
3:[0, 4]
4:[5, 6]
5:[2, 5]
6:[2, 4]

Status: It's your turn to make a move. Enter your command.
> Hello
Invalid input. Please try again.
>
Example 3

Mid-game example. The "domino snake" exceeds six dominoes in length.

======================================================================
Stock size: 7
Computer pieces: 4

[6, 6][6, 3][3, 0]...[4, 2][2, 3][3, 6]

Your pieces:
1:[0, 0]
2:[1, 2]
3:[5, 5]

Status: It's your turn to make a move. Enter your command.
Example 4

The player wins.

======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]

Your pieces:
1:[4, 4]

Status: It's your turn to make a move. Enter your command.
> 1
======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[0, 3][3, 4][4, 4]

Your pieces:

Status: The game is over. You won!

'''

import random

full_domino_set = [[i, j] for i in range(7) for j in range(i, 7)]
snakes = [x for x in full_domino_set if x[0] == x[1]]
stock_pieces = []
computer_pieces = []
player_pieces = []
game_snake = []
status = ''
game_in_play = True


def check_game_win():
    global game_in_play
    if len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        game_in_play = False
    elif len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        game_in_play = False
    elif is_draw(game_snake):
        print("Status: The game is over. It's a draw!")
        game_in_play = False


def deal_dominoes():
    current_set_of_dominoes = full_domino_set[:]
    stock_pieces.clear()
    computer_pieces.clear()
    player_pieces.clear()
    game_snake.clear()
    while current_set_of_dominoes:
        stock_pieces.append(current_set_of_dominoes.pop((random.randint(0, len(current_set_of_dominoes)-1))))
        computer_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))
        player_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))
        stock_pieces.append(current_set_of_dominoes.pop(random.randint(0, len(current_set_of_dominoes)-1)))


def first_play():
    global status
    status = ""
    for snake_piece in snakes[-1:0:-1]:
        if snake_piece in computer_pieces:
            game_snake.append(snake_piece)
            computer_pieces.remove(snake_piece)
            status = "player"
            return
        elif snake_piece in player_pieces:
            game_snake.append(snake_piece)
            player_pieces.remove(snake_piece)
            status = "computer"
            return
        else:
            continue


def is_draw(dominoes):
    flattened_dominoes = ""
    for domino in dominoes:
        flattened_dominoes += f'{domino[0]}{domino[1]}'
    if flattened_dominoes[0] == flattened_dominoes[-1]:
        if flattened_dominoes.count(flattened_dominoes[0]) == 8:
            return True


def play_game():
    global status
    print_game()
    check_game_win()
    if not game_in_play:
        return
    if status == 'computer':
        print(f"Status: Computer is about to make a move. Press Enter to continue...")
        play = random.randint(len(computer_pieces)*-1, len(computer_pieces))
        play_piece(play, computer_pieces)
        status = "player"
        input()
    else:
        while True:
            play = input("Status: It's your turn to make a move. Enter your command.")
            try:
                play = int(play)
                if len(player_pieces)*-1 > play or len(player_pieces) < play:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input. Please try again.")

        play_piece(play, player_pieces)
        status = "computer"


def play_piece(play, var):
    if play > 0:
        play -= 1
        game_snake.append(var[play])
        del var[play]
    elif play < 0:
        play = play * -1 - 1
        game_snake.insert(0, var[play])
        del var[play]
    else:
        var.append(stock_pieces.pop())


def print_game():
    print('=' * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")
    if len(game_snake) > 6:
        print(f'{game_snake[0]}{game_snake[1]}{game_snake[2]}...{game_snake[-3]}{game_snake[-2]}{game_snake[-1]}\n')
    else:
        return_string = ""
        for domino in game_snake:
            return_string += f'{domino}'
        print(f'{return_string}\n')
    print(f'Player pieces: ')
    count = 0
    for domino in player_pieces:
        count += 1
        print(f'{count}:{domino}')
    print()


if __name__ == '__main__':
    deal_dominoes()
    first_play()
    while game_in_play:
        play_game()
        
        
        
  \\

from collections import deque
from itertools import combinations_with_replacement
from random import shuffle, randint


class Error(Exception):
    """
    Base Error class for the dominoes.py module.
    """


class EmptyStockError(Error):
    """
    Raise when a player attempts to take a piece from the empty stock.
    """


class ActionError(Error):
    """
    Raise when the chosen action is out of range.
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
        no_move = False
        try:
            common_end = {*self.snake[0]}.intersection(self.snake[-1]).pop()
        except KeyError:
            pass
        else:
            if sum(common_end in tile for tile in self.snake) == 8:
                no_move = True
        return not self.player_pieces or not self.computer_pieces or no_move

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
                except (ActionError, EmptyStockError):
                    print(self.err_msg)

        else:
            while True:
                action = randint(-len(self.computer_pieces),
                                 len(self.computer_pieces))
                try:
                    self.move(action)
                except EmptyStockError:
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
        active_pieces = getattr(self, f'{self.status}_pieces')
        if action not in range(-len(active_pieces), len(active_pieces) + 1):
            raise ActionError

        if action == 0:
            try:
                active_pieces.append(self.stock_pieces.pop())
            except IndexError:
                raise EmptyStockError('No stock pieces left!')
        elif action > 0:
            self.snake.append(active_pieces.pop(action - 1))
        else:
            self.snake.appendleft(active_pieces.pop(abs(action) - 1))

        self.status = 'player' if self.status == 'computer' else 'computer'


def main():
    Domino().play()


if __name__ == '__main__':
    main()
    
    

\\


import random

status, full_stock, computer, player, stock, snake = '', [], [], [], [], []
condition = True

while condition:
    for i in range(7):
        for j in range(i, 7):
            full_stock.append([i, j])

    random.shuffle(full_stock)
    computer = full_stock[:7]
    player = full_stock[7:14]
    stock = full_stock[14:]
    snake = []

    for i in range(6, -1, -1):
        if [i, i] in computer:
            snake.append([i, i])
            computer.remove([i, i])
            status = 'player_turn'
            condition = False
            break
        elif [i, i] in player:
            snake.append([i, i])
            player.remove([i, i])
            status = 'computer_turn'
            condition = False
            break


def printing():
    print(70 * '=')
    print(f'Stock size: {len(stock)}', f'Computer pieces: {len(computer)}', '', sep='\n')
    if len(snake) > 6:
        print(snake[0], snake[1], snake[2], '...', snake[-3], snake[-2], snake[-1], sep='')
    else:
        for i in range(len(snake)):
            print(snake[i], end='')
    print('', '', 'Your pieces: ', sep='\n')
    for counter in range(len(player)):
        print(f"{counter + 1}:{player[counter]}")
    if status == 'player_turn':
        print('', "Status: It's your turn to make a move. Enter your command.", sep="\n")
    elif status == 'computer_turn':
        print('', f'Status: Computer is about to make a move. Press Enter to continue...', sep="\n")
    else:
        print(status)


printing()
while True:
    if status == 'computer_turn':
        input()
        move = random.choice(computer)
        computer.remove(move)
        snake.append(move)
        status = 'player_turn'
    elif status == 'player_turn':
        player_move = input()
        try:
            player[abs(int(player_move)) - 1]
        except:
            print("Invalid input. Please try again.")
            continue
        status = 'computer_turn'
        if int(player_move) == 0:
            player.append(stock[len(stock) - 1])
            stock.remove(stock[len(stock) - 1])
        elif int(player_move) > 0:
            snake.append(player[abs(int(player_move)) - 1])
        else:
            snake = [player[abs(int(player_move)) - 1]] + snake
        player.remove(player[abs(int(player_move)) - 1])
    else:
        exit()

    for i in range(7):
        count = 0
        for pair in snake:
            count += pair.count(i)
        if count == 8:
            status = "Status: The game is over. It's a draw!"
            break
    if len(player) == 0:
        status = 'Status: The game is over. You won!'
    elif len(computer) == 0:
        status = 'Status: The game is over. The computer won!'

    printing()
    
    
    
    
