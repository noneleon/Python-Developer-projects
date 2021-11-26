'''
Description
Hangman is a popular yet grim intellectual game. A cruel computer hides a word from you. Letter by letter you try to guess it. If you fail, you'll be hanged, if you win, you'll survive. See also: Wikipedia

You probably played the game at least once in your life; now you can actually create this game yourself!

Let's look at a brief overview of what you are going to build in this project. Here is what the gameplay should look like:

In the main menu, a player can choose to either play or exit the game.
If the user chooses to play, the computer picks a word from a list: this will be the answer to the puzzle.
The computer asks the player to enter a letter that they think is in the word.
If that letter does not appear in the word and this letter hasn't already been guessed, the computer counts it as a miss. A player can only afford 8 misses before the game is over.
If the letter does occur in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to go on.
When the entire word is uncovered, it's a victory! The game calculates the final score and returns to the main menu.
This may sound complex, but the project is split into small stages with hints to see you through. The final product is sure to be replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print something using Python. Try to apply that knowledge to entice your friends to play with an announcement for your game!

Objectives
In this stage, you should write a program that prints the lines shown in the example below.

Example
Output:

H A N G M A N
The game will be available soon.

'''

# Write your code here
print("""
H A N G M A N
The game will be available soon.
""")
