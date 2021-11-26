'''
Description
While studying, it may be very helpful to pay more attention to challenging parts where you make the most mistakes. In this stage, you will add some statistics features to your program so that the users can track their progress.

Implement the following additional actions:

save the application log to the given file: log
print the term or terms that the user makes most mistakes with: hardest card
erase the mistake count for all cards: reset stats
Remember that now you need to store three items (term, definition, mistakes) instead of two (term, definition).

You may want to take a look at io.StringIO objects: handling the log will be easier with them.

Objectives
Print the message Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats): each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.

The program's behavior depends on the user's input action:

log — ask the user where to save the log with the message File name:, save all the lines that have been input in/output to the console to the file, and print the message The log has been saved. Don't clear the log after saving it to the file.
hardest card — print a string that contains the term of the card with the highest number of wrong answers, for example, The hardest card is "term". You have N errors answering it. If there are several cards with the highest number of wrong answers, print all of the terms: The hardest cards are "term_1", "term_2". If there are no cards with errors in the user's answers, print the message There are no cards with errors.
reset stats — set the count of mistakes to 0 for all the cards and output the message Card statistics have been reset.
Update your import and export actions from the previous stage, so that the error count for each flashcard is also imported and exported.

Example
The symbol > represents the user input. Note that it's not part of the input.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
There are no cards with errors.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> import
File name:
> capitals.txt
28 cards have been loaded.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
The hardest card is "France". You have 10 errors answering it.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> ask
How many times to ask?
> 1
Print the definition of "Russia":
> Paris
Wrong. The right answer is "Moscow", but your definition is correct for "France" card.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
The hardest cards are "Russia", "France". You have 10 errors answering them.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> reset stats
Card statistics have been reset.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
There are no cards with errors.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> log
File name:
> todayLog.txt
The log has been saved.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> exit
Bye bye!
Note that all your outputs and user inputs should be on separate lines.


'''
import os
import io
import sys
import json
import random
import logging
from pathlib import Path


class FlashCard:
    def __init__(self):
        self.stream = io.StringIO()
        self.handler = logging.StreamHandler(self.stream)
        self.console = logging.StreamHandler(sys.stdout)
        self.handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s: %(message)s'))
        self.cards = []
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def add_handler(self):
        self.logger.addHandler(self.handler)
        self.logger.addHandler(self.console)

    def remove_handler(self):
        self.logger.removeHandler(self.handler)
        self.logger.removeHandler(self.console)

    def run(self):
        self.menu()

    def menu(self):
        while True:
            self.add_handler()
            self.logger.info("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            self.remove_handler()
            action = input()
            if action == "add":
                self.add()
            elif action == "remove":
                self.remove()
            elif action == "import":
                self.import_cards()
            elif action == "export":
                self.export_cards()
            elif action == "ask":
                self.ask()
            elif action == "log":
                self.log()
            elif action == "hardest card":
                self.hardest_card()
            elif action == "reset stats":
                self.reset()
            elif action == "exit":
                self.add_handler()
                self.logger.info("Bye bye!")
                self.remove_handler()
                exit(0)

    def add(self):
        self.add_handler()
        self.logger.info(f"The card:")
        while True:
            term = input()
            if term in Card.terms:
                self.logger.info(f'The term "{term}" already exists. Try again:')
                continue
            else:
                break
        self.logger.info(f"The definition of the card:")
        while True:
            definition = input()
            if definition in Card.definitions:
                self.logger.info(f'The definition "{definition}" already exists. Try again:')
                continue
            else:
                break
        new_card = Card(term, definition)
        self.cards.append(new_card)
        self.logger.info(f'The pair ("{term}":"{definition}") has been added.')
        self.remove_handler()

    def remove(self):
        self.add_handler()
        self.logger.info("Which card?")
        term = input()
        card = self.get_by_term(term)
        if card:
            self.cards.remove(card)
            self.logger.info("The card has been removed.")
        else:
            self.logger.info(f'''Can't remove "{term}": there is no such card.''')
        self.remove_handler()

    def import_cards(self):
        self.add_handler()
        self.logger.info("File name:")
        file_name = input()
        file = Path(os.path.join(os.path.curdir, file_name))
        if file.exists():
            with open(file, "r") as f:
                new_cards: dict = json.loads(f.read())
                new_cards: list = [Card(x, new_cards[x]) for x in new_cards]
                self.cards += new_cards
                self.logger.info(f"{len(new_cards)} cards have been loaded.")
        else:
            self.logger.info("File not found.")
        self.remove_handler()

    def export_cards(self):
        self.add_handler()
        self.logger.info("File name:")
        file_name = input()
        file = Path(os.path.join(os.path.curdir, file_name))
        with open(file, "w") as f:
            f.write(json.dumps({x.term: x.definition for x in self.cards}))
            self.logger.info(f"{len(self.cards)} cards have been saved.")
        self.remove_handler()

    def log(self):
        self.add_handler()
        self.logger.info("File name:")
        file_name = input()
        file = Path(os.path.join(os.path.curdir, file_name))
        logs = self.stream.getvalue()
        with open(file, "w") as f:
            f.write(logs)
        self.logger.info("The log has been saved.")
        self.remove_handler()

    def hardest_card(self):
        self.add_handler()
        if self.cards:
            largest = max([card.mistake for card in self.cards])
        else:
            largest = None
        if not largest:
            self.logger.info("There are no cards with errors.")
            self.remove_handler()
            return
        hardest: list[Card] = [card for card in self.cards if card.mistake == largest]
        if len(hardest) == 1:
            output = f'is "{hardest[0].term}"'
            card_s = "card"
            it_them = "it"
        else:
            output = f'are "{hardest[0].term}"'
            card_s = "cards"
            it_them = "them"
            for i in hardest[1:]:
                output += f', "{i.term}"'
        self.logger.info(f'The hardest {card_s} {output}. You have {largest} errors answering {it_them}.')
        self.remove_handler()

    def reset(self):
        self.add_handler()
        for card in self.cards:
            card.mistake = 0
        self.logger.info("Card statistics have been reset.")
        self.remove_handler()

    def ask(self):
        self.add_handler()
        self.logger.info("How many times to ask?")
        times = int(input())
        for _ in range(1, times + 1):
            card = random.choice(self.cards)
            self.logger.info(f'{_}: Print the definition of "{card.term}":')
            definition = input()
            if definition == card.definition:
                self.logger.info("Correct!")
            else:
                if definition in Card.definitions:
                    true_card = self.get_by_definition(definition)
                    self.logger.info(
                        f'Wrong. The right answer is "{card.definition}".but your definition is correct for "{true_card.term}".')
                else:
                    self.logger.info(f'Wrong. The right answer is "{card.definition}".')
                card.mistake += 1
        self.remove_handler()

    def get_by_definition(self, given_definition):
        for idx, card in enumerate(self.cards):
            if card.definition == given_definition:
                return card

    def get_by_term(self, given_term):
        for idx, card in enumerate(self.cards):
            if card.term == given_term:
                return card


class Card:
    terms = []
    definitions = []

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
        self.mistake = 0

    def __new__(cls, term, definition, *args, **kwargs):
        cls.terms.append(term)
        cls.definitions.append(definition)
        return super().__new__(cls)


if __name__ == "__main__":
    app = FlashCard()
    app.run()
    
    
\\


import json
import random

log = ""
hardest = {}


def dumplog(cards):
    global log
    fname = input("File name:\n")
    with open(f'{fname}', 'a+') as f:
        print(log, file=f)
        print("The log has been saved.\n")
    menu(cards)


def hard(cards):
    global hardest
    if hardest:
        err = max(hardest.values())
        hcards = [k for k, v in hardest.items() if v == err]
        multiple = len(hcards) > 1
        if multiple:
            print("The hardest cards are ", ", ".join(hcards),
                  f"\". You have {err} errors answering them.\n")
        else:
            print(f"The hardest card is \"{hcards[0]}\". You have {err} errors answering it.\n")
    else:
        lprint("There are no cards with errors.\n")
    menu(cards)


def reset(cards):
    global hardest
    hardest = {}
    print("Card statistics have been reset.\n")
    menu(cards)


def lprint(args):
    global log
    log += f"{args.rstrip()}\n"
    print(args)


def linput(args=None):
    global log
    if args:
        log += f"{args.rstrip()}\n"
        return input(args)
    else:
        inp = input()
        log += f"{inp.rstrip()}\n"
        return inp


def menu(cards=None):
    inp = linput("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
    match inp:
        case "add": add(cards)
        case "remove": remove(cards)
        case "import": importcards(cards)
        case "export": exportcards(cards)
        case "ask": ask(cards)
        case "log": dumplog(cards)
        case "hardest card": hard(cards)
        case "reset stats": reset(cards)
        case "exit":
            lprint("Bye bye!")
            exit()
        case _:
            menu(cards)


def add(cards: dict):
    lprint(f"The card:")
    while True:
        term = linput()
        if term in cards.keys():
            lprint(f"The card \"{term}\" already exists. Try again")
            continue
        break

    lprint(f"The definition of the card:")
    while True:
        defin = linput()
        if defin in cards.values():
            lprint(f"The definition \"{defin}\" already exists. Try again:")
            continue
        else:
            cards[term] = defin
            lprint(f"The pair (\"{term}\":\"{defin}\") has been added.\n")
            menu(cards)
            break


def remove(cards: dict):
    toremove = linput("Which card?\n")
    for k, v in cards.items():
        if k == toremove or v == toremove:
            del cards[k]
            lprint("The card has been removed.\n")
            menu(cards)
    lprint(f"Can't remove \"{toremove}\": there is no such card.\n")
    menu(cards)


def importcards(cards: dict):
    fname = linput("File name:\n")
    try:
        with open(fname, 'r') as j:
            temp = json.load(j)
            cards.update(temp)
            lprint(f"{len(temp)} cards have been loaded.\n")
    except FileNotFoundError:
        lprint("File not found.\n")
    menu(cards)


def exportcards(cards: dict):
    fname = linput("File name:\n")
    with open(fname, 'a+') as j:
        json.dump(cards, j)
        lprint(f"{len(cards)} cards have been saved.\n")
    menu(cards)


def ask(cards: dict):
    global hardest
    inp = int(linput("How many times to ask?\n"))

    for _ in range(inp):
        card = random.choice(list(cards.keys()))

        defin = linput(f"Print the definition of \"{card}\"\n")
        if defin == cards[card]:
            lprint("Correct!")
        elif defin in cards.values():
            if card in hardest.keys():
                hardest[card] += 1
            else:
                hardest[card] = 1
            answer = list(cards.keys())[list(cards.values()).index(defin)]
            lprint(f"Wrong. The right answer is \"{cards[card]}\", "
                   f"but your definition is correct for \"{answer}\"")
        else:
            if card in hardest.keys():
                hardest[card] += 1
            else:
                hardest[card] = 1
            lprint(f"Wrong. The right answer is \"{cards[card]}\"")

    print()
    menu(cards)


menu({})
