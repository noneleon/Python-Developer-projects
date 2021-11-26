'''
Description
In the beginning, we mentioned that the calculator will be able to store the results of previous calculations. Do you have any idea how to do that? Of course! This can be achieved by introducing variables. Storing results in variables and then operating them at any time is a very convenient function.

Objectives
So, your program should support variables. Use dict to store them.

Go by the following rules for variables:

We suppose that the name of a variable (identifier) can contain only Latin letters.
A variable can have a name consisting of more than one letter.
The case is also important; for example, n is not the same as N.
The value can be an integer number or a value of another variable.
It should be possible to set a new value to an existing variable.
To print the value of a variable you should just type its name.
The example below shows how variables can be declared and displayed.

> n = 3
> m=4
> a  =   5
> b = a
> v=   7
> n =9
> count = 10
> a = 1
> a = 2
> a = 3
> a
3
Incorrect spelling or declaration of variables should also throw an exception with the corresponding message to the user:

First, the variable is checked for correctness. If the user inputs an invalid variable name, then the output should be "Invalid identifier".
> a2a
Invalid identifier
> n22
Invalid identifier
If a variable is valid but not declared yet, the program should print "Unknown variable".
> a = 8
> b = c
Unknown variable
> e
Unknown variable
If an identifier or value of a variable is invalid during variable declaration, the program must print a message like the one below.
> a1 = 8
Invalid identifier
> n1 = a2a
Invalid identifier
> n = a2a
Invalid assignment
> a = 7 = 8
Invalid assignment
Please note that the program should print "Invalid identifier" if the left part of the assignment is incorrect. If the part after the "=" is wrong then use the "Invalid assignment". First we should check the left side.

Handle as many incorrect inputs as possible. The program must never throw an exception of any kind.

It is important to note, all variables must store their values between calculations of different expressions.

Do not forget about previously implemented commands: /help and /exit.

Examples
The greater-than symbol followed by a space (>) represents the user input.

> a  =  3
> b= 4
> c =5
> a + b - c
2
> b - c + 4 - a
0
> a = 800
> a + b + c
809
> BIG = 9000
> BIG
9000
> big
Unknown variable
> /exit
Bye!
'''

from collections import deque
import math


# class for control commands within loop
class CommandError(Exception):
    def __init__(self, message):
        self.message = message


assignments = {}


def get_precedence(char):
    if char == '^':
        return 3
    if char == '*' or char == '/':
        return 2
    if char == '+' or char == '-':
        return 1
    return -1


def is_assignment(string):
    tokens = string.split('=')
    if len(tokens) == 2:
        key = tokens[0].strip()
        if not key.isalpha():
            raise TypeError('Invalid identifier')
        valstr = tokens[1].strip()
        if not valstr.isalpha():
            try:
                value = int(valstr)
            except ValueError:
                raise ValueError('Invalid assignment')
        else:
            value = assignments.get(valstr)
            if value is None:
                raise NameError('Unknown variable')
        assignments[key] = value
        return True
    elif len(tokens) > 2:
        raise ValueError('Invalid assignment')
    return False


def is_command(string):
    if string[0] == "/":
        if line == "/help":
            print('The program calculates the sum of numbers. It supports multiplication, integer division, '
                  'parentheses, addition, and both unary and binary minus operators.')
        elif line == "/exit":
            raise CommandError('Exit command')
        else:
            raise CommandError('Unknown command')
        return True
    return False


def is_minus(token):
    return token[0] == '-' and len(token) % 2 == 1


def to_infix(string):
    infix = list()
    temp = ""
    prev = None
    minus = 0
    for char in string:
        if char.isalpha() or char.isdigit():
            if prev is not None:
                if prev == '-':
                    if minus % 2 == 0:
                        prev = '+'
                    minus = 0
                infix.append(prev)
                prev = None
            temp += char
        else:
            if len(temp) > 0:
                infix.append(temp)
                temp = ""
            if prev is not None and prev == ')':
                infix.append(prev)
                prev = None
            if char == '(':
                if prev is not None:
                    if prev == '-':
                        if minus % 2 == 0:
                            prev = '+'
                        minus = 0
                    infix.append(prev)
                prev = char
            if char == ')' or char == '*' or char == '/':
                if prev is not None:
                    raise ValueError('Invalid expression')
                prev = char
            if char == '+' or char == '-':
                if prev is not None and prev != char:
                    raise ValueError('Invalid expression')
                if char == '-':
                    minus += 1
                prev = char
    if len(temp) > 0:
        infix.append(temp)
    if prev is not None:
        if prev == '-' and minus % 2 == 0:
            prev = '+'
        infix.append(prev)
    return infix


def to_postfix(string):
    infix = to_infix(string)
    postfix = deque()
    stack = deque()
    for i in infix:
        if i.isalpha() or i.isdigit():
            postfix.append(i)
        else:
            if len(stack) == 0 or peek_stack(stack) == '(':
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while len(stack) > 0 and peek_stack(stack) != '(':
                    postfix.append(stack.pop())
                if len(stack) == 0:
                    raise ValueError('Invalid expression')
                stack.pop()
            elif get_precedence(peek_stack(stack)) < get_precedence(i):
                stack.append(i)
            elif get_precedence(peek_stack(stack)) >= get_precedence(i):
                while len(stack) > 0 and peek_stack(stack) != '(' and \
                        get_precedence(peek_stack(stack)) >= get_precedence(i):
                    postfix.append(stack.pop())
                stack.append(i)
    while len(stack) > 0:
        if peek_stack(stack) == '(':
            raise ValueError('Invalid expression')
        postfix.append(stack.pop())
    return postfix


def peek_stack(stack):
    return stack[len(stack) - 1]


def calculate_sum(string):
    total = deque()
    postfix = to_postfix(string)
    for p in postfix:
        if p.isdigit():
            total.append(int(p))
        elif p.isalpha():
            num = assignments.get(p)
            if num is None:
                raise NameError('Unknown variable')
            total.append(num)
        else:
            num1 = total.pop()
            try:
                num2 = total.pop()
            except IndexError:
                num2 = 0
            if p[0] == '*':
                num3 = num2 * num1
            elif p[0] == '/':
                num3 = num2 / num1
            elif p[0] == '+':
                num3 = num2 + num1
            elif p[0] == '-':
                num3 = num2 - num1
            else:
                num3 = math.pow(num1, num2)
            total.append(num3)
    print(int(total.pop()))


while True:
    line = input()
    try:
        if len(line) == 0 or is_command(line) or is_assignment(line):
            continue
        calculate_sum(line)
    except CommandError as ce:
        if ce.message == "Exit command":
            break
        print(ce.message)
    except NameError as ne:
        print(ne)
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
print('Bye!')

\\

import sys


def is_valid_identifier(identifier: str) -> bool:
    return identifier.isalpha()


def is_valid_value(value: str) -> bool:
    return value.isdigit() or is_valid_identifier(value)


def is_valid_numeric_expr(expr: str) -> bool:
    return not (
        expr.endswith(("+", "-"))
        or " " in expr
        and not any(char in ("+", "-") for char in expr)
    )


class SmartCalculator:
    memory = dict()

    def process_input(self):
        if inp := input():
            if inp.startswith("/"):
                self._execute_command(inp)
            else:
                try:
                    if "=" in inp:
                        self._execute_assignment(inp)
                    else:
                        if is_valid_numeric_expr(inp):
                            print(self._calculate_expr(inp))
                        else:
                            print("Invalid expression")
                except ValueError:
                    print("Invalid identifier")
                except KeyError:
                    print("Unknown variable")
                except TypeError as e:
                    print("Invalid assignment", e)

    def _execute_command(self, command: str) -> None:
        match command:
            case "/help":
                print("The program calculates blah blah")
            case "/exit":
                print("Bye!")
                sys.exit()
            case _:
                print("Unknown command")

    def _execute_assignment(self, inp: str) -> None:
        args = inp.replace("=", " ", 1).split()
        if not is_valid_identifier(args[0]):
            raise ValueError
        elif is_valid_identifier(args[1]) and args[1] not in self.memory:
            raise KeyError
        elif len(args) != 2 or not is_valid_value(args[1]):
            raise TypeError
        self.memory[args[0]] = self._parse_identifier(args[1])

    def _calculate_expr(self, expr: str) -> int:
        return sum(map(self._parse_identifier, self._parse_expr(expr)))

    def _parse_expr(self, expr: str) -> list[str]:
        args = expr.replace("--", "+").replace("+", " ").split()
        for i in range(len(args)):
            if args[i] == "-":
                args[i + 1] = args[i] + args[i + 1]
        return [arg for arg in args if arg != "-"]

    def _parse_identifier(self, identifier: str) -> int:
        try:
            return int(identifier)
        except ValueError:
            sign = 1
            if identifier.startswith("-"):
                identifier = identifier[1:]
                sign = -1

            if is_valid_identifier(identifier):
                return sign * int(self.memory[identifier])

            raise ValueError


def main():
    calc = SmartCalculator()
    while True:
        calc.process_input()


if __name__ == "__main__":
    main()


