'''
Description
People love to see their results as they're running to their goal.
So, let's learn how to show the user the score of the game.

When the game starts, the user should enter his/her name. After that, the program should greet the user and read a file namedrating.txt . This is a file containing current scores for different players. You can see the file format below: it's just lines containing user's name and his/her score divided by a single space.

Tim 350
Jane 200
Alex 400
If there’s a record for the user with the same name in the file, the program should take his/her rating and use it as a reference point for counting current user’s score (for example, if the user entered name Tim, then his score at the start of the game will be 350). If the user's name isn't written in the file, then your program should count user's score from 0.

You don't need to write anything in the rating.txt file!

The program should print user's score when the user enters !rating. For example, if your rating is 0 then the program should print:

Your rating: 0
Your program should add 50 points to the player for every draw, 100 for every win, and nothing for losing.

Objectives
Your program should:

Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
Read input specifying the user's name and output a new line Hello, <name>
Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
Play the game by the rules defined on the previous stages:
Read user's input
If the input is !exit, output Bye! and stop the game
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed
For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
If the input corresponds to anything else, output Invalid input
Play the game again
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

Enter your name: > Tim
Hello, Tim
> !rating
Your rating: 350
> rock
Sorry, but the computer chose paper
> paper
Well done. The computer chose rock and failed
> scissors
There is a draw (scissors)
> !rating
Your rating: 500
> !exit
Bye!
Example 2

Enter your name: > Chuck
Hello, Chuck
> scissors
There is a draw (scissors)
> rock
Well done. The computer chose scissors and failed
> paper
Well done. The computer chose rock and failed
> !rating
Your rating: 250
> !exit
Bye!

'''
import random

plays = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

player_name = input("Enter your name:")
player_score = 0
print(f'Hello, {player_name}')

ratings = open('rating.txt', 'r')
for line in ratings:
    if line.startswith(f'{player_name} '):
        player_score = int(line.strip(f'{player_name} '))
ratings.close()

while True:
    user_plays = input()
    if user_plays == "!exit":
        print('Bye!')
        break
    elif user_plays == '!rating':
        print(f'Your rating: {player_score}')
        continue
    elif user_plays not in list(plays):
        print('Invalid input')
        continue
    computer_plays = random.choice(list(plays))

    if plays[user_plays] == computer_plays:
        print(f'Well done. The computer chose {computer_plays} and failed')
        player_score += 100
    elif plays[computer_plays] == user_plays:
        print(f'Sorry, but the computer chose {computer_plays}')
    else:
        print(f'There is a draw ({computer_plays})')
        player_score += 50
        
\\

import random

plays = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

player_name = input("Enter your name:")
player_score = 0
print(f'Hello, {player_name}')

ratings = open('rating.txt', 'r')
for line in ratings:
    if line.startswith(f'{player_name} '):
        player_score = int(line.strip(f'{player_name} '))
ratings.close()

while True:
    user_plays = input()
    if user_plays == "!exit":
        print('Bye!')
        break
    elif user_plays == '!rating':
        print(f'Your rating: {player_score}')
        continue
    elif user_plays not in list(plays):
        print('Invalid input')
        continue
    computer_plays = random.choice(list(plays))

    if plays[user_plays] == computer_plays:
        print(f'Well done. The computer chose {computer_plays} and failed')
        player_score += 100
    elif plays[computer_plays] == user_plays:
        print(f'Sorry, but the computer chose {computer_plays}')
    else:
        print(f'There is a draw ({computer_plays})')
        player_score += 50
        
        
\\
import random

name = input("Enter your name: ")   # user enters his/her name
print(f"Hello, {name}")

rating = 0
file = open("rating.txt", "r")
for line in file:
    score = line.rstrip().split()
    if name in line:
        rating += int(score[1])
        break

option = ["rock", "paper", "scissors"]

while True:
    user_input = input().lower()
    computer_option = random.choice(option)
    if user_input == "!rating":
        print(f"Your rating: {rating}")
        continue
    elif user_input == "!exit":
        break
    elif user_input in option:
        if user_input == computer_option:
            print(f"There is a draw ({computer_option})")
            rating += 50
        elif (user_input == "rock" and computer_option == "scissors") or \
                (user_input == "paper" and computer_option == "rock") or \
                (user_input == "scissors" and computer_option == "paper"):
            print(f"Well done. The computer chose {computer_option} and failed")
            rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_option}")
            rating += 0
    else:
        print("Invalid input")
print("Bye!")



