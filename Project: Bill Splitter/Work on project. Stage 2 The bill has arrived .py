'''
Description
It's bill time! Let's split the bill among everyone and update the values in the dictionary you have created in the previous stage.

Since we don't want to deal with too many decimals (who carries that much change anyway?), round the split amount to two decimal places and then update the dictionary with the split values.

Objectives
In this stage your program should perform the following steps together with the steps of the previous stage:

If there are no people to split the bill (the number of friends is 0 or an invalid input), output "No one is joining for the party";
Else, take user input: the final bill;
Split the total bill equally among everyone;
Round the split value to two decimal places;
Update the dictionary with the split values;
Print the updated dictionary.
Do not print the output of the previous stage (see examples).

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: Five people joining

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

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
Example 2: Seven people joining

Enter the number of friends joining (including you):
> 7

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
> Ben
> Ned

Enter the total bill value:
> 41

{'Marc': 5.86, 'Jem': 5.86, 'Monica':5.86, 'Anna': 5.86, 'Jason': 5.86, 'Ben': 5.86, 'Ned': 5.86}
Example 3: Invalid input

Enter the number of friends joining (including you):
> 0

No one is joining for the party
'''

friends = dict()

try:
    num_friends = int(input("Enter the number of friends joining (including you):\n"))
    if num_friends <= 0:
        raise ValueError
except ValueError:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    total_bill = int(input("\nEnter the total bill value:\n"))
    bill_per_person = round(total_bill / len(friends.keys()), 2)
    friends = {person: bill_per_person for (person, _) in friends.items()}

    print(f"\n{friends}")
    
    
\\

class Friends:
    def __init__(self):
        self.friends = {}
        self.number_friends = 0
        self.total_bill = 0
        self.bill = 0

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

    def main(self):
        self.get_number_friends()
        if self.number_friends:
            self.add_friends()
            self.get_bill()
            self.split_bill()
            print(self.friends)


get_friends = Friends()
get_friends.main()



    