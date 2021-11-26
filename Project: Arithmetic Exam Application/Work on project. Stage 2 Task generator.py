'''
Description
Any test includes at least one task. This task can vary in difficulty and required timeframes. There can be more than one task; they can demand different forms of answers. One thing remains — if there's a task, there's a solution. And we need to assess it.

Math tasks can vary in difficulty. 1 * 3 is easy. 75 * 34 is a bit more difficult. For the next stages, think about levels of difficulty that you can add!

For now, let's use random numbers from 2 to 9 and integer operations: +, - and *.

Objectives
Generate a math task that looks like a math operation. Use the requirements above. Print it.
Read the answer from a user.
Check whether the answer is correct. Print Right! or Wrong!
Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

5 * 7
> 35
Right!
Example 2:

5 * 7
> 5
Wrong!

'''

# write your code here
import random
a = random.randint(2,9)
b = random.randint(2,9)
c_1 = ['*','-','+']
c = random.choice(c_1)
print(f'{a} {c} {b}')
d = input()

if c == '*':
    if int(d) == a * b:
        print('Right!')
    else:
        print('Wrong!')
elif c == '+':
    if int(d) == a + b:
        print('Right!')
    else:
        print('Wrong!')
elif c == '-':
    if int(d) == a - b:
        print('Right!')
    else:
        print('Wrong!')
else:
    print('Wrong!')
    
\\

import operator
import random

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
op = random.choice(list(ops))
action = ops[op]
a, b = [random.randint(2, 9) for i in range(2)]
solution = action(a, b)
print(a, op, b)
attempt = int(input())
print(['Wrong!', 'Right!'][attempt == solution])

\\

import random


def plus(x):
    return int(x[0]) + int(x[2])


def minus(x):
    return int(x[0]) - int(x[2])


def mult(x):
    return int(x[0]) * int(x[2])

def task():
    task = [random.randint(2, 9), random.choice(task_operator), random.randint(2, 9)]
    return task


operator = {'+': plus, '-': minus, '*': mult}
task_operator = ['+', '-', '*']
example = task()
print(f'{example[0]} {example[1]} {example[2]}')
if operator[example[1]](example) == int(input()):
    print('Right!')
else:
    print('Wrong!')

# stage_1 code
# usr_input = [x for x in input().split(' ')]
# print(operator[usr_input[1]](usr_input))
#

