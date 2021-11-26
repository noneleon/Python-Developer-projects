'''
Description
In this stage, you need to add a new feature to the project — pick one name from the dictionary at random; this person's share will be paid by others. Make it a lucky day for somebody!

Make sure you give your users a choice whether they want to use this feature or not. Don't turn it on by default.

After picking a random name, print it so that everyone knows who is the lucky one.

Objectives
In this stage your program should perform the following steps together with the steps from the previous stages:

In case of an invalid number of people, "No one is joining for the party" is expected as an output;
Otherwise, ask the user whether they want to use the "Who is lucky?" feature;
Take input from the user;
If a user wants to use the feature (Yes), choose a name from the dictionary keys at random and print the following: {Name} is the lucky one!;
If the user enters anything else, print No one is going to be lucky.
Do not print the output of the previous stage (see examples).

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
    total = round(int(input()) / people_amount, 2)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'No':
        print('No one is going to be lucky')
    elif lucky == 'Yes':
        print(f"{random.choice(bill)} is the lucky one")
    # for k, val in big_bill.items():
    #     big_bill[k] = total
    # print(big_bill)
    
 import random

print('Enter the number of friends joining (including you)')
n_o_f = int(input())

friend = dict()
def bill_per_person(total, n_o_f):
    bill_per_person = round(total / n_o_f, 2)
    for key in list:
        friend[key] = bill_per_person
    

 
if n_o_f != 0 and n_o_f > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    x = 0
    while x < n_o_f:
        name = input()
        friend[name] = friend.get(name, 0) 
        
        x += 1
    
    list = []
    for w in friend.keys():
        list.append(w)
    print('Enter the total bill value:')
    total = int(input())
    bill_per_person(total, n_o_f)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    user_input = input()
    if user_input.lower() == 'yes':
        
        individual = random.choice(list)
        print(individual, ' is the lucky one!')
    else:
        print('No one is going to be lucky')
    
    
    
else:
    print('No one is joining for the party')
    
    
    
\\


from random import choice


class Friends:
    def __init__(self):
        self.friends = {}
        self.number_friends = 0
        self.total_bill = 0
        self.bill = 0
        self.lucky = None

    def get_number_friends(self):
        print('Enter the number of friends joining (including you):')
        total = int(input())
        if total > 0:
            self.number_friends = total
        else:
            print('No one is joining for the party')

    def add_friends(self):
        print('Enter the name of every friend (including you), each on a new line:')
        for _ in range(self.number_friends):
            self.friends[input()] = 0

    def get_bill(self):
        print('Enter the total bill value:')
        self.total_bill = int(input())
        self.bill = round(self.total_bill / self.number_friends, 2)

    def split_bill(self):
        for name in self.friends.keys():
            self.friends[name] = self.bill

    def get_lucky(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        action = input()
        if action == 'Yes':
            self.lucky = choice(list(self.friends.keys()))
            print(f'{self.lucky} is the lucky one!')
        else:
            print('No one is going to be lucky')

    def main(self):
        self.get_number_friends()
        if self.number_friends:
            self.add_friends()
            self.get_bill()
            self.get_lucky()


get_friends = Friends()
get_friends.main()
    
    
