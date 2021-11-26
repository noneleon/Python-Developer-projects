'''
Description
Files are used to save progress and restore it the next time the user runs the program. It's tedious to print the actions manually. Sometimes you can just forget to do it! Let's add run arguments that define which file to read at the start and which file to save at the exit.

Objectives
When provided with command-line arguments, your program should do the following:

If --import_from=IMPORT is passed, where IMPORT is the file name, read the initial card set from the external file, and print the message n cards have been loaded. as the first line of the output, where n is the number of cards loaded from the external file. If such an argument is not provided, the set of cards should initially be empty and no message about card loading should be output.
If --export_to=EXPORT is passed, where EXPORT is the file name, write all cards that are in the program memory into this file after the user has entered exit, and the last line of the output should be n cards have been saved., where n is the number of flashcards in the set.
Run arguments examples
python flashcards.py --import_from=derivatives.txt
python flashcards.py --export_to=animals.txt
python flashcards.py --import_from=words13june.txt --export_to=words14june.txt
python flashcards.py --export_to=vocab.txt --import_from=vocab.txt 
'''

"""Flashcards can be used to remember any sort of data,
so this script is meant to be a useful learning tool"""
import random
from io import StringIO
import json
import logging
import sys
import argparse


class Flashcard:

    def __init__(self):
        """initiating the class using :
        log=StringIO object to store a log file
        flashcards = {} a dictionary to store the data"""

        self.log = StringIO()
        self.flashcards = {}

    def get_log(self, func):
        """prints the outputs both to console and to the log object"""
        targets = logging.StreamHandler(sys.stdout), logging.StreamHandler(self.log)
        logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=targets)
        logging.info(func)

    def compare_answers(self, definition, answer):
        """compares user's answer to the definition saved in the dictionary,
        updates the 'mistakes' count if user's answer is wrong
        returns an suitable response"""
        term_list = list(self.flashcards.keys())
        def_list = [self.flashcards[term]["word_def"] for term in term_list]

        if answer != definition:
            def_pos = def_list.index(definition)  # store the index for the definition
            if answer in def_list:
                pos = def_list.index(answer)
                self.flashcards[term_list[def_pos]]["mistake"] += 1

                return f'Wrong. The right answer is "{definition}",\
 but your definition is correct for "{term_list[pos]}".\n'
            else:
                self.flashcards[term_list[def_pos]]["mistake"] += 1

                return f'Wrong. The right answer is "{definition}".\n'

        return "Correct !\n"

    def add_cards(self):
        """adds user inputs data to the dictionary"""
        message = f"The card:\n"
        word_term = input(message)
        print(message, word_term, file=self.log, flush=True)
        definitions = [self.flashcards[card]["word_def"] for card in self.flashcards]
        while word_term in self.flashcards.keys():
            message = f'The card "{word_term}" already exists.\n'
            word_term = input(message)
            print(message, word_term, file=self.log, flush=True)
        else:
            message = f"The definition of the card:\n"
            word_def = input(message)
            print(message, word_def, file=self.log, flush=True)
            while word_def in definitions:
                message = f'The definition "{word_def}" already exists.\n'
                word_def = input(message)
                print(message, word_def, file=self.log, flush=True)
            else:
                self.flashcards[word_term] = {"word_def": word_def, "mistake": 0}
                return f'The pair ("{word_term}":"{word_def}") has been added.\n'

    def remove_cards(self, card):
        """removes a card from dictionary"""
        try:
            del self.flashcards[card]
            return "The card has been removed.\n"
        except KeyError:
            return f'Can\'t remove "{card}": there is no such card.\n'

    def import_from_file(self, file_name):
        """imports data from an input file and updates data dictionary"""
        try:
            with open(file_name, "r+") as file:
                cards = json.load(file)
            self.flashcards = self.flashcards | cards

            return f"{len(cards)} cards have been loaded\n"
        except FileNotFoundError:
            return "File not found.\n"

    def export_to_file(self, file_name):
        """exports data from dictionary to a input file"""
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.flashcards, file)
        return f"{len(self.flashcards)} cards have been saved.\n"

    def ask(self):
        """prompts user to enter the definition to a randomly chosen card
        returns the compare_answers method as an answer"""
        term_list = list(self.flashcards.keys())
        word = random.choice(term_list)
        message = f'Print the definition of "{word}":\n'
        user_answer = input(message)
        print(message, user_answer, file=self.log, flush=True)
        return self.compare_answers(self.flashcards[word]["word_def"], user_answer)

    def hardest_card(self):
        """finds the cards with the biggest number of mistakes
        returns a suitable message"""
        term_list = list(self.flashcards.keys())
        mistakes_list = [self.flashcards[card]["mistake"] for card in self.flashcards]
        positions = [i for i, x in enumerate(mistakes_list) if x == max(mistakes_list) and x > 0]
        if len(positions) == 1:
            return f"The hardest card is {term_list[positions[0]]}. \
You have {mistakes_list[positions[0]]} errors answering it.\n"
        elif len(positions) == 0:
            return f"There are no cards with errors.\n"
        else:
            hardest_list = [f'"{term_list[pos]}"' for pos in positions]
            return f'The hardest cards are {"{}, " * len(hardest_list)}\n'.format(*hardest_list)

    def reset_stats(self):
        """reset all the mistakes counts"""
        for card in self.flashcards:
            self.flashcards[card]["mistake"] = 0
        return f"Card statistics have been reset.\n"

    def log_to_file(self, file_name):
        """writes content of the log object to an input file"""
        with open(file_name, "w") as file:
            file.write(self.log.getvalue())
        return f"The log has been saved.\n"

    def exit_(self):
        """prints a message on exit"""
        return f"Bye Bye!\n"

    def main(self):
        """asks user for an input option and accesses the rest of the methods accordingly"""
        while True:
            menu = "Input the action (add, remove, import, export,\
 ask, exit, log, hardest card, reset stats):\n"
            user_choice = input(menu)
            print(menu, user_choice, file=self.log, flush=True)
            if user_choice == "exit":
                self.get_log(self.exit_())
                break
            elif user_choice == "add":
                self.get_log(self.add_cards())
            elif user_choice == "remove":
                message = input("Which card?\n")
                print(message, file=self.log, flush=True)
                self.get_log(self.remove_cards(message))
            elif user_choice == "import":
                message = input("File name:\n")
                print(message, file=self.log, flush=True)
                self.get_log(self.import_from_file(message))
            elif user_choice == "export":
                message = input("File name:\n")
                print(message, file=self.log, flush=True)
                self.get_log(self.export_to_file(message))
            elif user_choice == "ask":
                n_times = input("How many times to ask?\n")
                print(n_times, file=self.log, flush=True)
                for _ in range(int(n_times)):
                    self.get_log(self.ask())
            elif user_choice == "log":
                message = input("File name:\n")
                print(message, file=self.log, flush=True)
                self.get_log(self.log_to_file(message))
            elif user_choice == "hardest card":
                self.get_log(self.hardest_card())
            elif user_choice == "reset stats":
                self.get_log(self.reset_stats())
            else:
                self.get_log("No such option! Try again!")

    def arg_parser(self):
        """parser the arguments imputed by the user into the console"""
        parser = argparse.ArgumentParser()
        parser.add_argument("--import_from")
        parser.add_argument("--export_to")
        args = parser.parse_args()
        if args.import_from and args.export_to:
            self.get_log(self.import_from_file(args.import_from))
            self.main()
            self.get_log(self.export_to_file(args.export_to))
        elif args.import_from:
            self.get_log(self.import_from_file(args.import_from))
            self.main()
        elif args.export_to:
            self.main()
            self.get_log(self.export_to_file(args.export_to))
        else:
            self.main()


flashcard = Flashcard()
if __name__ == "__main__":
    flashcard.arg_parser()
    
\\

from collections import defaultdict
import random
import argparse

cards_dict = {}
statistics = defaultdict(int)
logs = []
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--import_from", default=None)
parser.add_argument("-e", "--export_to", default=None)
args = parser.parse_args()


def print_log(entry):
    print(entry)
    logs.append(entry)


def input_log():
    result = input()
    logs.append(result)
    return result


def add():
    print_log(f'The card:')
    while True:
        card = input_log()
        if card not in cards_dict.keys():
            break
        else:
            print_log(f'The term "{card}" already exists. Try again:')
    print_log(f'The definition of the card:')
    while True:
        definition = input_log()
        if definition not in cards_dict.values():
            break
        else:
            print_log(f'The definition "{definition}" already exists. Try again:')
    cards_dict[card] = definition
    print_log(f'The pair ("{card}":"{definition}") has been added.')


def remove():
    print_log('Which card?')
    rem = input_log()
    if rem in cards_dict:
        del cards_dict[rem]
        if rem in statistics:
            del statistics[rem]
        print_log('The card has been removed.')
    else:
        print_log(f'Can\'t remove "{rem}": there is no such card.')


def import_():
    try:
        print_log('File name:')
        file = input_log()
        with open(file, 'r') as f:
            count = 0
            for line in f.readlines():
                c, d, s = line.split('||')
                cards_dict[c.strip()] = d.strip()
                statistics[c] = int(s)
                count += 1
            print_log(f'{count} cards have been loaded.')
    except FileNotFoundError:
        print_log('File not found.')


def cli_import():
    file = args.import_from
    try:
        with open(file, 'r') as f:
            count = 0
            for line in f.readlines():
                c, d, s = line.split('||')
                cards_dict[c.strip()] = d.strip()
                statistics[c] = int(s)
                count += 1
            print_log(f'{count} cards have been loaded.')
    except FileNotFoundError:
        print_log('File not found.')


def export():
    print_log('File name:')
    file = input_log()
    with open(file, 'w') as f:
        for c, d in cards_dict.items():
            f.write(f'{c}||{d}||{statistics[c]}\n')
    print_log(f'{len(cards_dict)} cards have been saved.')


def cli_export():
    file = args.export_to
    with open(file, 'w') as f:
        for c, d in cards_dict.items():
            f.write(f'{c}||{d}||{statistics[c]}\n')
    print_log(f'{len(cards_dict)} cards have been saved.')


def ask():
    print_log('How many times to ask?')
    inp = int(input_log())
    for _ in range(inp):
        card = random.choice([x for x in cards_dict.keys()])
        print_log(f'Print the definition of "{card}":')
        inp = input_log()
        if inp == cards_dict[card]:
            print_log('Correct!')
        elif inp in cards_dict.values():
            print_log(f'Wrong. The right answer is "{cards_dict[card]}", but your definition is correct for \
"{list(cards_dict.keys())[list(cards_dict.values()).index(inp)]}".')
            statistics[card] += 1
        else:
            print_log(f'Wrong. The right answer is "{cards_dict[card]}".')
            statistics[card] += 1


def save_log():
    print_log('File name:')
    file_name = input_log()
    with open(file_name, 'w') as f:
        f.write("\n".join(logs))
    print_log('The log has been saved.')


def hardest():
    if statistics:
        if max(statistics.values()) == 0:
            print_log('There are no cards with errors.')
        else:
            errors = statistics.values()
            hard_num = list(errors).count(max(errors))
            if hard_num == 1:
                print_log(f'The hardest card is "{max(statistics, key=statistics.get)}".\
You have {max(errors)} errors answering it')
            else:
                hard_list = [f'"{x}"' for x in statistics.keys() if statistics[x] == max(errors)]
                print_log(f'The hardest cards are {", ".join(hard_list)}')
    else:
        print_log('There are no cards with errors.')


def main():
    if args.import_from:
        cli_import()
    while True:
        print_log('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
        action = input_log()
        if action == "add":
            add()
        elif action == "remove":
            remove()
        elif action == "import":
            import_()
        elif action == "export":
            export()
        elif action == "ask":
            ask()
        elif action == "exit":
            print_log('Bye bye!')
            if args.export_to:
                cli_export()
            break
        elif action == "log":
            save_log()
        elif action == "hardest card":
            hardest()
        elif action == "reset stats":
            statistics.clear()
            print_log('Card statistics have been reset.')
        elif action == "stats":
            print(statistics)


if __name__ == '__main__':
    main()