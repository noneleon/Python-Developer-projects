'''
Description
Finally, we got to the next operation: subtraction. It means that from now on the program must receive the addition + and subtraction - operators as an input to distinguish operations from each other. It must support both unary and binary minus operators. Moreover, If the user has entered several same operators following each other, the program still should work (like Java or Python REPL). Also, as you remember from school math, two adjacent minus signs turn into a plus. The smart calculator ought to have such a feature.

Pay attention to the /help command, it is important to maintain its relevance depending on the changes (in the next stages too). You can write information about your program in free form, but the main thing is that it should be understandable to you and other users.

Objectives
The program must calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4, and so on.
Modify the result of the /help command to explain these operations.
Decompose your program using functions to make it easy to understand and edit later.
The program should not stop until the user enters the /exit command.
If you encounter an empty line, do not output anything.
Examples
The greater-than symbol followed by a space (>) represents the user input.

> 8
8
> -2 + 4 - 5 + 6
3
> 9 +++ 10 -- 8
27
> 3 --- 5
-2
> 14       -   12
2
> /exit
Bye!
'''

while True:
    a = input()
    if a:
        if a == '/exit':
            print('Bye!')
            break    
        else:
            print(eval(a)) if a != '/help' else print('The program evaluvates the given equation')       
    else:
        continue
        
\\

while True:
    user = input()
    if user == "/exit":
        print("Bye!")
        break
    elif user == "/help":
        print("The program calculates the sum and subtract of numbers")
    elif user == '':
        continue
    elif " " not in user:
        print(user)
    else:
        num = user.split()
        res = int(num[0])
        for i in range(0, len(num)):
            if i % 2 != 0 and ('+' in num[i] or ('-' in num[i] and len(num[i]) % 2 == 0)):
                num[i] = '+'
            elif i % 2 != 0 and ('-' in num[i] and len(num[i]) % 2 != 0):
                num[i] = '-'
        for i in range(0, len(num)):
            if num[i] == '+':
                res += int(num[i + 1])
            elif num[i] == '-':
                res -= int(num[i + 1])
        print(res)
        
        