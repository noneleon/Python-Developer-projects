'''
Description
How about some brand new rules? The original game has a fairly small choice of options.

Extended versions of the game are decreasing the probability of a draw, so it could be cool to play them.
Now, your program should be able to accept alternative lists of options, like Rock, Paper, Scissors, Lizard, Spock, or even a list like this:
![](https://ucarecdn.com/eb3f7a5b-98ea-4b11-a3b7-4797ee774258/)
At this stage, before the start of the game, the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by a comma. For example,

rock,paper,scissors,lizard,spock

If the user inputs an empty line, your program should start the game with default options: rock, paper, and scissors.

After the game options are defined, your program should output Okay, let's start.

Whatever list of options the user chooses, your program, obviously, should be able to identify which option beats which, that is, the relationships between different options. First, every option is equal to itself (causing a draw if both the user and the computer choose the same option). Secondly, every option wins over one half of the other options of the list and gets defeated by another half. How to determine which options are stronger or weaker than the option you're currently looking at? Well, you can try to do it this way: take the list of options (provided by the user or the default one). Find the option for which you want to know its relationships with other options. Take all the options that follow this chosen option in the list. Add to them the list of options that precede the chosen option. Now you have another list of options that doesn't include the "chosen" option and has a different order of elements in it (first go the options following the chosen one in the original list, after them are the ones that precede it). So, in this "new" list, the first half of the options will be defeating the "chosen" option, and the second half will get beaten by it.

For example, the user's list of options is rock,paper,scissors,lizard,spock. You want to know what options are weaker than lizard. By looking at the list spock,rock,paper,scissors you realize that spock and rock will be beating the lizard, and paper and scissors will get defeated by it. For spock it'll be almost the same, but it'll get beaten by rock and paper, and prevail over scissors and lizard. For the version of the game with 15 options, you can look at the picture above to understand the relationships between options.

Of course, this is not the most efficient way to determine which option prevails over which. You are welcome to try to develop some other methods of tackling this problem.

Objectives
Your program should:

Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
Read input specifying the user's name and output a new line Hello, <name>
Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting the user's score from 0.
Read input specifying the list of options that will be used for playing the game (options are separated by comma). If the input is an empty line, play with default options.
Output a line Okay, let's start
Play the game by the rules defined in the previous stages:
Read the user's input
If the input is !exit, output Bye! and stop the game
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed
For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
If the input corresponds to anything else, output Invalid input
Play the game again (with the same options that were defined before the start of the game)

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter your name: > Tim
Hello, Tim
> rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
Okay, let's start
> rock
Sorry, but the computer chose air
> !rating
Your rating: 0
> rock
Well done. The computer chose sponge and failed
> !rating
Your rating: 100
> !exit
Bye!
Example 2:

Enter your name: > Tim
Hello, Tim
> 
Okay, let's start
> rock
Well done. The computer chose scissors and failed
> paper
Well done. The computer chose rock and failed
> paper
There is a draw (paper)
> scissors
Sorry, but the computer chose rock
> !exit
Bye!
 Report a typo

'''
from enum import Enum
from random import randint


class Choose(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class RPSEngine:
    OPTIONS = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.rating_file = open('rating.txt', mode='a')
        self.actual_user = None
        self.actual_user_score = 0
        self.game_options = None
        self.rating_file.close()

    def evaluate(self, hplay, cpuplay):
        if hplay == cpuplay:
            print("There is a draw ({})".format(cpuplay))
            self.actual_user_score += 50
        else:
            index_option = self.game_options.index(hplay)
            new_options = self.game_options[index_option + 1:] + self.game_options[:index_option]
            options_divider = len(new_options) // 2
            defeated_options = new_options[:options_divider]
            beating_options = new_options[options_divider:]
            if cpuplay in defeated_options:
                print("Sorry, but the computer chose {}".format(cpuplay))
            elif cpuplay in beating_options:
                print("Well done. The computer chose {} and failed!".format(cpuplay))
                self.actual_user_score += 100

    def start_game(self):
        input_choice = input()
        while input_choice in RPSEngine.OPTIONS:
            human_choice = self.human_play(input_choice)
            cpu_choice = self.cpu_play()
            self.evaluate(human_choice, cpu_choice)
            input_choice = input()
        else:
            if input_choice == '!exit':
                print("Bye!")
            elif input_choice == '!rating':
                print(self.actual_user_score)
            else:
                print("Invalid input")

    def register_name(self, user_name):
        previous_player = False
        self.rating_file = open('rating.txt', mode='r+')

        for line in self.rating_file:
            name, rate = line.split()
            if name == user_name:
                self.actual_user_score = int(rate)
                previous_player = True
                break
        if not previous_player:
            self.rating_file.write('{} 0\n'.format(user_name))
        self.rating_file.close()
        self.actual_user = user_name

    def update_score(self):
        self.rating_file = open('rating.txt', mode='r')
        entries = self.rating_file.readlines()
        self.rating_file.close()
        for index, entry in enumerate(entries):
            if self.actual_user in entry:
                entries[index] = '{} {}\n'.format(self.actual_user, self.actual_user_score)

        self.rating_file = open('rating.txt', mode='w')
        self.rating_file.writelines(entries)

    def chose_options(self):
        options = input()
        self.game_options = options.split(',') if options else ['rock', 'paper', 'scissors']
        RPSEngine.OPTIONS = self.game_options

    def new_game(self):
        name = input('Enter your name: ')
        print('Hello, {}'.format(name))
        self.register_name(name)
        self.chose_options()
        print("Okay, let's start")
        self.start_game()
        self.update_score()

    def human_play(self, choice):
        return choice if choice in RPSEngine.OPTIONS else None

    def cpu_play(self):
        choice = randint(0, 2)
        return RPSEngine.OPTIONS[choice]


if __name__ == '__main__':
    rps_game = RPSEngine()
    rps_game.new_game()
    
    
\\

import random


class Game:
    USER_WIN = 'User'
    COMPUTER_WIN = 'Computer'
    COMMANDS = {
        'QUIT': '!exit',
        'RATING': '!rating',
    }


def determine_winning_and_losing_traits(user_choice, shapes):
    amount = len(shapes) // 2
    choice_index = shapes.index(user_choice)

    all_except_choice = []
    # Recreate list of elements based on user choice
    all_except_choice += shapes[choice_index + 1:]
    all_except_choice += shapes[:choice_index]

    beaten_by_user_choice = all_except_choice[amount:]
    beat_user_choice = all_except_choice[:amount]

    return beaten_by_user_choice, beat_user_choice


def find_winner(user_choice, computer_choice, shapes):
    winning_shapes, losing_shapes = determine_winning_and_losing_traits(user_choice, shapes)
    if computer_choice in losing_shapes:
        return Game.COMPUTER_WIN
    else:
        return Game.USER_WIN


messages = {
    'enter_name': 'Enter your name: ',
    'greet': 'Hello, {name}',
    'start': 'Okay, let\'s start',
    'lose': 'Sorry, but the computer chose {option}',
    'draw': 'There is a draw ({option})',
    'win': 'Well done. The computer chose {option} and failed',
    'invalid': 'Invalid input',
    'rating': 'Your rating: {rating}',
    'quit': 'Bye!',
}

# rock > scissors
# paper > rock
# scissors > paper
hand_shapes = ['rock', 'paper', 'scissors']

# Meet & greet
user_name = input(messages['enter_name'])
print(messages['greet'].format(name=user_name))

# Read file & get data for existing ratings
user_rating = 0
with open('rating.txt', 'r') as rating_file:
    for line in rating_file:
        current_score = line.split()
        if current_score[0] == user_name:
            user_rating = int(current_score[1])
            break

# Read custom list of hand shapes
input_shapes = input()
if input_shapes:
    hand_shapes = input_shapes.split(',')

print(messages['start'])

while True:
    # Choose random computer shape
    computer_input = random.choice(hand_shapes)

    # Take user input
    user_input = input()

    # Test user input for value
    if user_input == Game.COMMANDS['QUIT']:
        print(messages['quit'])
        break
    if user_input == Game.COMMANDS['RATING']:
        print(messages['rating'].format(rating=user_rating))
        continue
    if user_input not in hand_shapes:
        print(messages['invalid'])
        continue

    # Handle draw
    if user_input == computer_input:
        print(messages['draw'].format(option=computer_input))
        user_rating += 50
        continue

    # Handle the rest of cases
    winner = find_winner(user_input, computer_input, hand_shapes)

    if winner == Game.USER_WIN:
        print(messages['win'].format(option=computer_input))
        user_rating += 100
        continue
    elif winner == Game.COMPUTER_WIN:
        print(messages['lose'].format(option=computer_input))
        continue

\\

import random


def list_of_plays(x):
    return x.split(',')


def find_losses(play, list_of_x):
    i = list_of_x.index(play)
    ordered_list = list_of_x[i:] + list_of_x[:i]
    return ordered_list[1:((len(list_of_x) // 2) + 1)]


default_plays = ['rock', 'paper', 'scissors']

player_name = input("Enter your name:")
player_score = 0
print(f'Hello, {player_name}')
raw_plays = input()

if raw_plays == '':
    plays = default_plays
else:
    plays = list_of_plays(raw_plays)

ratings = open('rating.txt', 'r')
for line in ratings:
    if line.startswith(f'{player_name} '):
        player_score = int(line.strip(f'{player_name} '))
ratings.close()

print("Okay, let's start")

while True:
    user_plays = input()
    if user_plays == "!exit":
        print('Bye!')
        break
    elif user_plays == '!rating':
        print(f'Your rating: {player_score}')
        continue
    elif user_plays not in list(plays):
        print('Invalid input')
        continue
    computer_plays = random.choice(list(plays))

    losing_plays = find_losses(user_plays, plays)

    if computer_plays in losing_plays:
        print(f'Sorry, but the computer chose {computer_plays}')
    elif user_plays == computer_plays:
        print(f'There is a draw ({computer_plays})')
        player_score += 50
    else:
        print(f'Well done. The computer chose {computer_plays} and failed')
        player_score += 100


        
        




