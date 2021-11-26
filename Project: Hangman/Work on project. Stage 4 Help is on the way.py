'''
Description
Now our game has become quite hard, and your chances of guessing the word depend on the size of the list. When the list has four words, you only have a 25% chance to guess correctly. So let's show a little mercy to the player and add a hint for them.

Objectives
As in the previous stage, you should use the following word list: 'python', 'java', 'kotlin', 'javascript'
Once the computer has chosen a word from the list, show its first 3 letters. Hidden letters should be replaced with hyphens ("-").
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

Example 1

H A N G M A N
Guess the word jav-: > java
You survived!
Example 2

H A N G M A N
Guess the word pyt---: > pythia
You lost!

'''

# Write your code here
import random
b = ['python', 'java', 'kotlin', 'javascript']
random.seed()
c = random.choice(b)
a_1  =   c[0:3]
a_2 = ("-" *(len(c) - 3))
a = a_1 + a_2
print("H A N G M A N")
a = input(f'Guess the word {a}:')
if a == c:
    print("You survived!")
else:
    print("You lost!")
    
    
\\

import random

word_list = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(word_list)
exposed = ''.join((choice[:3], "-" * (len(choice) - 3)))
print("H A N G M A N")
inp = input(f"Guess the word {exposed} : ")
if inp == choice:
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

    def read_user_word(self, encoded_word):
        word = input(f"Guess the word {encoded_word}: ").lower()
        return word

    def encode_word(self):
        encoded_word = self.hidden_word[:3] + '-' * (len(self.hidden_word) - 3)
        return encoded_word

    def run(self):
        self.greetings()
        encoded_word = self.encode_word()
        word = self.read_user_word(encoded_word)
        if word == self.hidden_word:
            print("You survived!")
        else:
            print("You lost!")


def main():
    game = Hangman()
    game.run()


if __name__ == "__main__":
    main()

