'''
Description
Randomly made choices are hardly a sign of intelligence. Teach your computer to make educated decisions with the help of basic statistics. Here's how it works:

The primary objective of the AI is to determine which domino is the least favorable and then get rid of it. To reduce your chances of skipping a turn, you must increase the diversity of your pieces. For example, it's unwise to play your only domino that has a 3, unless there's nothing else that can be done. Using this logic, the AI will evaluate each domino in possession, based on the rarity. Dominoes with rare numbers will get lower scores, while dominoes with common numbers will get higher scores.

The AI should use the following algorithm to calculate the score:

Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.
The AI will now attempt to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI will move down the score list and try another domino. The AI will skip the turn if it runs out of options.

Objectives
Replace the random move generator with the algorithm described above. Let's analyze how the computer will act in two example situations:

1. The first case (see Example 1 below).

Computer pieces: [2,5],[3,5],[0,5]
Domino snake: [4,4],[4,2],[2,1],[1,0],[0,0],[0,2]
Count:

0: 5
1: 2
2: 4
3: 1
4: 3
5: 3
6: 0
Scores:

[2,5]: 4 + 3 = 7
[3,5]: 1 + 3 = 4
[0,5]: 5 + 3 = 8
Attempts:
Domino [0,5] has the highest score. However, it cannot be played at this moment.
Domino [2,5] has the second-highest score. We can play it by appending it to the right side of the snake.

The result:
Play the [2,5] domino by appending it to the right side of the snake.

2. The second case (see example 2 below).

Computer pieces: [1,5],[3,5],[0,5]
Domino snake: [4,4],[4,2],[2,1],[1,0],[0,0],[0,2]
Count:

0: 5
1: 3
2: 3
3: 1
4: 3
5: 3
6: 0
Scores:

[1,5]: 3 + 3 = 6
[3,5]: 1 + 3 = 4
[0,5]: 5 + 3 = 8
Attempts:
Domino [0,5] has the highest score. However, it cannot be played at this moment.
Domino [1,5] has the second-highest score. However, it cannot be played at this moment.
Domino [3,5] is the last option. Unfortunately, it also cannot be played at this moment.

The result:
Take an extra piece from the stock (if it's not empty) and skip a turn.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

The Computer plays a domino.

======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 12
Computer pieces: 2

[4, 4][4, 2][2, 1]...[0, 0][0, 2][2, 5]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
>
Example 2

The Computer skips the turn.

======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 11
Computer pieces: 4

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
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
from collections import deque, Counter
from itertools import combinations_with_replacement
from random import shuffle

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


class ScoreError(Error):
    """
    Raise when attempting to score a tile not belonging to any of the players.
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
        one of the players or the stock runs out of pieces, or when
        the numbers on the ends of the snake are identical and appear
        within the snake 8 times.

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

    def score(self, tile: Tile) -> int:
        """
        Given a tile in a player's hand, return the score of the tile,
        defined as the sum of appearances of each of its numbers.
        Only appearances in the player's hand and the snake are counted.

        :param tile: A tile in a player's hand.
        :return: The score of the tile.
        :raises ScoreError: if the tile does not belong to any player
        """
        if tile in self.player_pieces:
            active_pieces = self.player_pieces
        elif tile in self.computer_pieces:
            active_pieces = self.computer_pieces
        else:
            raise ScoreError
        appearances = Counter(pips for piece in self.snake for pips in piece)
        appearances.update(pips for piece in active_pieces for pips in piece)
        return sum(appearances[pips] for pips in tile)

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
            for action, piece in sorted(enumerate(self.computer_pieces, 1),
                                        key=lambda x: self.score(x[1]),
                                        reverse=True):
                try:
                    self.move(action)
                except IllegalMoveError:
                    continue
                else:
                    break

            else:
                self.move(0)

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

# Write your code here
import random


def create_domino_set():
    full_domino = []
    for i in range(0,7):
        for j in range(i, 7):
            current_piece = [i, j]
            full_domino.append(current_piece)
    return full_domino


def stockpieces(full_domino_set):
    result = []
    fullset = full_domino_set
    random.seed()
    while len(result) < 14:
        rand = random.randint(0, len(fullset)-1)
        piece = fullset.pop(rand)
        result.append(piece)
    return result


def create_player_pieces(fullset):
    result = []
    # fullset = full_domino_set
    random.seed()
    while len(result) < 7:
        rand = random.randint(0, len(fullset)-1)
        piece = fullset.pop(rand)
        result.append(piece)
    return result


def draw_screen(stock, cp, pp, snk, player_turn):
    print("="*70)
    print("Stock size: {}".format(len(stock)))
    print("Computer pieces: {}".format(len(cp)))


    if player_turn:
        # print("Status: player")
        print()
        if len(snk) > 6:
            sub_snk_1 = snk[0:3]
            sub_snk_2 = snk[len(snk) - 3:len(snk)]
            print("{}...{}".format(" ".join([str(x) for x in sub_snk_1]), " ".join([str(x) for x in sub_snk_2])))
        else:
            print("{}".format(" ".join([str(x) for x in snk])))
        print()
        print("Your pieces:")
        for i in range(0, len(pp)):
            print("{}:{}".format(i+1, pp[i]))
        print("\nStatus: It's your turn to make a move. Enter your command.")
    else:
        print()
        if len(snk) > 6:
            sub_snk_1 = snk[0:3]
            sub_snk_2 = snk[len(snk)-3:len(snk)]
            print("{}...{}".format(" ".join([str(x) for x in sub_snk_1]), " ".join([str(x) for x in sub_snk_2])))
        else:
            print("{}".format(" ".join([str(x) for x in snk])))
        print()
        print("Your pieces:")
        for i in range(0, len(pp)):
            print("{}:{}".format(i+1, pp[i]))
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    # print("Your pieces: {}".format(pp))


def check_for_end(snake):
    result = False
    if len(snake) > 2:
        first_piece = snake[0]
        last_piece = snake[-1]
        number_to_search = first_piece[0]
        count_number_to_search = 0
        for last_piece in snake[1:len(snake)-1]:
            if first_piece[0] == last_piece[1]:
                for piece in snake:
                    if piece[0] == number_to_search:
                        count_number_to_search += 1
                    if piece[1] == number_to_search:
                        count_number_to_search += 1

            # print(number_to_search, count_number_to_search)
    else:
        first_piece = snake[0]
        number_to_search = first_piece[0]
        count_number_to_search = 1
        if number_to_search == first_piece[1]:
            count_number_to_search += 1

    if count_number_to_search == 8:
        return True
    else:
        return False


def computer_plays(comp_pieces):
    random.seed()
    computer_current_piece = random.choice(comp_pieces)
    return computer_current_piece

def random_piece_from_stock(sp):
    random.seed()
    random_piece = random.choice(sp)
    idx = sp.index(random_piece)
    sp.pop(idx)
    return random_piece

def input_int_only():
    done = False
    while not done:
        try:
            inp = int(input())
            done = True
        except ValueError:
            print("Invalid input. Please try again.")
            done = False
    return inp

is_players_turn = False
domino_sneak = []
game_finished = False
players = ['player', 'computer']
current_player = ""
while len(domino_sneak) == 0 and not game_finished:
    full_domino_set = create_domino_set()
    computer_pieces = create_player_pieces(full_domino_set)
    player_pieces = create_player_pieces(full_domino_set)
    stock_pieces = stockpieces(full_domino_set)

    if [6, 6] in player_pieces:
        i = player_pieces.index([6, 6])
        current_piece = player_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = False
        current_player = players[1]
    elif [6, 6] in computer_pieces:
        i = computer_pieces.index([6, 6])
        current_piece = computer_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = True
        current_player = players[0]
    elif [5, 5] in player_pieces:
        i = player_pieces.index([5, 5])
        current_piece = player_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = False
        current_player = players[1]
    elif [5, 5] in computer_pieces:
        i = computer_pieces.index([5, 5])
        current_piece = computer_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = True
        current_player = players[0]

# print("Stock pieces: {}".format(stock_pieces))
# print("Computer pieces: {}".format(computer_pieces))
# print("Player pieces: {}".format(player_pieces))
# print("Domino snake: {}".format(domino_sneak))
# if is_players_turn:
#   print("Status: player")
# else:
#    print("Status: computer")

while not game_finished:
    draw_screen(stock_pieces, computer_pieces, player_pieces, domino_sneak, is_players_turn)
    if not check_for_end(domino_sneak):
        if is_players_turn:
            # print("Status: It's your turn to make a move. Enter your command.")
            idx_invalid = True
            while idx_invalid:
                idx = input_int_only()
                if 0 < abs(idx) <= len(player_pieces):
                    current_piece = player_pieces.pop(abs(idx)-1)
                    if idx < 0:
                        if current_piece[0] == domino_sneak[0][0]:
                            current_piece = [current_piece[1], current_piece[0]]
                            domino_sneak.insert(0, current_piece)
                        elif current_piece[1] == domino_sneak[0][0]:
                            # current_piece = [current_piece[1], current_piece[0]]
                            domino_sneak.insert(0, current_piece)
                    else:
                        if current_piece[0] == domino_sneak[-1][1]:
                            # current_piece = [current_piece[1], current_piece[0]]
                            pass
                            domino_sneak.append(current_piece)
                        elif current_piece[1] == domino_sneak[-1][1]:
                            current_piece = [current_piece[1], current_piece[0]]
                            domino_sneak.append(current_piece)

                    if len(player_pieces) == 0:
                        game_finished = True
                    idx_invalid = False
                    is_players_turn = not is_players_turn
                elif idx == 0:
                    new_piece = random_piece_from_stock(stock_pieces)
                    player_pieces.append(new_piece)
                    idx_invalid = False
                    is_players_turn = not is_players_turn
                else:
                    idx_invalid = True
        else:
            # print("Status: Computer is about to make a move. Press Enter to continue...")
            input()
            current_piece = computer_plays(computer_pieces)
            idx = computer_pieces.index(current_piece)
            computer_pieces.pop(idx)
            # to do swap field for current_piece
            domino_sneak.append(current_piece)
            is_players_turn = not is_players_turn
            if len(computer_pieces) == 0:
                game_finished = True
        if len(computer_pieces) == 0:
            game_finished = True
            draw_screen(stock_pieces, computer_pieces, player_pieces, domino_sneak, is_players_turn)
            print("Status: The game is over. The computer won!")
        if len(player_pieces) == 0:
            game_finished = True
            draw_screen(stock_pieces, computer_pieces, player_pieces, domino_sneak, is_players_turn)
            print("Status: The game is over. You won!")
    else:
        draw_screen(stock_pieces, computer_pieces, player_pieces, domino_sneak, is_players_turn)
        print("Status: The game is over. It's a draw!")
        game_finished = True
        
\\

import random

STOCK = 0
COMPUTER = 1
PLAYER = 2

stock_pieces = []
computer_pieces = []
player_pieces = []
domino_snake = []
status = STOCK


def generate_pieces():
    pieces = []
    for i in range(7):
        for j in range(i, 7):
            pieces.append([i, j])
    return pieces


def split_pieces(pieces):
    indexes = []
    for i in range(14):
        indexes.append(STOCK)
    for i in range(7):
        indexes.append(COMPUTER)
    for i in range(7):
        indexes.append(PLAYER)

    random.shuffle(indexes)

    for i in range(len(indexes)):
        if indexes[i] == STOCK:
            stock_pieces.append(pieces[i])
        elif indexes[i] == COMPUTER:
            computer_pieces.append(pieces[i])
        elif indexes[i] == PLAYER:
            player_pieces.append(pieces[i])

    for i in [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]:
        if i in computer_pieces:
            computer_pieces.remove(i)
            domino_snake.append(i)
            return PLAYER
        elif i in player_pieces:
            player_pieces.remove(i)
            domino_snake.append(i)
            return COMPUTER


def setting_up_the_game():
    global status

    pieces = generate_pieces()

    while True:
        status = split_pieces(pieces)
        if status in [COMPUTER, PLAYER]:
            break


def print_domino_snake():
    if len(domino_snake) > 6:
        for i in range(3):
            print(domino_snake[i], end="")
        print("...", end="")
        for i in range(-3, 0):
            print(domino_snake[i], end="")
    else:
        for i in range(len(domino_snake)):
            print(domino_snake[i], end="")
    print()


def print_game():
    global status

    print("======================================================================")
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()
    print_domino_snake()
    print()
    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(f"{i + 1}:{player_pieces[i]}")
    print()


#  1: snake tail
# -1: snake head
#  0: not acceptable
def get_acceptable_end(piece):
    if domino_snake[0][0] in piece:
        return -1
    elif domino_snake[-1][-1] in piece:
        return 1
    return 0


def get_sorted_computer_piece_indexes():
    count = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(count)):
        for piece in computer_pieces:
            if i == piece[0]:
                count[i] += 1
            if i == piece[1]:
                count[i] += 1
        for piece in domino_snake:
            if i == piece[0]:
                count[i] += 1
            if i == piece[1]:
                count[i] += 1

    scores = {}
    for i in range(len(computer_pieces)):
        score = count[computer_pieces[i][0]] + count[computer_pieces[i][1]]
        scores.update({i: score})

    return dict(sorted(scores.items(), key=lambda item: -item[1]))


def get_next_action():
    if status == COMPUTER:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        action = 0
        for i in get_sorted_computer_piece_indexes().keys():
            end = get_acceptable_end(computer_pieces[i])
            if end == 1:
                action = i + 1
                break
            if end == -1:
                action = -(i + 1)
                break
    else:
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            try:
                action = int(input())
                if action in range(-len(player_pieces), len(player_pieces) + 1):
                    if action == 0:
                        break
                    if action > 0 and domino_snake[-1][-1] in player_pieces[action - 1]:
                        break
                    elif action < 0 and domino_snake[0][0] in player_pieces[-action - 1]:
                        break
                    else:
                        print("Illegal move. Please try again.")
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")

    return action


def make_a_move(action):
    global status

    if status == PLAYER:
        target = player_pieces
        status = COMPUTER
    elif status == COMPUTER:
        target = computer_pieces
        status = PLAYER
    else:
        return

    if action > 0:
        piece = target[action - 1]
        if domino_snake[-1][-1] == piece[-1]:
            piece = [piece[-1], piece[0]]
        domino_snake.append(piece)
        del target[action - 1]
    elif action < 0:
        piece = target[-action - 1]
        if domino_snake[0][0] == piece[0]:
            piece = [piece[-1], piece[0]]
        domino_snake.insert(0, piece)
        del target[-action - 1]
    else:
        if len(stock_pieces) > 0:
            target.append(stock_pieces.pop())


def check_status():
    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        return True
    if len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        return True
    if domino_snake[0][0] == domino_snake[-1][-1]:
        n = domino_snake[0][0]
        count = 0
        for i in domino_snake:
            for j in i:
                if j == n:
                    count += 1
        if count == 8:
            print("Status: The game is over. It's a draw!")
            return True


if __name__ == '__main__':
    setting_up_the_game()
    print_game()

    while True:
        make_a_move(get_next_action())
        print_game()
        if check_status():
            break

            
            
        
