'''
Description
Now let's consider a case when you need a lot of coffee. Maybe you're hosting a party with a lot of guests! In these circumstances, it's better to make preparations in advance.

So, we will ask a user to enter the desired amount of coffee, in cups. Given this, you can adjust the program by calculating how much water, coffee, and milk are necessary to make the specified amount of coffee.

Of course, all this coffee is not needed right now, so at this stage, the coffee machine doesn't actually make any coffee yet.

Objectives
Let's break the task into several steps:

First, read the numbers of coffee drinks from the input.
Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
Output the required ingredient amounts back to the user.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: a dialogue with a user might look like this

Write how many cups of coffee you will need:
> 25
For 25 cups of coffee you will need:
5000 ml of water
1250 ml of milk
375 g of coffee beans
Example 2: here is another dialogue

Write how many cups of coffee you will need:
> 125
For 125 cups of coffee you will need:
25000 ml of water
6250 ml of milk
1875 g of coffee beans

'''
def main():
    cups = int(input('Write how many cups of coffee you will need: '))

    # One cup: 200 ml of water, 50 ml of milk, and 15 g of coffee beans
    water = 200 * cups
    milk = 50 * cups
    beans = 15 * cups

    print(f'For {cups} cups of coffee you will need:')
    print(f'{water} ml of water')
    print(f'{milk} ml of milk')
    print(f'{beans} g of coffee beans')


if __name__ == '__main__':
    main()
    
    
    
    \\
    
def get_numberof_cups():
    return int(input("Write how many cups of coffee you will need:\n"))


def calculate_ingredients(n):
    water_vol = 200 * n
    milk_vol = 50 * n
    beans_wei = 15 * n
    return water_vol, milk_vol, beans_wei


def user_output(n, x, y, z):
    print(f"For {n} cups of coffee you will need:")
    print(f"{x} ml of water")
    print(f"{y} ml of milk")
    print(f"{z} g of coffee beans")


numberof_cups = get_numberof_cups()
water_volume, milk_volume, beans_weight = calculate_ingredients(numberof_cups)
user_output(numberof_cups, water_volume, milk_volume, beans_weight)



\\
# Write your code here
print("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready! """)
a = int(input("Write how many cups of coffee you will need:"))
water = 200
milk = 50
coffe = 15
print("For", a, "cups of coffee you will need:")
print(water * a, "ml of water")
print(milk * a, "ml of milk")
print(coffe * a, "g of coffee beans")


