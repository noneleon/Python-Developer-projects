'''
Description
The most recent version of the game is not so much fun, since we still don’t have a way to handle the player's victory. The player has 8 attempts to guess letters, and the number of remaining attempts decreases after each try even if the player guesses correctly.

In this next version, a player may get a lot of attempts because they are limited only by the number of mistakes they make. A player can be mistaken 8 times. They win when they have guessed all the letters and still have at least one try. If the player uses their last try and actually guesses the word, then they’ve won!

Objectives
The player starts the game with 8 "lives", which is to say, our player can input a wrong letter 8 times.

Print That letter doesn't appear in the word and reduce the number of remaining attempts if the word selected by the program doesn't contain this letter.
Print No improvements and reduce the attempts count if the selected word contains this letter but the user has already tried guessing it.
The number of remaining attempts should be decreased only if there are no letters to uncover.
Please, make sure that your program's output formatting precisely follows the output formatting in the example. Pay attention to the empty lines between tries and at the end.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

Example 1

H A N G M A N

------
Input a letter: > t

--t---
Input a letter: > z
That letter doesn't appear in the word

--t---
Input a letter: > t
No improvements

--t---
Input a letter: > t
No improvements

--t---
Input a letter: > y

-yt---
Input a letter: > x
That letter doesn't appear in the word

-yt---
Input a letter: > y
No improvements

-yt---
Input a letter: > p

pyt---
Input a letter: > p
No improvements

pyt---
Input a letter: > q
That letter doesn't appear in the word

pyt---
Input a letter: > p
No improvements
You lost!
Example 2

H A N G M A N

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v

java
You guessed the word!
You survived!

'''
import random
words = ['python', 'java', 'kotlin', 'javascript' ]
hidden = random.choice(words)
corr_word = ''
all_letters = ''
tries = 0
print("H A N G M A N")
while tries < 8:
    result = ''
    for l in hidden:
        if l in corr_word:
            result += l
        else:
            result += '-'
    print()
    print('{}'.format(result))
    if set(hidden) == set(corr_word):
        print('You survived!')
        break
    while True:
        user_letter = input('Input a letter: ')
        all_letters += user_letter
        break
    if user_letter not in hidden:
        tries += 1
        print('That letter doesn\'t appear in the word')
    elif user_letter in corr_word:
        tries += 1
        print('No improvements')
    else:
        corr_word += user_letter
if tries == 8:
    print('You lost!')
    exit()
    
    
\\


from collections import defaultdict
from random import choice


class Error(Exception):
    """
    Base error class for the hangman.py module.
    """
    pass


class LengthError(Error):
    """
    Raise when the input string is not of length 1.
    """
    pass


class Hangman:
    """
    Class representing the 'Hangman' game.

    """
    words = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self, attempts: int = 8) -> None:
        """
        Initialize the game, that is, choose the answer randomly from
        Hangman.words and set the number of attempts. Additionally,
        create a set that will store correct guesses and finally,
        create a dictionary with letters of the chosen word as keys and
        lists of indexes of those letters as values.

        :param attempts: The number of attempts. The default is 8.
        """
        self.answer = choice(self.words)
        self.attempts = attempts
        self.correct_guesses = set()
        self.lut = defaultdict(list)
        for index, letter in enumerate(self.answer):
            self.lut[letter].append(index)

    def check_letter(self, letter: str) -> None:
        """
        Check whether the letter is in the word and update the guess
        appropriately.

        :param letter: letter to check.
        :raises LengthError: if the letter string is not of length 1.
        """
        if len(letter) != 1:
            raise LengthError
        if letter in self.correct_guesses:
            print('No improvements')
            self.attempts -= 1
        elif letter in self.lut:
            self.correct_guesses.add(letter)
        else:
            print("That letter doesn't appear in the word")
            self.attempts -= 1

    def print_guess(self):
        print('')
        for letter in self.answer:
            if letter in self.correct_guesses:
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

        if set(self.lut) == self.correct_guesses:
            print('You guessed the word!')
            print('You survived!')
        else:
            print('You lost!')


if __name__ == '__main__':
    Hangman().play()

    

\\

from random import choice


class Hangman:
    choices_word = choice(['python', 'java', 'kotlin', 'javascript'])

    def __init__(self):
        self.choice = self.choices_word
        self.hidden_word = '-' * len(self.choice)
        self.name = 'H A N G M A N'

    def guess_letter(self):
        letter = input('Input a letter: ')
        if letter in self.choice and letter not in self.hidden_word:
            for i in range(self.choice.count(letter)):
                if i:
                    index = self.choice.rfind(letter)
                else:
                    index = self.choice.find(letter)
                temp = list(self.hidden_word)
                temp[index] = letter
                self.hidden_word = ''.join(temp)
                return False
        if letter in self.hidden_word:
            print('No improvements')
            return True
        else:
            print("That letter doesn't appear in the word")
            return True

    def game(self):
        print(self.name)
        counter = 8
        while counter > 0:
            print('\n' + self.hidden_word)
            if self.guess_letter():
                counter -= 1
        self.check_word()
        print('You lost!')

    def check_word(self):
        if self.hidden_word == self.choice:
            print('You guessed the word!')
            print('You survived!')
            exit()


game_hangman = Hangman()
game_hangman.game()


