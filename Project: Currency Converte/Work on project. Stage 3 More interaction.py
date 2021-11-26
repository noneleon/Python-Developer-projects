'''
Description
We are going to make our program more complex. As you remember, the conicoin rate was fixed in the previous stage. But in the real world, things are different. It's time to write a program that takes your conicoins and an up-to-date conicoin exchange rate, then counts how many dollars you would get, and prints the result.

Objectives
Get the number of conicoins from the user input.
Get the exchange rate from the user input.
Calculate and print the result.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Please, enter the number of conicoins you have: > 13
Please, enter the exchange rate: > 2
The total amount of dollars: 26
Example 2:

Please, enter the number of conicoins you have: > 128
Please, enter the exchange rate: > 3.21
The total amount of dollars: 410.88
'''

# write your code here!
a = int(input('Please, enter the number of conicoins you have: '))
b = float(input('Please, enter the exchange rate:'))
print(f'The total amount of dollars:{a*b}')


\\


coin_count = int(input("Please, enter the number of conicoins you have:"))
coin_rate = input("Please, enter the exchange rate:")
if '.' in coin_rate:
    coin_value = float(coin_rate)
else:
    coin_value = int(coin_rate)
print(f"The total amount of dollars: {round(coin_count * coin_value, 2)}")