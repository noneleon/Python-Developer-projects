'''
Description
Let's write an application that assesses the user's knowledge.
Many people get nervous during exams; they can accidentally hit a wrong key, confuse , with . in floats, and so on. Our application should allow some room for errors and give a person the opportunity to correct the typo.

Objectives
The application should give the user 5 tasks. The tasks are akin to the previous stage: two numbers from 2 to 9 and an integer operation.
The user receives one task, prints the answer. If the answer contains a typo (letters or otherwise empty), the program should print Incorrect format. and ask to re-enter the answer. Repeat until the answer is in the correct format. If the answer is a number, print Right! or Wrong! depending on the answer and carry on to the next question.
After five tasks, output Your mark is n/5. where n is the number of correct answers.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: An example of the output


3 + 8
> 11q
Incorrect format.
> eleven
Incorrect format.
> 11
Right!
5 * 3
> 35
Right!
2 - 5
> -4
Wrong!
3 * 3
> 9
Right!
8 + 3
> 11
Right!
Your mark is 4/5.

'''

# write your code here
import random
mark = 0
Input = 0
for _ in range(5):
    operations = [" + ", " - ", " * "]
    question = str(random.randint(2, 9)) + random.choice(operations) + str(random.randint(2, 9))
    print(question)
    while True:
        try:
            Input = int(input())
            if Input == eval(question):
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
            break
        except ValueError:
            print("Incorrect format.")
            continue
print("Your mark is {}/5.".format(mark))
\\

import random


def calc():
    global count
    x, y, op = random.randint(2, 9), random.randint(2, 9), random.choice(["+", "-", "*"])

    task = f'{x} {op} {y}'
    print(task)

    while True:
        try:
            guess = int(input())
            break
        except:
            print("Wrong format.")

    if guess == eval(task):
        print("Right!")
        count += 1
    else:
        print("Wrong!")

count = 0
for n in range(0,5):
    calc()

print(f"Your mark is {count}/5.")
\\

import random

number_of_tasks = 0
user_mark = 0

while number_of_tasks < 5:
    # Generate math task
    math_task = f"{random.randint(2, 9)} {random.choice(['+', '-', '*'])} {random.randint(2, 9)}"
    print(math_task)
    correct_result = eval(math_task)

    # Test user's answer
    while True:
        try:
            user_answer = int(input())
        except ValueError:
            print('Incorrect format.')
            continue
        break

    # Check user's answer
    if user_answer == correct_result:
        user_mark += 1
        print('Right!')
    else:
        print('Wrong!')

    number_of_tasks += 1

print(f'Your mark is {user_mark}/5')