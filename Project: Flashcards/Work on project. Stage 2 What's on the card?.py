'''
Description
Of course, we cannot use flashcards with only one hardcoded card. So let's make our program more dynamic! Let’s create flashcards depending on the user's input and add a primitive guessing mechanism so that the user can check how well they remember the definitions.

In this stage, you need to implement a custom flashcard-creation mechanism which will be extensively used in further steps, and add a mechanism to check the user's answer.

Objectives
Your program should read two lines from the console, a term, and a definition, that represent a card.

After that, the user inputs a line as an answer (a definition of the term on the card). Compare the user's answer with the correct definition and print the result.

The output of the program must contain one of two words:

wrong if the answer doesn't match the definition;
right if the answer matches the definition.
Of course, at this point, the user is unlikely to get the answer wrong, since they’re the ones who just typed in the answer... But don’t worry: right now we're just warming up so that in later stages we could make this a bit more challenging for our users.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: the user's answer is correct

Input (a term, a definition, an answer):

> print()
> outputs text
> outputs text
Output:

Your answer is right!
Example 2: the user's answer is incorrect

Input (a term, a definition, an answer):

> Jetbrains
> A place for people who love to code
> A place for people who hate to code
Output:

Your answer is wrong...

'''
# Write your code her
a = input()
b = input()
c = input()
if b == c:
    print('Your answer is right!')
else:
    print('Your answer is wrong...')

\\

check = [input() for _ in range(3)]
print("Your answer is right!" if check[2] == check[1] else "Your answer is wrong...")

\\
# Write your code here
card = input()
definition = input()
answer = input()
print(f'Your answer is {"right" if answer == definition else "wrong"}!')

