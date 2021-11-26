'''
Description
A real coffee machine doesn't have an infinite supply of water, milk, or coffee beans. And if you input a really big number, it's almost certain that a real coffee machine wouldn't have the supplies needed to make all that coffee for you.

In this stage, you need to improve the previous program. Now you will check amounts of water, milk, and coffee beans available in your coffee machine at the moment.

Objectives
Write a program that does the following:

It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".
If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.
If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".
Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Write how many ml of water the coffee machine has:
> 300
Write how many ml of milk the coffee machine has:
> 65
Write how many grams of coffee beans the coffee machine has:
> 100
Write how many cups of coffee you will need:
> 1
Yes, I can make that amount of coffee
Example 2:

Write how many ml of water the coffee machine has:
> 500
Write how many ml of milk the coffee machine has:
> 250
Write how many grams of coffee beans the coffee machine has:
> 200
Write how many cups of coffee you will need:
> 10
No, I can make only 2 cups of coffee
Example 3:

Write how many ml of water the coffee machine has:
> 1550
Write how many ml of milk the coffee machine has:
> 299
Write how many grams of coffee beans the coffee machine has:
> 300
Write how many cups of coffee you will need:
> 3
Yes, I can make that amount of coffee (and even 2 more than that)
Example 4:

Write how many ml of water the coffee machine has:
> 0
Write how many ml of milk the coffee machine has:
> 0
Write how many grams of coffee beans the coffee machine has:
> 0
Write how many cups of coffee you will need:
> 1
No, I can make only 0 cups of coffee
Example 5:

Write how many ml of water the coffee machine has:
> 0
Write how many ml of milk the coffee machine has:
> 0
Write how many grams of coffee beans the coffee machine has:
> 0
Write how many cups of coffee you will need:
> 0
Yes, I can make that amount of coffee 
Example 6:

Write how many ml of water the coffee machine has:
> 200
Write how many ml of milk the coffee machine has:
> 50
Write how many grams of coffee beans the coffee machine has:
> 15
Write how many cups of coffee you will need:
> 0
Yes, I can make that amount of coffee (and even 1 more than that)
'''
def count(water: int, milk: int, beans: int, cups: int) -> str:
    possible = min([
        water // 200,
        milk // 50,
        beans // 15
    ])

    if possible == cups:
        message = 'Yes, I can make that amount of coffee'
    elif possible > cups:
        message = f'Yes, I can make that amount of coffee' \
                  f' (and even {possible - cups} more than that)'
    else:
        message = f'No, I can make only {possible} cups of coffee'

    return message


def main():
    water = int(input('Write how many ml of water the coffee machine has: '))
    milk = int(input('Write how many ml of milk the coffee machine has: '))
    beans = int(input('Write how many grams of coffee beans'
                      ' the coffee machine has: '))
    cups = int(input('Write how many cups of coffee you will need: '))

    print(count(water, milk, beans, cups))


if __name__ == '__main__':
    main()
    
    
\\

import math
print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input())
print('Write how many cups of coffee you will need:')
cups_need = int(input())
cups_water = water / 200
cups_milk = milk / 50 
cups_beans = beans / 15
extra = math.floor(min(cups_water - cups_need, cups_milk - cups_need, cups_beans - cups_need))
cups = math.floor(min(cups_water, cups_milk, cups_beans))
if cups == cups_need:
    print('Yes, I can make that amount of coffee')
elif cups > cups_need:
    print(f'Yes, I can make that amount of coffee (and even {extra} more than that)')
else:
    print(f'No, I can make only {cups} cups of coffee')
    
    
\\

class CoffeeMachine():

    def __init__(self):
        self.w = 200
        self.m = 50
        self.b = 15
        self.water_vol = int(input("Write how many ml of water the coffee machine has:\n"))
        self.milk_vol = int(input("Write how many ml of milk the coffee machine has:\n"))
        self.beans_wei = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
        self.number_of_cups = int(input("Write how many cups of coffee you will need:\n"))
        self.canmake = min([self.water_vol // self.w, self.milk_vol // self.m, self.beans_wei // self.b])
        self.answer1 = "Yes, I can make that amount of coffee"
        self.answer2 = "No, I can make only {} cups of coffee"
        self.answer3 = " (and even {} more than that)"

    def calculate_ingredients(self):
        water_vol_used = self.w * self.number_of_cups
        self.water_vol -= water_vol_used
        milk_vol_used = self.m * self.number_of_cups
        self.milk_vol -= milk_vol_used
        beans_wei_left = self.b * self.number_of_cups
        self.beans_wei -= beans_wei_left

    def user_output(self):
        if self.water_vol < 0 or self.milk_vol < 0 or self.beans_wei < 0:
            return self.answer2.format(str(self.canmake))
        elif self.water_vol >= 0 and self.milk_vol >= 0 and self.beans_wei >= 0:
            if self.canmake == self.number_of_cups:
                return self.answer1
            elif self.canmake > self.number_of_cups:
                return self.answer1 + self.answer3.format(str(self.canmake - self.number_of_cups))


my_coffee_machine = CoffeeMachine()
my_coffee_machine.calculate_ingredients()
print(my_coffee_machine.user_output())

