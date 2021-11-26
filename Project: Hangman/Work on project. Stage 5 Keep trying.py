'''
Description
Let's make the game iterative. Now it's time to make the game resemble the classic version of Hangman a bit more. The player should now guess letters in the word instead of typing the entire word all at once. If the player guesses a letter, it should be uncovered in the word. For now, start by building the defeat condition and add 8 tries to guess a letter that appears in the word. When the player runs out of attempts, the game ends.

Later we will determine the winning conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

Objectives
Now your game should work as follows:

A player has exactly 8 tries and enters letters. Nothing changes if a player has more tries left but they have already guessed the word.
If the letter doesn't appear in the word, the computer takes one try away – even if the user has already guessed this letter.
If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.
Also, the word should be selected from our list: 'python', 'java', 'kotlin', 'javascript', so that your program can be tested more reliably.
Please, make sure that your program's output formatting precisely follows the example. Pay attention to the empty lines between tries and at the end.
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
Input a letter: > z
That letter doesn't appear in the word

-a-a---i--
Input a letter: > l
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > p

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

Thanks for playing!
We'll see how well you did in the next stage
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
Input a letter: > o
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v

java
Input a letter: > a

java
Input a letter: > j

Thanks for playing!
We'll see how well you did in the next stage

'''

import random

def loadWords():
    word_list = ['javascript']
    # word_list = ['python', 'kotlin', 'java', 'javascript']
    return random.choice(word_list)

word = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    if c == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '-'
    return ans
    print(ans)

def getAvailableLetters(lettersGuessed):
    import string
    ans = list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)
    print(ans)

def hangman(secretWord):
    print("H A N G M A N")
    print()
    hidden = len(word)
    hint = "-" * hidden
    print(hint)
# print("Welcome to the game, Hangman!")
# print("I am thinking of a word that is", len(secretWord), "letters long.")
#
    global lettersGuessed
    turns = 0
    lettersGuessed = []

    while 8 - turns > 0:
        turns += 1
        if isWordGuessed(secretWord, lettersGuessed):
        # 	print(word)
        # 	print("Congratulations, you won!")
        # 	break
            continue

        else:
            # print("-------------")
            # print("You have", 8 - mistakeMade, "guesses left.")
            # print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = str(input("Input a letter: ")).lower()
            print()
            # if guess in lettersGuessed:
            # 	print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

            if guess in secretWord and guess not in lettersGuessed:
                # x = guess in secretWord and guess not in lettersGuessed
                lettersGuessed.append(guess)
                print(getGuessedWord(secretWord, lettersGuessed))

            else:
                lettersGuessed.append(guess)
                print("No such letter in the word.")
                print()
                if 8 - turns > 0:
                    print(getGuessedWord(secretWord, lettersGuessed))

        if 8 - turns == 0:
            # print(word)
            print("Thanks for playing!")
            print("We'll see how well you did in the next stage")
            break

        else:
            continue

secretWord = word.lower()
hangman(secretWord)
\\

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
        Hangman.words and set the number of attempts.

        :param attempts: The number of attempts. The default is 8.
        """
        self.answer = choice(self.words)
        self.guess = list('-' for _ in self.answer)
        self.attempts = attempts

    def check_letter(self, letter: str) -> None:
        """
        Check whether the letter is in the word and update the guess
        appropriately.

        :param letter: letter to check.
        :raises LengthError: if the letter string is not of length 1.
        """
        if len(letter) != 1:
            raise LengthError
        found = False
        for index, char in enumerate(self.answer):
            if char == letter:
                self.guess[index] = letter
                found = True
        self.attempts -= 1
        if not found:
            print("That letter doesn't appear in the word")

    def play(self) -> None:
        """
        Start the game loop.
        """
        print('H A N G M A N')
        while self.attempts:
            print('')
            print(''.join(self.guess))
            self.check_letter(input('Input a letter: '))
        print('')
        print('Thanks for playing!')
        print("We'll see how well you did in the next stage")


def main():
    Hangman().play()


if __name__ == '__main__':
    main()

\\

import random

word_list = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(word_list)
basket = set(choice)
counter = 8
exposed = ''.join(("-" * len(choice)))
print("H A N G M A N")

while counter > 0:
    inp_index = 0
    print("")
    print(exposed)
    inp = input('Input a letter: ')
    if inp in basket:
        inp_index = choice.find(inp)
        exposed = exposed[:inp_index] + inp + exposed[inp_index+1:]
        counter -= 1
    else:
        print("That letter doesn't appear in the word")
        counter -= 1

    if counter == 0:
        print("")
        print("Thanks for playing!\nWe'll see how well you did in the next stage")
        break

    



