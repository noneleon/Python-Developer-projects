'''
Description
Rock paper scissors is a popular hand game. Two players simultaneously form one of three shapes with their hands, and then, depending on the shapes, one player wins — rock beats scissors, paper wins over rock, scissors defeats paper.
The game is well-known for fair win-conditions between equal options.

Let's start with an unfair version! :)

Write a program that reads input that states which option users have chosen. After this, your program must make users lose! That is, your program should always choose an option that defeats the one picked by users. Once it finds this option, output the line Sorry, but the computer chose <option>, where <option> is the name of the option that the program's picked depending on the user's input.
For example, if users enter rock, the program should print Sorry, but the computer chose paper and so on.

Please, pay attention to the format of the output. It should follow the one in the example, including capital letters and punctuation. Do not print additional strings!

Objectives
Your program should:

Take input from the user;
Find an option that wins over the user's option;
Output the line: Sorry, but the computer chose <option>.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> scissors
Sorry, but the computer chose rock
Example 2:

> paper
Sorry, but the computer chose scissors
'''

# Write your code here
a = input()
if a == 'scissors':
    print('Sorry, but the computer chose rock')
elif a == 'paper':
    print('Sorry, but the computer chose scissors')
else:
    print('Sorry, but the computer chose paper')
    
    
\\
move = input()
response = "Sorry, but the computer chose"
if move == "scissors":
    print(response, "rock")
elif move == "rock":
    print(response, "paper")
else:
    print(response, "scissors")
