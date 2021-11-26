'''
Description
While learning new things, we may mix things up and use the right definition for the wrong term. Let's inform our players if they enter the definition that is wrong for the requested flashcard but correct for another flashcard in our set.

Also, it might be very confusing if our flashcard set contains cards with the same term or definition, since seeing only one side of the card we can't tell them apart. Let's add a constraint: the user must add only unique terms and definitions. To do this, you need to find a way to check whether the set contains a particular term or definition and get the term by the definition, and vice versa.

These two features will definitely improve our game!

Objectives
Modify your program and add the following functionalities:

When the user tries to add a duplicate term, forbid it and output the message The term "term" already exists. Try again: using the term instead of "term". Ask for the term until the user inputs a unique term.
When the user tries to add a duplicate definition, forbid it and Output the message The definition "definition" already exists. Try again: with the definition instead of "definition". Ask the player to input the definition until the user inputs a unique one.
When the user enters the wrong definition for the requested term, but this definition is correct for another term, print the appropriate message: Wrong. The right answer is "correct answer", but your definition is correct for "term for user's answer". , where "correct answer" is the actual definition for the requested term, and "term for user's answer" is the appropriate term for the user-entered definition.
Examples
The symbol > represents the user input. Note that it's not part of the input.

Example 1: the user tries to add duplicated term and definition

Input the number of cards:
> 2
The term for card #1:
> print()
The definition for card #1:
> outputs text
The term for card #2:
> print()
The term "print()" already exists. Try again:
> str()
The definition for card #2:
> outputs text
The definition "outputs text" already exists. Try again:
> converts to a string
Print the definition of "print()":
> outputs text
Correct!
Print the definition of "str()":
> converts to a string
Correct!
Example 2: the user gives a correct definition for a term that exists, but which is not the term that the program is asking about

Input the number of cards:
> 2
The term for card #1:
> uncle
The definition for card #1:
> a brother of one's parent
The term for card #2:
> ankle
The definition for card #2:
> a part of the body where the foot and the leg meet
Print the definition of "uncle":
> a part of the body where the foot and the leg meet
Wrong. The right answer is "a brother of one's parent", but your definition is correct for "ankle".
Print the definition of "ankle":
> ???
Wrong. The right answer is "a part of the body where the foot and the leg meet".
Note that all your outputs and user inputs should be on separate lines.


'''
number_cards, flashcards, inverse_flashcards = int(input("Input the number of cards:\n")), {}, {}

for i in range(number_cards):
    term = input(f"The term for card #{i + 1}:\n")
    while term in flashcards.keys():
        term = input(f'The term "{term}" already exists. Try again:\n')

    definition = input(f"The definition for card #{i + 1}:\n")
    while definition in flashcards.values():
        definition = input(f'The definition "{definition}" already exists. Try again:\n')

    flashcards[term], inverse_flashcards[definition] = definition, term

for j in flashcards:
    print(f'Print the definition of "{j}":')
    answer = input()
    if answer == flashcards[j]:
        print('Correct!')
    elif answer in flashcards.values():
        print(f'Wrong. The right answer is "{flashcards[j]}"', end=' ')
        print(f'but your definition is correct for "{inverse_flashcards[answer]}".')
    else:
        print(f'Wrong. The right answer is "{flashcards[j]}".')
\\

# Write your code here
class Program:
    def __init__(self):
        self.cards = []

    def run(self):
        self.init()
        self.guess()
        
    def init(self):
        print("Input the number of cards:")
        number = int(input())
        count = 1
        while count <= number:
            print(f"The term for card #{count}:")
            while True:
                term = input()
                if term in Card.terms:
                    print(f'The term "{term}" already exists. Try again:')
                    continue
                else:
                    break
            print(f"The definition for card #{count}:")
            while True:
                definition = input()
                if definition in Card.definitions:
                    print(f'The definition "{definition}" already exists. Try again:')
                    continue
                else:
                    break
            new_card = Card(term, definition)
            self.cards.append(new_card)
            count += 1

    def guess(self):
        for card in self.cards:
            print(f'Print the definition of "{card.term}":')
            definition = input()
            if definition == card.definition:
                print("Correct!")
            else:
                if definition in Card.definitions:
                    true_card = Card.get(definition)
                    print(f'Wrong. The right answer is "{card.definition}".but your definition is correct for "{true_card.term}".')
                else:
                    print(f'Wrong. The right answer is "{card.definition}".')


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

    @classmethod
    def get(cls, given_definition):
        for idx, definition in enumerate(cls.definitions):
            if definition == given_definition:
                return cls(cls.terms[idx], cls.definitions[idx])


if __name__ == "__main__":
    app = Program()
    app.run()
\\
cards = {}

for i in range(int(input("Input the number of cards:\n"))):
    print(f"The term for card #{i + 1}:")
    while True:
        term = input()
        if term in cards.keys():
            print(f"The term \"{term}\" already exists. Try again")
            continue
        break

    print(f"The definition for card #{i + 1}:")
    while True:
        defin = input()
        if defin in cards.values():
            print(f"The definition \"{defin}\" already exists. Try again:")
            continue
        else:
            cards[term] = defin
            break

for card in cards:
    defin = input(f"Print the definition of \"{card}\"\n")
    if defin == cards[card]:
        print("Correct!")
    elif defin in cards.values():
        answer = list(cards.keys())[list(cards.values()).index(defin)]
        print(f"Wrong. The right answer is \"{cards[card]}\", "
              f"but your definition is correct for \"{answer}\"")
    else:
        print(f"Wrong. The right answer is \"{cards[card]}\"")
