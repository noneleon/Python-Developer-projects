'''
Description
It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better. First, we need to recalculate the split value for everyone. Make sure that our lucky one pays 0.

Recalculate the split value for n-1 people where n is the total length of the dictionary and update the values in the dictionary with the new split value for everyone.

If a user decides not to use the "Who is lucky" feature, print the original dictionary.

Objectives
In this stage your program should perform the following steps together with the steps from the previous stages:

In case of an invalid number of people, "No one is joining for the party" is expected as an output;
Otherwise, if the user choice is Yes, re-split the bill according to the feature;
Round the split value to two decimal places;
Update the dictionary with new split values and 0 for the lucky person;
Print the updated dictionary;
If the user entered anything else instead of Yes, print the original dictionary.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: The feature is used

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}
Example 2: The feature is skipped

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
Example 3: Invalid input

Enter the number of friends joining (including you):
> 0

No one is joining for the party

'''

import random

print("Enter the number of friends joining (including you):")
people_amount = int(input())
bill = []
if people_amount <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(0, people_amount):
        bill.append(input())
    big_bill = dict.fromkeys(bill, 0)
    print("Enter the total bill value:")
    m =  int(input())
    if m % people_amount==0:
        total = int(m / people_amount)
    else:
        total = round(m / people_amount, 2)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    n=random.choice(bill)
    if lucky == 'No':
        print('No one is going to be lucky')
        for k, val in big_bill.items():
            big_bill[k] = total
        print(big_bill)
    elif lucky == 'Yes':
        if m % (people_amount-1)==0:
            total = int(m / (people_amount-1))
        else:
            total = round(m / (people_amount-1), 2)
        print(f"{n} is the lucky one")
        for k, val in big_bill.items():
            big_bill[k] = total
        big_bill[n]=0
        print(big_bill)
        
        
\\

from random import choice


def get_num_of_friends():
    print('Enter the number of friends joining (including you):')
    return int(input())


def get_friends(num):
    print('Enter the name of every friend (including you), each on a new line:')
    f_dict = dict()
    while num:
        f_dict[input('')] = 0
        num -= 1
    return f_dict


def get_bill():
    print('Enter the total bill:')
    return int(input())


def split_bill(bill, no_of_split):
    return round(bill / no_of_split, 2)


def update_dict(f_dict, lucky, bill):
    for key in f_dict.keys():
        if key != lucky:
            f_dict[key] = bill


def get_lucky(f_list):
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No')
    opt = input()
    if opt == 'Yes':
        lucky = choice(list(f_list.keys()))
        print(lucky, 'is the lucky one!')
        return lucky
    else:
        print('No one is going to be lucky')
    return None


try:
    no_of_friends = get_num_of_friends()
    assert no_of_friends > 0
    friends = get_friends(no_of_friends)
    total_bill = get_bill()
    lucky_friend = get_lucky(friends)
    no_of_friends = no_of_friends - 1 if lucky_friend else no_of_friends
    bill_split = split_bill(total_bill, no_of_friends)
    update_dict(friends, lucky_friend, bill_split)
    print(friends)
except ValueError:
    print('error')
except AssertionError:
    print('No one is joining for the party')

\\

import random
from random import Random

class Friends:
    def __init__(self):
        # declaring variables
        self.friends_dict: dict = {}
        self.number_of_friends = 0
        self.lucky_one = ""
        self.bill = 0
        self.choice = False

        # main logic
        self.count_friends()
        self.get_bill()
        self.lucky()
        self.bill_split()

    def count_friends(self):
        self.number_of_friends = int(input('Enter the number of friends joining (including you):\n'))
        if int(self.number_of_friends) <= 0:
            print("\nNo one is joining for the party")
            exit()
        print('\nEnter the name of every friend (including you), each on a new line:')
        self.friends_dict = {input(): 0 for _ in range(self.number_of_friends)}

    def get_bill(self):
        self.bill = float(input("Enter the total bill value:\n"))

    def bill_split(self):
        if not self.choice:
            split_bill = round(self.bill/len(self.friends_dict), 2)
        else:
            split_bill = round(self.bill / (len(self.friends_dict) - 1), 2)
        for key in self.friends_dict.keys():
            if key != self.lucky_one:
                self.friends_dict[key] = split_bill
        print(self.friends_dict)

    def lucky(self):
        choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        a = self.number_of_friends
        listy = list(self.friends_dict.keys())
        r = random.choice(listy)
        if choice == "Yes":
            self.choice = True
            self.lucky_one = r
            print(f"{r} is the lucky one!")
        else:
            print("No one is going to be lucky")


def main():
    splitter = Friends()


if __name__ == '__main__':
    main()

    
    
    
        