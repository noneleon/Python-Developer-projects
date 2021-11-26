'''
Description
Simple tasks are good for younger kids, but math can be more difficult and more interesting! Quadratic equations, trigonometry, and a lot of other interesting things. Math library can help you with that.

Sometimes students want to save the results of the test. This is useful for viewing the learning dynamics on a topic or to identify difficult tasks.

At this stage, let's add integral squares. Of course, you can add more difficulty levels later.

Objectives
With the first message, the program should ask for a difficulty level:
1 - simple operations with numbers 2-9
2 - integral squares 11-29

A user enters an answer.
For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
For the second difficulty level: the task is an integer; the answer is the square of this number.
In case of another input: ask to re-enter. Repeat until the format is correct.

The application gives 5 tasks to a user.

The user receives one task, prints the answer.
If the answer contains a typo, print Incorrect format. and ask to re-enter the answer. Repeat until the answer is in the correct format.
If the answer is a number, print Right! or Wrong! Go to the next question.

After five answers, print Your mark is N/5. where N is the number of correct answers.

Output Would you like to save your result to the file? Enter yes or no.
In case of yes, YES, y, Yes: the app should ask the username and write Name: n/5 in level X (<level description>). (X stands for the level number) in the results.txt file. For example — Alex: 3/5 in level 1 (simple operations with numbers 2-9).
The results should be saved to the file immediately after the user gave the positive answer to the question Would you like to save your result to the file?
If the file results.txt does not exist, you should create it.

In case of no or any other word: exit the program.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:


Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 11
Incorrect format.
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 2
11
> 121
Right!
15
> 100
Wrong!
21
> 441'
Wrong format! Try again.
21
> 441
Right!
17
> 289
Right!
13
> 169
Right!
Your mark is 4/5. Would you like to save the result? Enter yes or no.
> yes
What is your name?
> Kate
The results are saved in "results.txt".
Afterword
After finishing this stage, you are totally free to improve the project in any way you like to make it a more convenient and useful tool.

You can add any features to your application. It will not be verified by tests, so there are no strict requirements.

Sample ideas:

Add a complex exam. Increase a difficulty level on the fly. For example, if a person passed the 1st level, start the 2nd one immediately.
You can add a correction level: store the tasks with wrong answers and give them next time.
Add more difficulty levels.
Track the time (read about Timer).
Write a more detailed report to a file with the results.
Show previous results inside the app (show lines from results.txt that contains the username)
Any other improvement that might be useful!

'''
import random

levels = ["simple operations with numbers 2-9", "integral squares of 11-29"]
choices = ["yes", "YES", "y", "Yes"]
print("Which level do you want? Enter a number:")
print("1 - simple operations with numbers 2-9")
print("2 - integral squares of 11-29")
ex_choice = 0
choice = int(input())
mark = 0
while choice != 1 or choice != 2:
    if choice == 1:
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
        break
    elif choice == 2:
        for _ in range(5):
            question = int(random.randint(11, 29))
            print(question)
            while True:
                try:
                    Input = int(input())
                    if Input == question ** 2:
                        print("Right!")
                        mark += 1
                    else:
                        print("Wrong!")
                    break
                except ValueError:
                    print("Incorrect format.")
                    continue
        break
    else:
        print("Incorrect format.")
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = int(input())
print("Your mark is {}/5. Would you like to save the result? Enter yes or no.".format(mark))
choice2 = input().strip()
if choice2 in choices:
    name = input("What is your name?\n")
    ex_choice = choice - 1
    selected_level = levels[ex_choice]
    s = "{}: {}/5 in level {} ({}).".format(name, mark, choice, selected_level)
    with open("results.txt", "a") as f:
        f.write(s)
    print('The results are saved in "results.txt".')
    
\\
import re
from operator import add, sub, mul
from random import choice, randrange
from typing import Callable, Optional, Any


def input_(*, prompt: Optional[str] = None,
           predicate: Callable,
           wrapper: Callable,
           err_msg: Optional[str] = None,
           repeat_prompt: bool = True) -> Any:
    """
    Take input from the standard input until predicate is True. Return
    the accepted input processed by wrapper.

    :param prompt: Optional message to display before taking input. The
                   default is None.
    :param predicate: Callable object returning a boolean used to decide
                      whether an input is accepted.
    :param wrapper: Callable object used to process the accepted input before
                    returning it.
    :param err_msg: Optional error message to display when an input is
                    rejected.
    :param repeat_prompt: Boolean flag controlling whether the initial prompt
                          should be repeated if an input is rejected.
    :return: wrapper(x) where x is the first input such that predicate(x) is
             True.
    """
    if prompt is not None:
        print(prompt)

    while True:
        user_input = input()
        if predicate(user_input):
            return wrapper(user_input)

        if err_msg is not None:
            print(err_msg)
        if repeat_prompt and prompt is not None:
            print(prompt)


menu_prompt = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares 11-29"""

menu_err_msg = 'Incorrect format.'
task_err_msg = 'Wrong format! Try again.'


def menu() -> int:
    """
    Display the menu. Return the chosen level.

    :return: chosen level cast to integer
    """
    return input_(prompt=menu_prompt,
                  predicate=lambda x: x in ('1', '2'),
                  wrapper=int,
                  err_msg=menu_err_msg)


def is_integral(x: str) -> bool:
    """
    Check whether a string can be cast to integer.
    :param x: string to check
    :return: True or False
    """
    return bool(re.fullmatch(r'-?\d+', x))


def task(difficulty: int) -> bool:
    """
    Run one of the test tasks.
    :param difficulty: task difficulty (can be 1 or 2)
    :return: True if the user answer is correct, False otherwise.
    """
    if difficulty == 1:
        operators = {'+': add, '-': sub, '*': mul}
        a, b = randrange(2, 10), randrange(2, 10)
        op = choice(list(operators))
        answer = str(operators[op](a, b))

        return input_(prompt=f'{a} {op} {b}',
                      predicate=is_integral,
                      wrapper=lambda x: x == answer,
                      err_msg=task_err_msg,
                      repeat_prompt=False,
                      )

    if difficulty == 2:
        a = randrange(11, 30)
        answer = str(a ** 2)

        return input_(prompt=f'{a}',
                      predicate=is_integral,
                      wrapper=lambda x: x == answer,
                      err_msg=task_err_msg,
                      repeat_prompt=False,
                      )


def save(*, level, description, correct_count, repetitions):
    """
    Save the test results to 'results.txt' file in the working directory.
    If the file exists, the results will be appended, if not the file will be
    created.

    :param level: difficulty level of the task
    :param description: description of the task
    :param correct_count: number of correct answers
    :param repetitions: number of repetitions
    :return:
    """
    print('Would you like to save the result? Enter yes or no.')
    if input() in ('yes', 'y', 'YES', 'Yes'):
        print('What is your name?')
        name = input()
        file_name = 'results.txt'
        with open(file_name, 'a', encoding='utf_8') as f_out:
            report = (f'{name}: {correct_count}/{repetitions} '
                      f'in level {level} ({description})'
                      )
            f_out.write(report)
            print(f'The results are saved in "{file_name}".')


def main():
    test = {'level': menu(), 'correct_count': 0, 'repetitions': 5}

    if test['level'] == 1:
        test['description'] = 'simple operations with numbers 2-9'
    else:
        test['description'] = 'integral squares 11-29'

    for _ in range(test['repetitions']):
        correct = task(test['level'])
        if correct:
            test['correct_count'] += 1
            print('Right!')
        else:
            print('Wrong!')

    print(f"Your mark is {test['correct_count']}/{test['repetitions']}.")

    save(**test)


if __name__ == '__main__':
    main()
    
\\

import random


def easyexpr(expr=None):
    return expr if expr else f"{random.randint(2, 9)} {random.choice(['+', '-', '*'])} {random.randint(2, 9)}"


def hardexpr(expr=None):
    global diff
    diff = True
    num = random.randint(11, 29)
    return expr if expr else f"{num} * {num}"


def save(mark):
    global diff
    diff = "level 2 (integral squares of 11-29)" if diff else "level 1 simple operations with numbers 2-9"
    name = input("What is your name?\n")
    with open("results.txt", "a+") as f:
        print(f"{name}: {mark} in {diff}.", file=f)
        print("The results are saved in \"results.txt\".")


i, correct, diff = 0, 0, False

while True:
    try:
        expression = {'1': easyexpr, '2': hardexpr}[
            input("Which level do you want? Enter a number:\n"
                  "1 - simple operations with numbers 2-9\n"
                  "2 - integral squares of 11-29\n")]()
        break
    except KeyError:
        print("Incorrect format")
        continue


while i < 5:
    print(expression.split()[0] if diff else expression)
    try:
        if int(input()) == eval(expression):
            print("Right!")
            i += 1
            correct += 1
        else:
            print("Wrong!")
            i += 1
        expression = hardexpr() if diff else easyexpr()
    except ValueError:
        print("Incorrect format")
        expression = hardexpr(expression) if diff else easyexpr(expression)

print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
save(f"{correct}/5") if input() in ["yes", "YES", "y", "Yes"] else exit()

