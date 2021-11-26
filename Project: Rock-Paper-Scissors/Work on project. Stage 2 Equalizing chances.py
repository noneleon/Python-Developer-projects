'''
Description
Well, now let's do something more tangible. Nobody wants to play the game where you always lose. We can use the power of the random module to make a truly challenging game.

Write a program that reads input from users, chooses a random option, and then says who won: the user or the computer.
There are a few examples below to provide the output for any outcome (<option> is the option chosen by your program):

Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed
Objectives
Your program should:

Read user's input that includes the option that users have chosen;
Choose a random option;
Compare the options and determine the winner;
Output one of the lines above, depending on the result of the game.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> rock
Well done. The computer chose scissors and failed
Example 2:

> scissors
There is a draw (scissors)
Example 3:

> paper
Sorry, but the computer chose scissors
'''

# Write your code here
import random
b = list(["scissors", "rock", "paper"])
user_pick = input()
computer_pick = random.choice(b)
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


def users_choice():
    user_choice =  input()
    return user_choice


def comp_choice():
    pc_choice = random.choice(('rock', 'paper', 'scissors'))
    return pc_choice


def who_is_the_winner(human, comp):
    lose_conditions = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    if lose_conditions[human] == comp:
        return lose(comp)
    elif human == comp:
        return draw(comp)
    else:
        return win(comp)


def lose(x):
    return f'Sorry, but the computer chose {x}'


def draw(x):
    return f'There is a draw ({x})'


def win(x):
    return f'Well done. The computer chose {x} and failed'


def main():
    human = users_choice()
    comp = comp_choice()
    print(who_is_the_winner(human, comp))


if __name__ == "__main__":
    main()
    
    
\\

import random
random.seed()

winners = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

computer = random.choice(list(winners.keys()))
human = input()

if computer == human:
    print(f"There is a draw (${computer})")
elif computer == winners[human]:
    print(f"Well done. The computer chose ${computer} and failed")
else:
    print(f"Sorry, but the computer chose ${computer}")
