'''
Theory
Note:
Before you start this project, it's better to get familiar with the basic domino rules. Keep in mind that there are many versions of the game. The rules used in this particular project will be described as we go along.

As you might know, a domino is a playing piece that is characterized by the two numbers written on it. The numbers are integers and can range from 0 to 6. A single domino piece has no orientation, so, a full domino set (that includes all the possible pairs of numbers) will have 28 unique dominoes.

You may think that there should be 7*7=49 dominoes in total. However, this is not the case because the combinations like [1,2] and [2,1] are the same domino, not two separate ones.

Description
To play domino, you need a full domino set and at least two players. In this project, the game is played by you and the computer.

At the beginning of the game, each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces).

To start the game, players determine the starting piece. The player with the highest domino or the highest double ([6,6] or [5,5] for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed.

Status is the player, who is to make the next move
Objectives
Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer".
Stock pieces      # 14 domino elements
Computer pieces   # 7 or 6 domino elements
Player pieces     # 6 or 7 domino elements
Domino snake      # 1 starting domino
Status            # the player that goes first
If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
Output all five variables.
Examples
Example 1

The player makes the first move.

Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
Domino snake: [[6, 6]]
Status: player

Example 2

The computer makes the first move.

Stock pieces: [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3]]
Computer pieces: [[0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5]]
player pieces: [[1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4]]
Domino snake: [[5, 5]]
Status: computer
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

print("Stock pieces:", stock)
print("Computer pieces:", computer)
print("Player pieces:", player)
print("Domino snake:", [snake])
print("status:", status)

\\

# Write your code here
import random

#Generate list of dominoes
def generate_domino_set():
    global domino_set
    domino_set = []
    for i in range(7):    
        for j in range(7):
            domino_piece = [] 
            domino_alt_piece = [] 
            domino_piece.append(i)
            domino_piece.append(j)
            domino_alt_piece.append(j)
            domino_alt_piece.append(i)
            if domino_alt_piece not in domino_set:
                domino_set.append(domino_piece)

def split_set():
    global domino_set
    global player_pieces
    global computer_pieces
    global stock_pieces
    
    player_pieces = []
    computer_pieces = []    
    stock_pieces = domino_set.copy()
    
    for i in range(7):
        player_pieces.append(stock_pieces.pop())
        computer_pieces.append(stock_pieces.pop())
            
def determine_starting_player():
    global status
    global domino_snake
    domino_snake = []
    status = "none"
    
    for i in range(6, 0, -1):
        domino_piece = [i,i]
        if domino_piece in player_pieces:
            status = "computer"
            player_pieces.remove(domino_piece)
            domino_snake.append(domino_piece)
            break
        elif domino_piece in computer_pieces:
            status = "player"              
            computer_pieces.remove(domino_piece) 
            domino_snake.append(domino_piece)      
            break


status = "none"
generate_domino_set()
#print(domino_set)
while status == "none":
    random.shuffle(domino_set)
    split_set()
    determine_starting_player()

#print("Domino_Set: ", domino_set)
print("Stock pieces:", stock_pieces)
print("Computer pieces:", computer_pieces)
print("player pieces:", player_pieces)
print("Domino snake:", domino_snake)
print("Status:", status)

