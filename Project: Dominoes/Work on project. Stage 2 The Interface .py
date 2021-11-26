'''
Description
A good game needs a good interface. In this stage, you will make your output user-friendly.

The player should be able to see the domino snake, the so-called playing field, and their own pieces. It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.

Two things must remain hidden from the player: the stock pieces and the computer's pieces. The player should not be able to see them, only the number of pieces remaining.

Objectives
Print the header using seventy equal sign characters (=).
Print the number of dominoes remaining in the stock – Stock size: [number].
Print the number of dominoes the computer has – Computer pieces: [number].
Print the domino snake. At this stage, it consists of the only starting piece.
Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
Print the status of the game:
If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
If status = "player", print "Status: It's your turn to make a move. Enter your command."
Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.
Examples
Example 1

The player makes the first move (status = "player")

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

Example 2

The Computer makes the first move (status = "computer")

======================================================================
Stock size: 14
Computer pieces: 7

[5, 5]

Your pieces:
1:[1, 3]
2:[1, 4]
3:[4, 5]
4:[1, 6]
5:[1, 1]
6:[0, 4]

Status: Computer is about to make a move. Press Enter to continue...
'''
import random
dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
random.shuffle(dominoes)
stock = dominoes[:14]
computer = dominoes[14:21]
player = dominoes[21:]

snake = max(max(computer), max(player))

if snake in computer:
    computer.remove(snake)
    status = 'player'
else:
    player.remove(snake)
    status = 'computer'

print('=' * 70)
print("Stock size:", len(stock))
print("Computer pieces:", len(computer))
print()
print(snake)
print()
print("Your pieces:")
for i in range(len(player)):
    n = i + 1
    pieces = player[i]
    print("{}:{}".format(n,pieces))

if status == 'player':
    print()
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print()
    print("Status: Computer is about to make a move. Press Enter to continue...")
    
    
import random


def return_domino_set():
    nums = []
    possible_pairs = set()
    for n in range(0, 7):
        for m in range(0, 7):
            if m not in nums:
                possible_pairs.add((n, m))
        nums.append(n)
    return possible_pairs


def get_stock(domino):
    return set(tuple(n) for n in random.sample(list(domino), 14))


def get_computer(pairs):
    return set(tuple(n) for n in random.sample(list(pairs), 7))


def get_domino_snake(pairs):
    return max(pair for pair in pairs if pair[0] == pair[1])


def check_status(computer_pairs, player_pairs, snake_pair):
    if snake_pair in computer_pairs:
        computer_pairs.remove(snake_pair)
        return 'player'
    player_pairs.remove(snake_pair)
    return 'computer'


def get_player_pairs(player_pairs):
    for i, pair in enumerate(player_pairs, start=1):
        print(f'{i}:{list(pair)}')


messages = dict(
    player="It's your turn to make a move. Enter your command.",
    computer="Computer is about to make a move. Press Enter to continue..."
)

domino_pairs = return_domino_set()
stock_pairs = get_stock(domino_pairs)
computer = get_computer(domino_pairs - stock_pairs)
player = domino_pairs - stock_pairs - computer
snake = get_domino_snake(computer.union(player))
status = check_status(computer, player, snake)

print('=' * 70)
print('Stock size:', len(stock_pairs))
print('Computer pieces:', len(computer))

print(list(snake))

get_player_pairs(player)
print('Status:', messages.get(status))


\\



