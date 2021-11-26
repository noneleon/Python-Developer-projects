'''
Description
Keep improving your bot by developing new skills for it. We suggest a simple guessing game that will predict the age of a user.

It's based on a simple math trick. First, take a look at this formula:

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
The numbersremainder3, remainder5 and remainder7 are the remainders of division by 3, 5 and 7 respectively.

It turns out that for each number ranging from 0 to 104 the calculation will result in the number itself. This perfectly fits the ordinary age range, doesn't it? Ask a user for the remainders and use them to guess the age!

Objective
At this stage, you will introduce yourself to the bot. It will greet you by your name and then try to guess your age using arithmetic operations.

Your program should print the following lines:

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
Your age is {your_age}; that's a good time to start programming!
Read three numbers from the standard input. Assume that all the numbers will be given on separate lines.

Instead of {your_age}, the bot will print the age determined according to the special formula discussed above.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: a dialogue with the bot

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
> Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
> 1
> 2
> 1
Your age is 22; that's a good time to start programming!
Use the provided template to simplify your work. You can change the text, but not the number of printed lines.
'''
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print(f'What a great name you have, {name}!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders

remainder3 = int(input())
remainder5= int(input())
remainder7= int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f'Your age is {your_age}; that\'s a good time to start programming!')


