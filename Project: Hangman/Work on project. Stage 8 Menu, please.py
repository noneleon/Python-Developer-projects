'''
Description
We're almost done!

Let's add a little more flavor to the game by adding a suggestion to replay the game after the current session ends.

Objectives
The game starts with a menu where a player can choose to either play or exit.
Print Type "play" to play the game, "exit" to quit: and show this message again if the player inputs something else.
If the user chooses to play, the game begins.
Please, make sure that your program's output formatting precisely follows the output formatting in the example. Pay attention to the empty lines between tries and in the end.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

H A N G M A N
Type "play" to play the game, "exit" to quit: > play

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word

-a-a---i--
Input a letter: > o
You've already guessed this letter

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You've already guessed this letter

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > a
You've already guessed this letter

-a-a---ip-
Input a letter: > z
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > t

-a-a---ipt
Input a letter: > x
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > b
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > d
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > w
That letter doesn't appear in the word
You lost!

Type "play" to play the game, "exit" to quit: > exit
'''

import random
from string import ascii_lowercase
print('H A N G M A N')
print('Type "play" to play the game, "exit" to quit: ', end='')
x = input()
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
# word = random.choice(['java'])
s = set()
w = set()
lives = 8
while x != 'play':
	if x == 'exit':
		exit()
	print('Type "play" to play the game, "exit" to quit: ', end = '')
	x = input()
while lives > 0 and x == 'play':
    print()
    for k in word:
        if k in s:
            print(k, end='')
        else:
            print('-', end='')
    print()
    print('Input a letter: ', end='')
    n = input()
    if n not in word and n not in w and n in ascii_lowercase:
        print('That letter doesn\'t appear in the word')
        lives -= 1
        w.add(n)
    elif n in w:
        print('You\'ve already guessed this letter')
        lives -= 0
    elif n in s:
        print('You\'ve already guessed this letter')
        lives -= 0
    elif len(n) > 1:
        print('You should input a single letter')
        lives -= 0
    elif n not in ascii_lowercase:
        print('Please enter a lowercase English letter')
        lives -= 0
    else:
        s.add(n)
    if set(word) == s:
        print('You guessed the word ' + word +'!\nYou survived!')
        break
else:
    print('You lost!')
    
\\

from random import choice


class Hangman:
    """
    Class representing the 'Hangman' game.

    """
    words = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self, attempts: int = 8) -> None:
        """
        Initialize the game, that is, choose the answer randomly from
        Hangman.words and set the number of attempts. Additionally,
        create a set that will store guesses and the set of all letters
        appearing in the answer.

        :param attempts: The number of attempts. The default is 8.
        """
        self.answer = choice(self.words)
        self.attempts = attempts
        self.guesses = set()
        self.letters = set(self.answer)

    def check_letter(self, letter: str) -> None:
        """
        Check whether the letter is in the word and add it to the set of
        guesses.

        :param letter: letter to check.
        """
        if len(letter) != 1:
            print('You should input a single letter')
            return
        if not letter.islower():
            print('Please enter a lowercase English letter')
            return
        if letter in self.guesses:
            print("You've already guessed this letter")
        else:
            self.guesses.add(letter)
            if letter not in self.letters:
                print("That letter doesn't appear in the word")
                self.attempts -= 1

    def print_guess(self):
        print('')
        for letter in self.answer:
            if letter in self.guesses:
                print(letter, end='')
            else:
                print('-', end='')
        print('')

    def menu(self) -> None:
        """Display the game menu."""
        print('H A N G M A N')
        while True:
            input_ = input('Type "play" to play the game, "exit" to quit: ')
            if input_ == 'play':
                self.play()
            elif input_ == 'exit':
                return

    def play(self) -> None:
        """
        Start the game loop.
        """
        while self.attempts:
            self.print_guess()
            self.check_letter(input('Input a letter: '))

            if self.letters.issubset(self.guesses):
                print(f'You guessed the word {self.answer}!')
                print('You survived!')
                break
        else:
            print('You lost!')


if __name__ == '__main__':
    Hangman().menu()

    
\\
from random import choice
import sys


while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        print("H A N G M A N")
        hidden_word = choice(['python', 'java', 'kotlin', 'javascript'])
        prompt = '-' * len(hidden_word)
        i = 0
        letters = []
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while i < 8:
            print('\n' + prompt)
            if prompt.find('-') == -1:
                print('You guessed the word!\nYou survived!')
                sys.exit(0)
            letter = input('Input a letter: ')
            if len(letter) > 1:
                print('You should input a single letter!')
                continue
            if letter in uppercase_letters or letter not in (uppercase_letters and uppercase_letters.lower()):
                print('Please enter a lowercase English letter!')
                continue
            if letter in letters:
                print('You\'ve already guessed this letter!')
                continue
            letters.append(letter)
            if letter in hidden_word:
                j = -1
                while True:
                    j = hidden_word.find(letter, j + 1)
                    if j == -1:
                        break
                    prompt = prompt[0:j] + letter + prompt[j + 1:]
            else:
                print("That letter doesn't appear in the word")
                i += 1
                if i == 8:
                    print("You lost!")
                    sys.exit(0)
    elif menu == 'exit':
        sys.exit(0)
    else:
        continue

