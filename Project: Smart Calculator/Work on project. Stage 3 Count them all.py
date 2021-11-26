'''
Description
In rare cases, we need to calculate the sum of only two numbers. Now it is time to teach the calculator to read an unlimited sequence of numbers. Also, let's take care of ourselves if after a while we want to remember what our program does. For this purpose, we'll introduce a new command /help to our calculator. Users who have first exposure to this program may use /help as well to know more about it!

Objectives
Add to the calculator the ability to read an unlimited sequence of numbers.
Add a /help command to print some information about the program.
If you encounter an empty line, do not output anything.
Examples
The greater-than symbol followed by a space (>) represents the user input.

> 4 5 -2 3
10
> 4 7
11
> 6
6
> /help
The program calculates the sum of numbers
> /exit
Bye!
'''

while True:
    a = input()
    if a == '/exit':
        print('Bye!')
        break
    if len(a) == 0:
        continue
    elif a == '/help':
        print('The program calculates the sum of numbers')
    else:
        print(sum([int(x) for x in a.split()])) if a else print()
        
\\
def main():
    # def addition(x, y):
    #     """Return the sum of the two argument"""
    #     return int(x) + int(y)

    while True:
        var = input()
        if var == '/exit':
            print('Bye!')
            break
        if var == '/help':
            print('The program calculates the sum of numbers')
        elif var == '':
            continue
        else:
            list_num = [int(i) for i in var.split()]
            print(sum(list_num))


if __name__ == "__main__":
    main()