'''
Description
Let's simulate an actual coffee machine! What do we need for that? This coffee machine will have a limited supply of water, milk, coffee beans, and disposable cups. Also, it will calculate how much money it gets for selling coffee.

There are several options for the coffee machine we want you to implement: first, it should sell coffee. It can make different types of coffee: espresso, latte, and cappuccino. Of course, each variety requires a different amount of supplies, however, in any case, you will need only one disposable cup for a drink. Second, the coffee machine must get replenished by a special worker. Third, another special worker should be able to take out money from the coffee machine.

Objectives
Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program is supposed to do one of the mentioned actions at a time. It should also calculate the amounts of remaining ingredients and how much money is left. Display the quantity of supplies before and after purchase.

First, your program reads one option from the standard input, which can be "buy", "fill", "take". If a user wants to buy some coffee, the input is "buy". If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be "fill". If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input "take".
If the user writes "buy" then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.
For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
If the user writes "fill", the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.
If the user writes "take" the program should give all the money that it earned from selling coffee.
At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.

To sum up, your program should print the coffee machine's state, process one query from the user, as well as print the coffee machine's state after that. Try to use functions for implementing every action that the coffee machine can do.
Examples
An espresso should be number 1 in the list, a latte number 2, and a cappuccino number 3.
Options are named as "buy", "fill", "take".

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money

Write action (buy, fill, take):
> buy
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:
> 3

The coffee machine has:
200 of water
440 of milk
108 of coffee beans
8 of disposable cups
556 of money
Example 2:

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money

Write action (buy, fill, take):
> fill
Write how many ml of water you want to add:
> 2000
Write how many ml of milk you want to add:
> 500
Write how many grams of coffee beans you want to add:
> 100
Write how many disposable coffee cups you want to add:
> 10

The coffee machine has:
2400 of water
1040 of milk
220 of coffee beans
19 of disposable cups
550 of money
Example 3:

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money

Write action (buy, fill, take):
> take
I gave you $550

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
0 of money

'''
print('''The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
''')

water_stack = 400
milk_stack = 540
beans_stack = 120
cups_stack = 9
money_stack = 550
      
def buy(coffee_type):
    global water_stack, milk_stack, beans_stack, cups_stack, money_stack
    if coffee_type == 1:
        water_stack = water_stack - 250
        beans_stack = beans_stack - 16
        cups_stack = cups_stack - 1
        money_stack = money_stack + 4
    elif coffee_type == 2:
        water_stack = water_stack - 350
        milk_stack =  milk_stack - 75
        beans_stack = beans_stack - 20
        cups_stack = cups_stack - 1
        money_stack = money_stack + 7
    elif coffee_type == 3:
        water_stack = water_stack - 200
        milk_stack =  milk_stack - 100
        beans_stack = beans_stack - 12
        cups_stack = cups_stack - 1
        money_stack = money_stack + 6

def fill(water, milk, beans, cup):
    global water_stack, milk_stack, beans_stack, cups_stack, money_stack
    water_stack += water
    milk_stack += milk
    beans_stack += beans
    cups_stack += cup

def take(money):
    global money_stack
    money_stack = money_stack - money


print("Write action (buy, fill, take): ")
action = str(input())
if action == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    coffee_type = int(input())
    buy(coffee_type)  
elif action == "fill":
    water = int(input("Write how many ml of water you want to add: "))
    milk = int(input("Write how many ml of milk you want to add: "))
    beans = int(input("Write how many grams of coffee beans you want to add: "))
    cup = int(input("Write how many disposable coffee cups you want to add: "))
    fill(water, milk, beans, cup)
elif action == "take":
    print("I gave you $")
    money = 550
    take(money)

print()
print(f'''The coffee machine has:
{water_stack} of water
{milk_stack} of milk
{beans_stack} of coffee beans
{cups_stack} of disposable cups
{money_stack} of money
''')


\\


class CoffeeMachine:

    def __init__(self):
        self.products = ['espresso', 'latte', 'cappuccino']
        self.water_vol = 400
        self.milk_vol = 540
        self.beans_wei = 120
        self.number_of_cups = 9
        self.bank = 550

    def state(self):
        print("The coffee machine has:\n")
        print(f"{self.water_vol} of water")
        print(f"{self.milk_vol} of milk")
        print(f"{self.beans_wei} of coffee beans")
        print(f"{self.number_of_cups} of disposable cups")
        print(f"{self.bank} of money\n")

    def action(self):
        return input("Write action (buy, fill, take):\n")

    def action_buy(self):
        select_drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if select_drink == '1':
            self.water_vol -= 250
            self.milk_vol -= 0
            self.beans_wei -= 16
            self.number_of_cups -= 1
            self.bank += 4
        elif select_drink == '2':
            self.water_vol -= 350
            self.milk_vol -= 75
            self.beans_wei -= 20
            self.number_of_cups -= 1
            self.bank += 7
        elif select_drink == '3':
            self.water_vol -= 200
            self.milk_vol -= 100
            self.beans_wei -= 12
            self.number_of_cups -= 1
            self.bank += 6

    def action_fill(self):
        self.water_vol += int(input("Write how many ml of water you want to add:\n"))
        self.milk_vol += int(input("Write how many ml of milk you want to add:\n"))
        self.beans_wei += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.number_of_cups += int(input("Write how many disposable coffee cups you want to add:\n"))

    def action_take(self):
        print(f"I take you ${self.bank}")
        self.bank = 0


my_coffee_machine = CoffeeMachine()

my_coffee_machine.state()
action = my_coffee_machine.action()
if action == 'buy':
    my_coffee_machine.action_buy()
elif action == 'fill':
    my_coffee_machine.action_fill()
elif action == 'take':
    my_coffee_machine.action_take()
my_coffee_machine.state()

\\

from collections import namedtuple
from dataclasses import dataclass

Ingredient = namedtuple('Ingredient', 'name amount')


class Error(Exception):
    """
    Base Error class for coffee_machine module.
    """


class MissingIngredientsError(Error):
    """
    Raised when there are not enough ingredients to fulfill the order.
    """


@dataclass
class Coffee:
    name: str
    price: int
    recipe: list[Ingredient]


class CoffeeMachine:
    """
    Class representing a coffee machine.
    """
    MENU = [
        Coffee('espresso', 4, [Ingredient('water', 250),
                               Ingredient('beans', 16)]),

        Coffee('latte', 7, [Ingredient('water', 350),
                            Ingredient('milk', 75),
                            Ingredient('beans', 20)]),

        Coffee('cappuccino', 6, [Ingredient('water', 200),
                                 Ingredient('milk', 100),
                                 Ingredient('beans', 12)])
    ]

    UNITS = {'water': 'ml', 'milk': 'ml', 'beans': 'g'}

    def __init__(self, *, water: int = 0, milk: int = 0, beans: int = 0,
                 cups: int = 0, money: int = 0.0, ) -> None:
        """
        Initialize a coffee machine instance.

        :param water: amount of water in ml, default is 0
        :param milk: amount of milk in ml, default is 0
        :param beans: amount of beans in ml, default is 0
        :param cups: number of disposable cups, default is 0
        :param money: amount of money in dollars and cents, default is 0.0
        """
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def fill(self, *, water: int = 0, milk: int = 0, beans: int = 0,
             cups: int = 0, money: int = 0, ) -> None:
        """
        Adds or subtract items from the machine if possible.

        :param water: amount of water in ml, default is 0
        :param milk: amount of milk in ml, default is 0
        :param beans: amount of beans in ml, default is 0
        :param cups: number of disposable cups, default is 0
        :param money: amount of money in dollars, default is 0
        :raises MissingIngredientError: if the result of the operation would
                be negative.
        """
        for attr, value in locals().items():
            if attr == 'self':
                continue
            result = getattr(self, attr) + value
            if result < 0:
                raise MissingIngredientsError
            else:
                setattr(self, attr, result)

    def get_money(self, verbose: bool = True) -> int:
        """
        Returns the available money and resets the money attribute to 0.

        :verbose: if True, a message is printed that the money was dispensed;
                 default is True
        :return: the value of money attribute
        """
        money = self.money
        self.money = 0
        if verbose:
            print(f'I gave you ${money}.')
        return money

    def buy(self, coffee_index: int) -> None:
        """
        Process the purchase operation, that is, remove ingredients and add
        money to the machine.

        :param coffee_index: the index in the MENU of the coffee being bought
        """
        coffee = self.MENU[coffee_index]
        fill_kwargs = {ingredient.name: -ingredient.amount
                       for ingredient in coffee.recipe}
        fill_kwargs.update({'cups': -1, 'money': coffee.price})
        self.fill(**fill_kwargs)

    def report(self) -> None:
        """
        Prints the coffee's machine state.
        """
        full_names = {'beans': 'coffee beans', 'cups': 'disposable cups'}
        print('The coffee machine has:')
        for attr, value in vars(self).items():
            print(f'{value} of {full_names.get(attr, attr)}')

    @staticmethod
    def read_option() -> str:
        """
        Reads one option from the standard input.

        :return: the chosen option ('buy', 'fill', 'take').
        """
        print('Write action (buy, fill, take):')
        while True:
            option = input()
            if option in ('buy', 'fill', 'take'):
                return option

    def read_coffee_type(self) -> int:
        """
        Reads one coffee type to buy from standard input.

        :return: the chosen the index in MENU of the chose coffee type
        """
        print('What do you want to buy?', end=' ')
        coffee_list = ', '.join(
            f'{n} - {coffee.name}' for n, coffee in enumerate(self.MENU, 1)
        )
        print(f'{coffee_list}:')

        while True:
            input_ = input()
            try:
                return int(input_) - 1
            except ValueError:
                continue

    def read_and_buy(self) -> None:
        """
        Reads one coffee type to buy from standard input and process the
        purchase operation.
        """
        self.buy(self.read_coffee_type())

    def read_fill_value(self, attr: str) -> int:
        """
        Reads the value for attr from the standard input. Runs in a loop until
        non-negative integer is entered. Returns the accepted input.

        :param attr: one of the supplies ('water', 'milk', 'beans', 'cup')
        :return: A non-negative integer representing amount of attr.
        """
        while True:
            if attr == 'cups':
                print('Write how many disposable cups you want to add.')
            else:
                print(
                    (f'Write how many {self.UNITS[attr]}' 
                     f' of {attr} you want to add:')
                )

            try:
                input_ = int(input())
            except ValueError:
                continue
            else:
                if input_ < 0:
                    continue
                else:
                    return input_

    def read_and_fill(self) -> None:
        """
        Reads the values of the machine supplies from the standard input and
        adds the entered amounts to the machine.
        """
        fill_kwargs = {}
        for attr in vars(self):
            if attr == 'money':
                continue
            fill_kwargs[attr] = self.read_fill_value(attr)
        self.fill(**fill_kwargs)


def main():
    machine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)
    machine.report()
    choice = machine.read_option()
    if choice == 'buy':
        machine.read_and_buy()
    elif choice == 'fill':
        machine.read_and_fill()
    else:
        machine.get_money()
    machine.report()


if __name__ == '__main__':
    main()

    
    




