'''
Description
If there is a predefined word, the game isn't replayable. You already know the word, so there’s no longer any challenge. At this stage, let's make the game more challenging by choosing a word from a special list with a variety of options. This way, our game will have more replay value.

Objectives
Create the following list of words: 'python', 'java', 'kotlin', 'javascript'.
Program the game to choose a word from the list at random. You can enter more words, but let's stick to these four for now.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

Example 1. The computer randomly chose python from the list.

H A N G M A N
Guess the word: > python
You survived!
Example 2. The computer randomly chose something other than python from the list.

H A N G M A N
Guess the word: > python
You lost!
Example 3. The computer randomly chose something other than kotlin from the list.

H A N G M A N
Guess the word: > kotlin
You lost!
 Report a typo
'''

# Write your code here
import random
a = input("""
H A N G M A N
Guess the word: 
""")

b = ['python', 'java', 'kotlin', 'javascript']
random.seed()
c = random.choice(b)
if a == c:
    print("You survived!")
else:
    print("You lost!")
    
    
\\

import random


class Hangman:
    mistakes = 0
    words_list = [
        "python",
        "java",
        "kotlin",
        "javascript"
    ]

    def __init__(self):
        self.hidden_word = random.choice(self.words_list)

    def greetings(self):
        print("H A N G M A N")

    def read_user_word(self):
        word = input("Guess the word: ").lower()
        return word

    def run(self):
        self.greetings()
        word = self.read_user_word()
        if word == self.hidden_word:
            print("You survived!")
        else:
            print("You lost!")


def main():
    game = Hangman()
    game.run()


if __name__ == "__main__":
    main()

    
