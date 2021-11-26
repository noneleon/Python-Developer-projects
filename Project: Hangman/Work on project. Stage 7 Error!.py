'''
Description
Now that we are done with the basics, let's work on perfecting some details.

In the previous stage, if the user entered the same letter twice, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. This doesn’t seem fair to the player, does it? They gain no additional information about the situation on the field yet the program still reduces their remaining attempts. Let's fix it!

Objectives
If the user enters the same letter twice, then the program should output You've already guessed this letter . This message should also be printed if the user inputs a letter that doesn't appear in the word. The number of attempts shouldn't be decreased in this case.
Also, you should check to make sure the player entered an English lowercase letter. If not, the program should print Please enter a lowercase English letter .
You should also check if the player entered exactly one letter. If not, the program should print You should input a single letter . Remember that zero is also not one!
Note that none of these three errors should reduce the number of remaining attempts!
Please, make sure that your program's output formatting precisely follows the output formatting in the example. Pay attention to the empty lines between tries and in the end.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

Example 1

H A N G M A N

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
Example 2

H A N G M A N

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word

j---
Input a letter: > +
Please enter a lowercase English letter

j---
Input a letter: > A
Please enter a lowercase English letter

j---
Input a letter: > ii
You should input a single letter

j---
Input a letter: > ++
You should input a single letter

j---
Input a letter: >
You should input a single letter

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v
You guessed the word java!
You survived!

'''
import random
from string import ascii_lowercase
print('H A N G M A N')
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
# word = random.choice(['java'])
s = set()
w = set()
lives = 8
while lives > 0:
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
        print('You guessed the word' + word +'!\nYou survived!')
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

    def play(self) -> None:
        """
        Start the game loop.
        """
        print('H A N G M A N')
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
    Hangman().play()

\\

import random

print("H A N G M A N")

possible_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(possible_words)
hidden = "-" * len(word)
hidden = list(hidden)
lives = 8
used_letters = list()

while lives:
     print(f"\n{''.join(hidden)}")
     if not '-' in hidden:
          print("You guessed the word!")
          print("You survived!")
          break
     guess = input("Input a letter: ")
     if len(guess) != 1:
          print("You should input a single letter")
     elif guess in used_letters:
          print("You've already guessed this letter")
     elif not guess.islower():
          print("Please enter a lowercase English letter")
     elif guess in word:
          for j in range(len(word)):
               if hidden[j] == '-':
                    if word[j] == guess:
                         hidden[j] = guess
     else:
          lives -= 1
          print("That letter doesn't appear in the word")
     used_letters.append(guess)
     if lives <= 0:
          print("You lost!")

    
