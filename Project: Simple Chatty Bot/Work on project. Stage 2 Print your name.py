'''
Description
The greeting part is great, but chatbots are also supposed to interact with a user. It's time to implement this functionality.

Objective
At this stage, you will introduce yourself to the bot so that it can greet you by your name.

Your program should print the following lines:

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
What a great name you have, {your_name}!
You may change the name and the creation year of your bot if you want.

Instead of {your_name}, the bot must print your name entered from the standard input.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: a dialogue with the bot

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Use the provided template to simplify your work. You can change the text, but not the number of printed lines.

'''


print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders

print("Your age is {your_age}; that's a good time to start programming!")
