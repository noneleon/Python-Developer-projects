'''
Description
Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. It should repeatedly ask a user what they want to do. If the user types "buy", "fill" or "take", then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, they should type "exit". The program should terminate on this command. Also, when the user types "remaining", the program should output all the resources that the coffee machine has.

Objectives
Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.

Example
Your coffee machine should have the same initial resources as in the example (400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash).

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> fill

Write how many ml of water do you want to add:
> 1000
Write how many ml of milk do you want to add:
> 0
Write how many grams of coffee beans do you want to add:
> 0
Write how many disposable cups of coffee do you want to add:
> 0

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
> take

I gave you $564

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
> exit
'''
money = 550
water = 400
milk = 540
beans = 120
cups = 9


class ResourceError(Exception):
    pass


def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def select_action() -> str:
    return input('Write action (buy, fill, take, remaining, exit): ')


def select_flavor() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)


def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise ResourceError
    print('I have enough resources, making you a coffee!\n')


def buy():
    global money, water, milk, beans, cups

    flavor = select_flavor()

    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            is_enough(need_water=250, need_beans=16)

            money += 4
            water -= 250
            beans -= 16
            cups -= 1
        elif flavor == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)

            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif flavor == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)

            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown flavor {flavor}')
    except ResourceError:
        pass


def fill():
    global water, milk, beans, cups

    print()
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))
    print()


def take():
    global money

    print()
    print(f'I gave you ${money}')
    print()

    money = 0


def main():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')


if __name__ == '__main__':
    main()
    
    
    
\\

from collections import namedtuple
from dataclasses import dataclass
from typing import Union

Ingredient = namedtuple('Ingredient', 'name amount')


class Error(Exception):
    """
    Base Error class for coffee_machine module.
    """


class MissingIngredientsError(Error):
    """
    Raised when there are not enough ingredients to fulfill the order.
    """

    def __init__(self):
        self.missing = None


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
                error = MissingIngredientsError()
                setattr(error, 'missing', attr)
                raise error
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
            print(f'\nI gave you ${money}.')
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
        print('\nThe coffee machine has:')
        for attr, value in vars(self).items():
            print(f'{value} of {full_names.get(attr, attr)}')

    @staticmethod
    def read_option() -> str:
        """
        Reads one option from the standard input.

        :return: the chosen option ('buy', 'fill', 'take',
                                    'remaining', 'exit').
        """
        print('\nWrite action (buy, fill, take, remaining, exit):')
        while True:
            option = input()
            if option in ('buy', 'fill', 'take', 'remaining', 'exit'):
                return option

    def read_coffee_type(self) -> Union[int, None]:
        """
        Reads one coffee type to buy from standard input.

        :return: the chosen the index in MENU of the chose coffee type or None
                 if 'back' is entered
        """
        print('\nWhat do you want to buy?', end=' ')
        coffee_list = ', '.join(
            f'{n} - {coffee.name}' for n, coffee in enumerate(self.MENU, 1)
        )
        print(f'{coffee_list}:')

        while True:
            input_ = input()
            if input_ == 'back':
                return
            try:
                return int(input_) - 1
            except ValueError:
                continue

    def read_and_buy(self) -> None:
        """
        Reads one coffee type to buy from standard input and process the
        purchase operation.
        """
        coffee = self.read_coffee_type()
        if coffee is not None:
            try:
                self.buy(coffee)
            except MissingIngredientsError as E:
                print(f'Sorry, not enough {E.missing}')
            else:
                print('I have enough resources, making you a coffee!')

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
        print('')
        fill_kwargs = {}
        for attr in vars(self):
            if attr == 'money':
                continue
            fill_kwargs[attr] = self.read_fill_value(attr)
        self.fill(**fill_kwargs)


def main():
    machine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)
    while True:
        choice = machine.read_option()
        if choice == 'buy':
            machine.read_and_buy()
        elif choice == 'fill':
            machine.read_and_fill()
        elif choice == 'take':
            machine.get_money()
        elif choice == 'remaining':
            machine.report()
        else:
            return


if __name__ == '__main__':
    main()

    
    
\\

supplies_cups = {}
recipes = {"espresso":
              {"water": 250, "coffee beans": 16, "disposable cups": 1},
          "latte":
              {"water": 350, "milk": 75, "coffee beans": 20, "disposable cups": 1},
          "cappuccino":
              {"water": 200, "milk": 100, "coffee beans": 12, "disposable cups": 1}
          }

supplies = {"water": 400,
            "milk": 540,
            "coffee beans": 120,
            "disposable cups": 9}

units = {"water": "ml", "milk": "ml", "coffee beans": "g",
         "disposable cups": ""}

balance = 550

prices = {"espresso": 4, "latte": 7, "cappuccino": 6}


def report_state():
    global balance, supplies
    print("The coffee machine has:")

    for k, v in supplies.items():
        print("{1} of {0}".format(k, v))

    print("{0} of money".format(balance))


def is_enough_supplies(recipe):
    global recipes, supplies
    result = [True]

    for ingredient_name, ingredient_quantity in recipes[recipe].items():
        if supplies[ingredient_name] - ingredient_quantity <= 0:
            result[0] = False
            result.append(ingredient_name)
            break

    return result


def buy():
    global recipes, balance, supplies

    choice = input("What do you want to buy?"
                   "1 - espresso, 2 - latte, 3 - cappuccino, "
                   "back - to main menu:").strip()

    if choice == "1":
        choice = "espresso"
    elif choice == "2":
        choice = "latte"
    elif choice == "3":
        choice = "cappuccino"
    elif choice == "back":
        return

    ies = is_enough_supplies(choice)

    if ies[0]:
        print("I have enough resources, making you a coffee!")
        balance += prices[choice]

        for ingredient_name, ingredient_quantity in recipes[choice].items():
            supplies[ingredient_name] -= ingredient_quantity
    else:
        print("Sorry, not enough {0}!".format(ies[1]))


def fill():
    global supplies
    for k, v in supplies.items():
        if units[k] == "g":
            unit = "grams"
        else:
            unit = units[k]

        if k == "disposable cups":
            supply_name = "disposable coffee cups"
        else:
            supply_name = k

        print("Write how many {0}{2}{1} you want to add:"
              .format(unit, supply_name,
                      "" if supply_name == "disposable coffee cups" else " of "))

        supplies[k] += int(input())


def take():
    global balance
    balance -= balance
    print("I gave you ${}".format(balance))


def main():
    command = ""
    while command != "exit":
        command = input("Write action (buy, fill, take, remaining, exit):\n").strip()

        if command == "buy":
            buy()
        elif command == "fill":
            fill()
        elif command == "take":
            take()
        elif command == "remaining":
            report_state()
        elif command == "exit":
            break
        else:
            print("This should have never happened.")


if __name__ == "__main__":
    main()

    
\\

water = 400
milk = 540
cof_b = 120
cups = 9
money = 550


def storage(w_u, m_u, c_u, cup, mon):
    global water
    global milk
    global cof_b
    global cups
    global money
    water -= w_u
    milk -= m_u
    cof_b -= c_u
    cups -= cup
    money -= mon
    return water, milk, cof_b, cups, money


def check(water_n, milk_n, cof_n, cups_n):
    xs = [storage(0, 0, 0, 0, 0)]
    if xs[0][0] - water_n < 0:
        print('Sorry, not enough water!')
        return False
    elif xs[0][1] - milk_n < 0:
        print('Sorry, not enough milk')
        return False
    elif xs[0][2] - cof_n < 0:
        print('Sorry, not enough coffee bean')
        return False
    elif xs[0][3] - cups_n < 0:
        print('Sorry, not enough cups')
        return False
    else:
        print('I do coffee')
        return True


def buy(cof):
    if cof == 1:  # espresso
        es = check(250, 0, 16, 1)
        if es is True:
            storage(250, 0, 16, 1, -4)
        else: return
    elif cof == 2:  # latte
        la = check(350, 75, 20, 1)
        if la is True:
            storage(350, 75, 20, 1, -7)
        else: return
    elif cof == 3:  # cappuccino
        ca = check(200, 100, 12, 1)
        if ca is True:
            storage(200, 100, 12, 1, -6)
        else: return


def fill():
    water_a = -(int(input('Write how many ml of water do you want to add: ')))
    milk_a = -(int(input('Write how many ml of milk do you want to add: ')))
    coff_a = -(int(input('Write how many grams of coffee beans do you want to add: ')))
    cups_a = -(int(input('Write how many disposable cups of coffee do you want to add: ')))
    storage(water_a, milk_a, coff_a, cups_a, 0)


def take():
    xs = [storage(0, 0, 0, 0, 0)]
    print("I gave you", '$' + str(xs[0][4]))
    storage(0, 0, 0, 0, (xs[0][4]))


def remaining():
    xs = [storage(0, 0, 0, 0, 0)]
    print('The coffee machine has:')
    print(xs[0][0], ' of water')
    print(xs[0][1], ' of milk')
    print(xs[0][2], ' of coffee beans')
    print(xs[0][3], ' of disposable cups')
    print('$' + str(xs[0][4]), ' of money')
    return xs


def main():
    while True:
        user = input('Write action (buy, fill, take, remaining, exit): ')
        if 'buy' in user:
            coffee_c = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: '))
            if 'back' in coffee_c:
                remaining()
                return
            else:
                buy(int(coffee_c))
        elif 'fill' in user:
            fill()
        elif 'take' in user:
            take()
        elif 'remaining' in user:
            remaining()
        else:
            break
main()




