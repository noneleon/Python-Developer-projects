'''Description
Let's redesign our program and write a class that represents a coffee machine. The class should have a method that takes a string as input. Every time the user inputs a string to the console, the program invokes this method with one argument: the line that the user inputs to the console. This system simulates pretty accurately how real-world electronic devices work. External components (like buttons on the coffee machine or tapping on the screen) generate events that pass into the single interface of the program.

The class should not use system input at all; it will only handle the input that comes to it via this method and its string argument.

The first problem that comes to mind: how to write that method in a way that it represents all that coffee machine can do? If the user inputs a single number, how can the method determine what that number is: a variant of coffee chosen by the user or the number of the disposable cups that a special worker added into the coffee machine?

The right solution to this problem is to store the current state of the machine. The coffee machine has several states it can be in. For example, the state could be "choosing an action" or "choosing a type of coffee". Every time the user inputs something and a program passes that line to the method, the program determines how to interpret this line using the information about the current state. After processing this line, the state of the coffee machine can be changed or can stay the same.

Objective
Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method.

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
$0 of money

Write action (buy, fill, take, remaining, exit):
> exit'''

class CoffeMachine:
    n_machines = 0

    def __new__(cls, *args, **kwargs):
        cls.n_machines += 1
        return object.__new__(cls)

    def __init__(self):
        self.waterMl = 400
        self.milkMl = 540
        self.coffeeBeansGr = 120
        self.amountOfMoney = 550
        self.disposableCups = 9

    def users_action(self):
        users_action = str(input("Write action (buy, fill, take, remaining, exit):\n"))
        if users_action == "buy":
            users_action = (
                input("What do you want to buy? 1 - espresso, "
                      "2 - latte, "
                      "3 - cappuccino, "
                      "back - to main menu:\n"))
            self.buy_coffee(users_action)
            # inputed_action = ""
        elif users_action == "fill":
            add_list =[0,0,0,0]
            info_list = ["Write how many ml of water do you want to add:",
                         "Write how many ml of milk do you want to add:",
                         "Write how many grams of coffee beans do you want to add:",
                         "Write how many disposable cups of coffee do you want to add"
                         ]
            for i in range(4):
                print(info_list[i])
                add_list[i]=int(input())
            self.fill_resourses(add_list)
        elif users_action == "take":
            self.take_money()
        elif users_action == "remaining":
            self.print_info()
        elif users_action == "exit":
            exit()

    def buy_coffee(self, users_choice):
        if users_choice == "1":  # espresso
            if (self.waterMl < 250):
                print("Sorry, not enough water!\n")
                self.users_action()
            elif (self.coffeeBeansGr < 16):
                print("Sorry, not enough coffee beans!\n")
                self.users_action()
            elif (self.disposableCups == 0):
                print("Sorry, not enough disposable cups!\n")
                self.users_action()
            else:
                self.waterMl -= 250
                self.coffeeBeansGr -= 16
                self.amountOfMoney += 4
                self.disposableCups -= 1
                print("I have enough resources, making you a coffee!\n")
                self.users_action()

        elif users_choice == "2":  # latte
            if (self.waterMl < 350):
                print("Sorry, not enough water!\n")
                self.users_action()
            elif (self.milkMl < 75):
                print("Sorry, not enough milk!\n")
                self.users_action()
            elif (self.coffeeBeansGr < 20):
                print("Sorry, not enough coffee beans!\n")
                self.users_action()
            elif (self.disposableCups == 0):
                print("Sorry, not enough disposable cups!\n")
                self.users_action()
            else:
                self.waterMl -= 350
                self.milkMl -= 75
                self.coffeeBeansGr -= 20
                self.amountOfMoney += 7
                self.disposableCups -= 1
                print("I have enough resources, making you a coffee!\n")
                self.users_action()

        elif users_choice == "3":  # cappuccino
            if (self.waterMl < 200):
                print("Sorry, not enough water!\n")
                self.users_action()
            elif (self.milkMl < 100):
                print("Sorry, not enough milk!\n")
                self.users_action()
            elif (self.coffeeBeansGr < 12):
                print("Sorry, not enough coffee beans!\n")
                self.users_action()
            elif (self.disposableCups == 0):
                print("Sorry, not enough disposable cups!\n")
                self.users_action()
            else:
                self.waterMl -= 200
                self.milkMl -= 100
                self.coffeeBeansGr -= 12
                self.amountOfMoney += 6
                self.disposableCups -= 1
                print("I have enough resources, making you a coffee!\n")
                self.users_action()
        else:
            self.users_action()

    def fill_resourses(self,added):
        self.waterMl+=added[0]
        self.milkMl += added[1]
        self.coffeeBeansGr += added[2]
        self.disposableCups += added[3]
        self.users_action()

    def print_info(self):
        print(f"The coffee machine has:\n"
              f"{self.waterMl} of water\n"
              f"{self.milkMl} of milk\n"
              f"{self.coffeeBeansGr} of coffee beans\n"
              f"{self.disposableCups} of disposable cups\n"
              f"{self.amountOfMoney} of money\n")
        self.users_action()

    def take_money(self):
        print(f"I gave you ${self.amountOfMoney}")
        self.amountOfMoney = 0
        self.users_action()

CoffeAutomat = CoffeMachine()
CoffeAutomat.users_action()



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
    Raised when there are not enough ingredients to perform an action.
    """

    def __init__(self):
        self.missing = None


@dataclass
class Coffee:
    """
    Dataclass representing a coffee drink.
    """
    name: str
    recipe: list[Ingredient]


class CoffeeMachine:
    """
    Class representing a coffee machine.
    """
    MENU = [
        Coffee('espresso', [Ingredient('water', 250),
                            Ingredient('beans', 16),
                            Ingredient('cups', 1),
                            Ingredient('money', -4)]),

        Coffee('latte', [Ingredient('water', 350),
                         Ingredient('milk', 75),
                         Ingredient('beans', 20),
                         Ingredient('cups', 1),
                         Ingredient('money', -7)]),

        Coffee('cappuccino', [Ingredient('water', 200),
                              Ingredient('milk', 100),
                              Ingredient('beans', 12),
                              Ingredient('cups', 1),
                              Ingredient('money', -6)])
    ]

    UNITS = {'water': 'ml', 'milk': 'ml', 'beans': 'g'}

    def __init__(self, *, water: int = 0, milk: int = 0, beans: int = 0,
                 cups: int = 0, money: int = 0, ) -> None:
        """
        Initialize a coffee machine instance.

        :param water: amount of water in ml, default is 0
        :param milk: amount of milk in ml, default is 0
        :param beans: amount of beans in ml, default is 0
        :param cups: number of disposable cups, default is 0
        :param money: amount of money in dollars, default is 0
        """
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = 'choosing action'
        self.write()

    def write(self, *, invalid_input: bool = False) -> None:
        """
        Print the message based on the machine state.

        :param invalid_input: if True, the message for the current machine
                              state is preceded by 'Invalid input!', default
                              is False
        """
        if invalid_input:
            print('Invalid input!')

        if self.state == 'choosing action':
            print('\nWrite action (buy, fill, take, remaining, exit):')

        elif self.state == 'choosing coffee':
            print('\nWhat do you want to buy?', end=' ')
            coffee_list = ', '.join(
                f'{n} - {coffee.name}' for n, coffee in enumerate(self.MENU, 1)
            )
            print(f'{coffee_list}, back - to main menu :')

        elif self.state.startswith('fill'):
            _, attr = self.state.split(' ')
            print('\n')
            if attr == 'cups':
                print('Write how many disposable cups you want to add.')
            else:
                print(
                    (f'Write how many {self.UNITS[attr]}'
                     f' of {attr} you want to add:')
                )

    def read(self, input_: str) -> None:
        """
        Read a string and perform an appropriate action based on its content
        and the state of the machine.
        :param input_: string representing a user's input
        """
        if self.state == 'choosing action':
            if input_ == 'buy':
                self.state = 'choosing coffee'
                self.write()
            elif input_ == 'fill':
                self.state = 'fill water'
                self.write()
            elif input_ == 'take':
                self.take()
                self.write()
            elif input_ == 'remaining':
                self.report()
                self.write()
            else:
                self.write(invalid_input=True)

        elif self.state == 'choosing coffee':
            if input_ == 'back':
                self.state = 'choosing action'
                self.write()
            else:
                try:
                    menu_index = int(input_) - 1
                except ValueError:
                    self.write(invalid_input=True)
                else:
                    if menu_index in range(len(self.MENU)):
                        coffee = self.MENU[menu_index]
                        try:
                            self.buy(coffee)
                        except MissingIngredientsError as E:
                            print(f'Sorry, not enough {E.missing}')
                        else:
                            print(
                                'I have enough resources, making you a coffee!'
                            )
                        finally:
                            self.state = 'choosing action'
                            self.write()
                    else:
                        self.write(invalid_input=True)

        elif self.state.startswith('fill'):
            _, attr = self.state.split(' ')
            try:
                amount = int(input_)
            except ValueError:
                self.write(invalid_input=True)
            else:
                if amount < 0:
                    self.write(invalid_input=True)
                else:
                    self.fill(**{attr: amount})
                    if self.state == 'fill water':
                        self.state = 'fill milk'
                    elif self.state == 'fill milk':
                        self.state = 'fill beans'
                    elif self.state == 'fill beans':
                        self.state = 'fill cups'
                    elif self.state == 'fill cups':
                        self.state = 'choosing action'
                    self.write()

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

    def take(self) -> None:
        """
        Reset money attribute to 0.

        """
        print(f'\nI gave you ${self.money}.')
        self.money = 0

    def buy(self, coffee: Coffee) -> None:
        """
        Process the purchase operation, that is, remove ingredients and add
        money to the machine if possible.

        :param coffee: Coffee object from the MENU
        :raises: MissingIngredientError if there are not enough ingredients
        """
        fill_kwargs = {ingredient.name: -ingredient.amount
                       for ingredient in coffee.recipe}
        self.fill(**fill_kwargs)

    def report(self) -> None:
        """
        Prints the coffee's machine state.
        """
        full_names = {'beans': 'coffee beans', 'cups': 'disposable cups'}
        print('\nThe coffee machine has:')
        for attr, value in vars(self).items():
            if attr == 'state':
                continue
            print(f'{value} of {full_names.get(attr, attr)}')


def main():
    machine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)
    while True:
        input_ = input()
        if input_ == 'exit':
            return
        machine.read(input_)


if __name__ == '__main__':
    main()

    
\\


class Machine:
    water = 0
    milk = 0
    coffee_beans = 0
    disposable_cups = 0
    money = 0

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def machine_print(self):
        print("\nThe coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'${self.money} of money')

    def action_taker(self, action):
        if action == "buy":
            self.buy_coffee(
                input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
        elif action == "fill":
            self.fill_machine()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.machine_print()
        else:
            return False
        return True

    def check_enough(self, water, milk, coffee_beans, disposable_cups):
        if self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < coffee_beans:
            print("Sorry, not enough coffee_beans!")
        elif self.disposable_cups < disposable_cups:
            print("Sorry, not enough disposable_cups!")
        else:
            return True
        return False

    def change_machine(self, water, milk, coffee_beans, disposable_cups, money, action):
        if action == "buy":
            if self.check_enough(-water, -milk, -coffee_beans, -disposable_cups):
                print("I have enough resources, making you a coffee!")
            else:
                return
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.disposable_cups += disposable_cups
        self.money += money

    def buy_coffee(self, choice):
        try:
            choice = int(choice)
        except ValueError:
            return
        if choice == 1:
            self.change_machine(-250, 0, -16, - 1, 4, "buy")
        elif choice == 2:
            self.change_machine(-350, -75, -20, - 1, 7, "buy")
        else:
            self.change_machine(-200, -100, -12, - 1, 6, "buy")

    def take_money(self):
        money = self.money
        self.change_machine(0, 0, 0, 0, -money, "take")
        print(f"I gave you ${money}")

    def fill_machine(self):
        water = int(input("\nWrite how many ml of water you want to add:\n"))
        milk = int(input("Write how many ml of milk you want to add:\n"))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        disposable_coffee = int(input("Write how many disposable coffee cups you want to add:\n"))
        self.change_machine(water, milk, coffee_beans, disposable_coffee, 0, "fill")


machine = Machine(400, 540, 120, 9, 550)
act = machine.action_taker(input("\nWrite action (buy, fill, take, remaining, exit):\n"))
while act:
    act = machine.action_taker(input("\nWrite action (buy, fill, take, remaining, exit):\n"))


