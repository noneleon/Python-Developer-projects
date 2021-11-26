'''
Description
Holy moly! Suddenly you remember that back in 2008 you purchased several conicoins! Are you officially rich? Well, we need to find it out. You need to write a program that shows how much you can get after selling your conicoins. One conicoin is 100 dollars. Read your amount of the conicoins as the input, convert them into dollars, and output the result. Also, express your joy, it's important.

Objectives
Find out if you are rich.

Input the amount of your conicoins.
Calculate the number of dollars you receive after the conversion. 1 conicoin = 100 dollars, print the result as shown below.
Woohoo! You are rich!
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Output:

> 42
I have 42 conicoins.
42 conicoins cost 4200 dollars.
I am rich! Yippee!

'''

# write your code here!
a = int(input())
print(f'I have {a} conicoins.')
print(f'{a} conicoins cost {100*a} dollars.')
print('I am rich! Yippee!')


amount = int(input())
print(f'I have {amount} coins.\n{amount} conicoins cost {amount * 100} dollars.\nI am rich! Yepee!')