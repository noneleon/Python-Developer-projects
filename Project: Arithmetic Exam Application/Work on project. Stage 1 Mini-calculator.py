'''
Description
People learn new things in one way or another. Learning sometimes means that you need to check your comprehension by taking a test. It also requires a person (or a program) to check your answers. You may have been in a situation when you think that you have solved the task correctly, but your professor has a different (sometimes wrong!) answer. It happens; everybody makes mistakes.

Not our application though. It should calculate the solution in a very precise manner. We need to make a simple calculator that can evaluate expressions like a + b, a - b, or a * b. We will leave the division aside for now.

Objectives
A user inputs a line that looks like a simple mathematical operation.
The application should print the result of the operation.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> 5 + 7
12
Example 2:

> 3 * 100
300
Example 3:

> 5 - 10
-5
Example 4:

> 8 * 0
0
'''

# write your code here
a,b,c = input().split()
a , c = int(a) ,int(c)

if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
else:
    print('')
    
\\
import operator
import itertools as it
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
s = input('> ')
a1, t, a2 = map(str.strip, s.partition(*it.compress(list(ops), map(s.__contains__, ops))))
print(ops[t](*map(int, (a1, a2))))


\\

# write your code here
x, op,  y = input().split()
try:
    x = int(x)
    y = int(y)
    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        print(x / y)

except:
    print("error happen ")

