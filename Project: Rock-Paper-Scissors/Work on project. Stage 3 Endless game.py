'''Description
We came up with a really cool idea in the previous stage. But the game is really short so far. Nobody plays a single shot of rock paper scissors. We need to make the game run forever. Not literally, though — let's implement a way to stop your program.

Improve your program so that it will take an unlimited number of inputs until users enter !exit. After entering !exit, the program should print Bye! and terminate. Also, let's try to handle invalid inputs: your program should be ready to handle typos in user input, or when there's a mishmash instead of a normal command. So, if the input doesn't correspond to any known command (an option or !exit), your program should output the following line: Invalid input.

Objectives
Your program should:

Take input from users;
If the input contains !exit, output Bye! and stop the game;
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed
If the input corresponds to anything else, output Invalid input;
Repeat it all over again.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> rock
Well done. The computer chose scissors and failed
> paper
Well done. The computer chose rock and failed
> paper
There is a draw (paper)
> scissors
Sorry, but the computer chose rock
> rokc
Invalid input
> xit!
Invalid input
> !exit
Bye!'''

# Write your code here
import random
b = list(["scissors", "rock", "paper"])
while True:
    user_pick = input()
    computer_pick = random.choice(b)
    if user_pick not in ["scissors", "rock", "paper","!exit"]:
        print('Invalid input')
    elif user_pick == '!exit':
        print('Bye!')
        break
    else:
        if user_pick == computer_pick:  # tie
            print(f"There is a draw ({computer_pick})")

        elif user_pick=="scissors" and computer_pick == "paper" :
            print(f"Well done. Computer chose {computer_pick} and failed") 
        elif user_pick=="paper" and computer_pick == "rock" :
            print(f"Well done. Computer chose {computer_pick} and failed")  
        elif user_pick=="rock" and computer_pick == "scissors" :
            print(f"Well done. Computer chose {computer_pick} and failed") # you win
        else:
            print(f"Sorry, but computer chose {computer_pick}")  # you lose
    
    
\\

import random


class Game:
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    USER_WIN = 'User'
    COMPUTER_WIN = 'Computer'
    QUIT = '!exit'


def find_winner(user_choice, computer_choice):
    win_beat_pairs = {Game.ROCK: Game.SCISSORS,
                      Game.PAPER: Game.ROCK,
                      Game.SCISSORS: Game.PAPER}
    if win_beat_pairs[user_choice] == computer_choice:
        return Game.USER_WIN
    else:
        return Game.COMPUTER_WIN


messages = {
    'lose': 'Sorry, but the computer chose {option}',
    'draw': 'There is a draw ({option})',
    'win': 'Well done. The computer chose {option} and failed',
    'invalid': 'Invalid input',
    'quit': 'Bye!',
}

# rock > scissors
# paper > rock
# scissors > paper
hand_shapes = [Game.ROCK, Game.PAPER, Game.SCISSORS]

while True:
    # Choose random computer shape
    computer_input = random.choice(hand_shapes)

    # Take user input
    user_input = input()

    # Test user input for value
    if user_input == Game.QUIT:
        print(messages['quit'])
        break
    if user_input not in hand_shapes:
        print(messages['invalid'])
        continue

    # Handle draw
    if user_input == computer_input:
        print(messages['draw'].format(option=computer_input))
        continue

    # Handle the rest of cases
    winner = find_winner(user_input, computer_input)

    if winner == Game.USER_WIN:
        print(messages['win'].format(option=computer_input))
        continue
    elif winner == Game.COMPUTER_WIN:
        print(messages['lose'].format(option=computer_input))
        continue

        
\\

import random

plays = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

while True:
    user_plays = input()
    if user_plays == "!exit":
        print('Bye!')
        break
    elif user_plays not in list(plays):
        print('Invalid input')
        continue
    computer_plays = random.choice(list(plays))
    
    if plays[user_plays] == computer_plays:
        print(f'Well done. The computer chose {computer_plays} and failed')
    elif plays[computer_plays] == user_plays:
        print(f'Sorry, but the computer chose {computer_plays}')
    else:
        print(f'There is a draw ({computer_plays})')
