'''
Description
Our users cannot create new flashcards all the time. It seems like a good idea to keep old but useful cards in storage so we can use them later. Let's try to do that!

In this stage, you will improve the application's interactivity by having it ask the user for action and perform it. You will also provide additional functionality, allowing the user to store flashcards in files for future use.

The program should support the following actions:

add a card: add
remove a card: remove
load cards from file: import
save cards to file: export
ask for definitions of some random cards: ask
exit the program: exit
You can store cards in a file in any format; tests do not check the content of the file, but they do check that the saved flashcards are loaded correctly.

When you load flashcards from a file, you shouldn't erase the cards that aren't in the file. If the imported flashcard already exists, update its definition in the program memory. There won't be any conflict with definitions in the tests.

Objectives
Print the message Input the action (add, remove, import, export, ask, exit): each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.

The program's behavior depends on the action the user inputs:

add — create a new flashcard with a unique term and definition. After adding the card, output the message The pair ("term":"definition") has been added, where "term" is the term entered by the user and "definition" is the definition entered by the user. If a term or a definition already exists, output the line This <term/definition> already exists. Try again: and accept a new term or definition.
remove — ask the user for the term of the card they want to remove with the message Which card?, and read the user's input from the next line. If a matching flashcard exists, remove it from the set and output the message The card has been removed.. If there is no such flashcard in the set, output the message Can't remove "card": there is no such card., where "card" is the user's input.
import — print the line File name:, read the user's input from the next line, which is the file name, and import all the flashcards written to this file. If there is no file with such name, print the message File not found.. After importing the cards, print the message n cards have been loaded., where n is the number of cards in the file. The imported cards should be added to the ones that already exist in the memory of the program. However, the imported cards have priority: if you import a card with the name that already exists in the memory, the card from the file should overwrite the one in memory.
export — request the file name with the line File name: and write all currently available flashcards into this file. Print the message n cards have been saved., where n is the number of cards exported to the file.
ask — ask the user about the number of cards they want and then prompt them for definitions, like in the previous stage.
exit — print Bye bye! and finish the program.
Examples
The symbol > represents the user input. Note that it's not part of the input.

Example 1: the user removes an existing card and tries to remove a non-existent one.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> France
The definition of the card:
> Paris
The pair ("France":"Paris") has been added.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> France
The card "France" already exists. Try again:
> Great Britain
The definition of the card:
> Paris
The definition "Paris" already exists. Try again:
> London
The pair ("Great Britain":"London") has been added.

Input the action (add, remove, import, export, ask, exit):
> remove
Which card?
> France
The card has been removed.

Input the action (add, remove, import, export, ask, exit):
> remove
Which card?
> Wakanda
Can't remove "Wakanda": there is no such card.

Input the action (add, remove, import, export, ask, exit):
> exit
Bye bye!
Example 2: the user uses files to import and export their flashcards; definitions of existing cards are updated after import

Input the action (add, remove, import, export, ask, exit):
> import
File name:
> ghost_file.txt
File not found.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> Japan
The definition of the card:
> Tokyo
The pair ("Japan":"Tokyo") has been added.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> Russia
The definition of the card:
> UpdateMeFromFile
The pair ("Russia":"UpdateMeFromFile") has been added.

Input the action (add, remove, import, export, ask, exit):
> import
File name:
> capitals.txt
28 cards have been loaded.

Input the action (add, remove, import, export, ask, exit):
> ask
How many times to ask?
> 1
Print the definition of "Russia":
> Moscow
Correct!

Input the action (add, remove, import, export, ask, exit):
> export
File name:
> capitalsNew.txt
29 cards have been saved.

Input the action (add, remove, import, export, ask, exit):
> exit
Bye bye!
Example 3: the program asks for definitions several times

Input the action (add, remove, import, export, ask, exit):
> add
The card
> a brother of one's parent
The definition of the card
> uncle
The pair ("a brother of one's parent":"uncle") has been added.

Input the action (add, remove, import, export, ask, exit):
> add
The card
> a part of the body where the foot and the leg meet
The definition of the card
> ankle
The pair ("a part of the body where the foot and the leg meet":"ankle") has been added.

Input the action (add, remove, import, export, ask, exit):
> ask
How many times to ask?
> 6
Print the definition of "a brother of one's parent":
> ankle
Wrong. The right answer is "uncle", but your definition is correct for "a part of the body where the foot and the leg meet".
Print the definition of "a part of the body where the foot and the leg meet":
> ??
Wrong. The right answer is "ankle".
Print the definition of "a brother of one's parent":
> uncle
Correct!
Print the definition of "a part of the body where the foot and the leg meet":
> ankle
Correct!
Print the definition of "a brother of one's parent":
> ??
Wrong. The right answer is "uncle".
Print the definition of "a part of the body where the foot and the leg meet":
> uncle
Wrong. The right answer is "ankle", but your definition is correct for "a brother of one's parent".

Input the action (add, remove, import, export, ask, exit):
> exit
Bye bye!
Note that all your outputs and user inputs should be on separate lines.
'''
import json
import os.path


def add_flashcard():
    global flashcards, inv_flashcards, hist_flashcards
    term = input(f"The card:\n")
    while term in flashcards.keys():
        term = input(f'This {term} already exists. Try again::\n')

    definition = input(f"The definition of the card:\n")
    while definition in flashcards.values():
        definition = input(f'This {definition} already exists. Try again::\n')

    flashcards[term], inv_flashcards[definition], hist_flashcards[term] = definition, term, definition
    flash_print('add', (term, definition))


def removed_flashcard():
    global flashcards, inv_flashcards

    remove_card = input('Which card?\n')
    if flashcards.get(remove_card, None) is not None:
        inv_flashcards.pop(flashcards[remove_card])
        flashcards.pop(remove_card)
        flash_print('remove', remove_card)
    else:
        print(f'''Can't remove "{remove_card}": there is no such card.''')


def import_flashcard():
    global flashcards, inv_flashcards, hist_flashcards

    file_name = input('File name:\n')
    if os.path.isfile(file_name):
        with open(file_name, 'r') as import_file:
            json_read = json.load(import_file)
            for qty, term in enumerate(json_read['flashcards']):
                flashcards[term] = json_read['flashcards'][term]
                inv_flashcards[json_read['flashcards'][term]] = term
                hist_flashcards[term] = json_read['flashcards'][term]
            flash_print('import', qty + 1)
    else:
        print('File not found.')


def export_flashcard():
    global flashcards, inv_flashcards, hist_flashcards

    file_name = input('File name:\n')
    export_dict = {'flashcards': flashcards, 'inv_flashcards': inv_flashcards, 'hist_flashcards': hist_flashcards}
    with open(file_name, 'w') as export_file:
        json.dump(export_dict, export_file, indent=6)

    flash_print('export', len(flashcards.keys()))


def ask_flashcard():
    global flashcards, inv_flashcards
    times, n = int(input('How many times to ask?\n')), 0

    while n != times:
        for j in flashcards:
            print(f'Print the definition of "{j}":')
            answer = input()

            if answer == flashcards[j]:
                print('Correct!')
            elif answer in flashcards.values():
                print(f'Wrong. The right answer is "{flashcards[j]}"', end=' ')
                print(f'but your definition is correct for "{inv_flashcards[answer]}".')
            else:
                print(f'Wrong. The right answer is "{flashcards[j]}".')

            n += 1
            if n == times:
                break


def flash_print(form, data, text='null'):
    if form in ['add']:
        text = f'The pair ("{data[0]}":"{data[1]}") has been added.\n'
    elif form in ['remove']:
        text = f'The card has been removed.\n'
    elif form in ['exit']:
        text = data
    elif form in ['import', 'export']:
        output = 'loaded' if form == 'import' else 'saved'
        text = f'{data} cards have been {output}.'
    print(text)


flashcards, inv_flashcards, hist_flashcards = {}, {}, {}

while True:
    action = input("Input the action (add, remove, import, export, ask, exit):\n")

    if action == 'add':
        add_flashcard()
    elif action == 'remove':
        removed_flashcard()
    elif action == 'import':
        import_flashcard()
    elif action == 'export':
        export_flashcard()
    elif action == 'ask':
        ask_flashcard()
    elif action == 'exit':
        flash_print('exit', 'Bye bye!')
        exit()
        
\\

import json
import os
import random
from pathlib import Path


class FlashCard:
    def __init__(self):
        self.cards = []

    def run(self):
        self.menu()

    def menu(self):
        while True:
            print("Input the action (add, remove, import, export, ask, exit):")
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
            elif action == "exit":
                print("Bye bye!")
                exit(0)

    def add(self):
        print(f"The card:")
        while True:
            term = input()
            if term in Card.terms:
                print(f'The term "{term}" already exists. Try again:')
                continue
            else:
                break
        print(f"The definition of the card:")
        while True:
            definition = input()
            if definition in Card.definitions:
                print(f'The definition "{definition}" already exists. Try again:')
                continue
            else:
                break
        new_card = Card(term, definition)
        self.cards.append(new_card)
        print(f'The pair ("{term}":"{definition}") has been added.')

    def remove(self):
        print("Which card?")
        term = input()
        card = self.get_by_term(term)
        if card:
            self.cards.remove(card)
            print("The card has been removed.")
        else:
            print(f'''Can't remove "{term}": there is no such card.''')

    def import_cards(self):
        print("File name:")
        file_name = input()
        file = Path(os.path.join(os.path.curdir, file_name))
        if file.exists():
            with open(file, "r") as f:
                new_cards: dict = json.loads(f.read())
                new_cards: list = [Card(x, new_cards[x]) for x in new_cards]
                self.cards += new_cards
                print(f"{len(new_cards)} cards have been loaded.")
        else:
            print("File not found.")

    def export_cards(self):
        print("File name:")
        file_name = input()
        file = Path(os.path.join(os.path.curdir, file_name))
        with open(file, "w") as f:
            f.write(json.dumps({x.term: x.definition for x in self.cards}))
            print(f"{len(self.cards)} cards have been saved.")

    def ask(self):
        print("How many times to ask?")
        times = int(input())
        for _ in range(times):
            card = random.choice(self.cards)
            print(f'Print the definition of "{card.term}":')
            definition = input()
            if definition == card.definition:
                print("Correct!")
            else:
                if definition in Card.definitions:
                    true_card = self.get_by_definition(definition)
                    print(
                        f'Wrong. The right answer is "{card.definition}".but your definition is correct for "{true_card.term}".')
                else:
                    print(f'Wrong. The right answer is "{card.definition}".')

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

    def __new__(cls, term, definition, *args, **kwargs):
        cls.terms.append(term)
        cls.definitions.append(definition)
        return super().__new__(cls)




if __name__ == "__main__":
    app = FlashCard()
    app.run()
flashcards/a.txt


{"a": "1", "b": "2", "c": "3"}


