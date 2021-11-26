'''
Description
In the final stage, it remains to add operations: multiplication *, integer division / and parentheses (...). They have a higher priority than addition + and subtraction -.

Here is an example of an expression that contains all possible operations:

3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)
The result is 121.

A general expression can contain many parentheses and operations with different priorities. It is difficult to calculate such expressions if you do not use special methods. Fortunately, there is a fairly effective and universal solution, using a stack, to calculate the most general expressions.

From infix to postfix

Earlier we processed expressions written in infix notation. This notation is not very convenient if an expression has operations with different priorities, especially when brackets are used. But we can use postfix notation, also known as Reverse Polish notation (RPN). In this notation, operators follow their operands. See several examples below.

Infix notation 1:

3 + 2 * 4
Postfix notation 1:

3 2 4 * +
Infix notation 2:

2 * (3 + 4) + 1
Postfix notation 2:

2 3 4 + * 1 +
To better understand the postfix notation, you can play with a converter.

As you can see, in postfix notation operations are arranged according to their priority and parentheses are not used at all. So, it is easier to calculate expressions written in postfix notation.

You can use a stack (LIFO) to convert an expression from infix to postfix notation. The stack is used to store operators for reordering. Here are some rules that describe how to create an algorithm that converts an expression from infix to postfix notation.

Add operands (numbers and variables) to the result (postfix notation) as they arrive.
If the stack is empty or contains a left parenthesis on top, push the incoming operator on the stack.
If the incoming operator has higher precedence than the top of the stack, push it on the stack.
If the precedence of the incoming operator is lower than or equal to that of the top of the stack, pop the stack and add operators to the result until you see an operator that has smaller precedence or a left parenthesis on the top of the stack; then add the incoming operator to the stack.
If the incoming element is a left parenthesis, push it on the stack.
If the incoming element is a right parenthesis, pop the stack and add operators to the result until you see a left parenthesis. Discard the pair of parentheses.
At the end of the expression, pop the stack and add all operators to the result.
No parentheses should remain on the stack. Otherwise, the expression has unbalanced brackets. It is a syntax error.

Calculating the result

When we have an expression in postfix notation, we can calculate it using another stack. To do that, scan the postfix expression from left to right:

If the incoming element is a number, push it into the stack (the whole number, not a single digit!).
If the incoming element is the name of a variable, push its value into the stack.
If the incoming element is an operator, then pop twice to get two numbers and perform the operation; push the result on the stack.
When the expression ends, the number on the top of the stack is a final result.
Here you can find an example and additional explanations on postfix expressions.

Objectives
Your program should support multiplication *, integer division / and parentheses (...). To do this, use infix to postfix conversion algorithm above and then calculate the result using stack.
Do not forget about variables; they, and the unary minus operator, should still work.
Modify the result of the /help command to explain all possible operators. You can write the output for the command in free form.
The program should not stop until the user enters the /exit command.
Note that a sequence of + (like +++ or +++++) is an admissible operator that should be interpreted as a single plus. A sequence of - (like -- or ---) is also an admissible operator and its meaning depends on the length. If a user enters a sequence of * or /, the program must print a message that the expression is invalid.
As a bonus, you may add the power operator ^ that has a higher priority than * and /.
> 2^2
4
> 2*2^3
16
Examples
The greater-than symbol followed by a space (>) represents the user input.

> 8 * 3 + 12 * (4 - 2)
48
> 2 - 2 + 3
3
> 4 * (2 + 3
Invalid expression
> -10
-10
> a=4
> b=5
> c=6
> a*2+b*3+c*(2+3)
53
> 1 +++ 2 * 3 -- 4
11
> 3 *** 5
Invalid expression
> 4+3)
Invalid expression
> /command
Unknown command
> /exit
Bye!

'''

"""The program performs simple mathematic operations based on user input"""

from collections import deque

class Calculator:

    precedence = {"^":3, "*": 2, "/": 2, "+": 1, "-": 1}

    def __init__(self):
        self.variables = {}

    def addition(self, nums):
        """method used for adding numbers"""
        total = 0
        for i, num in enumerate(nums):
            value = 0
            if "-" in num or "+" in num:
                pass
            elif num in self.variables:
                value = int(self.variables[num])
            else:
                value = int(num)
            if i == 0:
                total += value
            elif "-" in num or "+" in num:
                continue
            else:
                if self.negative_num(nums[i-1]):
                    total += (value * -1)
                else:
                    total += value
        return total

    def negative_num(self, operators):
        """method used to check if a number is negative"""
        if operators.count("-") % 2 == 0:
            return False
        return True


    def variable(self, inp):
        """method used to store variables from user input into a dictionary"""
        var = inp.split("=")[0].strip()
        value = inp.split("=")[1].strip()
        if value in self.variables:
            value = self.variables[value]
        if self.ok_var(var) and self.ok_value(value):
            self.variables[var] = value
        else:
            print("Invalid identifier")

    def ok_var(self, var):
        """method user to check if a variable name is correct"""
        if not var.isalpha():
            return False
        return True

    def ok_value(self, value):
        """method used to check the value introduced is numeric"""
        if not value.replace("-", "").isdigit():
            return False
        return True

    def reversedPolish(self, expression):
        """method used to transform users input from infix to postfix notation"""
        output_exp = []
        operators = deque()
        temp = None
        for _, item in enumerate(expression):
            if item.isnumeric():
                output_exp.append(item)
            elif item in self.variables:
                output_exp.append(self.variables[item])
            elif len(operators) == 0 or operators[-1] == "(":
                operators.append(item)
            elif item == "(":
                operators.append(item)
            elif item == ")":
                temp = operators.pop()
                while temp != "(":
                    output_exp.append(temp)
                    temp = operators.pop()
            elif self.precedence[item] > self.precedence[operators[-1]]:
                operators.append(item)
            elif self.precedence[item] <= self.precedence[operators[-1]]:
                temp = operators.pop()
                while self.precedence[temp] < self.precedence[item]:
                    output_exp.append(temp)
                    temp = operators.pop()
                operators.append(item)
                output_exp.append(temp)
        if len(operators) != 0:
            while len(operators) > 0:
                output_exp.append(operators.pop())

        return output_exp

    def evaluate(self, a, b, operator):
        """method used to evaluate operators in user input and perform calculation acordingly"""
        if operator == "^":
            return a ** b
        elif operator == '*':
            return a*b
        elif operator == '/':
            return a//b
        elif operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        else:
            return None

    def calculate(self, exp):
        """method used to perform calculation using postfix notation"""
        postfix = self.reversedPolish(exp)
        result = deque()

        for i in postfix:
            if i.isnumeric():
                result.append(int(i))
            else:
                temp = result.pop()
                tmp = result.pop()
                result.append(self.evaluate(int(tmp), int(temp), i))

        return result[0]



def commands(user_input):
    """funtion used to evaluate user's commands"""
    if user_input == "/help":
        print("The program performs simple mathematic operations based on user input")
        return False
    elif user_input == "/exit":
        print("Bye!")
        return True
    else:
        print("Unknown command")
        return False

def errors(usr_input):
    """functions check's user input for errors such as double operators(excluding + and -)"""
    for i, ch in enumerate(usr_input):
        if ch == "*" and usr_input[i + 1] == "*":
            return True
        elif ch == "/" and usr_input[i + 1] == "/":
            return True

    if "(" in usr_input and ")" in usr_input:
        if usr_input.index(")") < usr_input.index("("):
            return True

    if usr_input.count("(") != usr_input.count(")"):
        return True
    return False


def parse_input(inp_string):
    """function parses user input and change multiple + and - operators to single operator"""
    neg_start = False
    temp = []
    parsed_string = inp_string.replace(' ', '')
    parse_list = []
    for i, c in enumerate(parsed_string):
        # group all common characters
        if i == 0 and c == '-':
            neg_start = True
        elif i+1 == len(parsed_string):
            if temp != [] and c.isnumeric():
                temp.append(c)
                parse_list.append(''.join(temp))
                temp.clear()
            else:
                if temp != []:
                    parse_list.append(''.join(temp))
                temp.clear()
                parse_list.append(c)
        elif c == '*' or c == '/' or c == '(' or c == ')':
            parse_list.append(c)
        elif c.isnumeric() and (parsed_string[i+1].isnumeric()):
            temp.append(c)
        elif c.isnumeric() and not parsed_string[i+1].isnumeric():
            temp.append(c)
            parse_list.append(''.join(temp))
            temp.clear()
        elif c.isalpha() and parsed_string[i+1].isalpha():
            temp.append(c)
        elif c.isalpha() and not parsed_string[i+1].isalpha():
            temp.append(c)
            parse_list.append(''.join(temp))
            temp.clear()
        elif c == '-' and parsed_string[i + 1] == '-':
            temp.append(c)
        elif c == '-' and not parsed_string[i + 1] == '-':
            temp.append(c)
            parse_list.append(''.join(temp))
            temp.clear()
        elif c == '+' and parsed_string[i + 1] == '+':
            temp.append(c)
        elif c == '+' and not parsed_string[i + 1] == '+':
            temp.append(c)
            parse_list.append(''.join(temp))
            temp.clear()
        else:
            pass

    if neg_start:
        parse_list[0] *= -1
    # replace groups of - and + with single characters
    for i, c in enumerate(parse_list):
        if '+' in c:
            parse_list[i] = '+'
        elif '-' in c:
            if c.count('-') % 2 == 0:
                parse_list[i] = '+'
            else:
                parse_list[i] = '-'
    return parse_list


if __name__ == '__main__':
    EXT = False
    calculator = Calculator()
    while EXT is False:
        user_input = input().strip()
        if user_input.startswith('/'):
            EXT = commands(user_input)
        elif user_input == '':
            continue
        elif '=' in user_input:
            calculator.variable(user_input)
        elif user_input.isalpha():
            if user_input in calculator.variables:
                print(calculator.variables[user_input])
            else:
                print('Unknown variable')
        elif user_input.replace("-", "").isnumeric():
            print(user_input)
        elif errors(user_input):
            print('Invalid expression')
            continue
        else:
            calc = parse_input(user_input)
            print(calculator.calculate(calc))

            
\\
import string
from collections import deque


class Calculator:
    def __init__(self):
        self.variable = Variable()
        self.postfix = deque()
        self.operations = deque()

    def main(self):
        while True:
            data = input()
            if data.startswith("/"):
                self.command(data)
            elif data == "":
                continue
            else:
                err = self.check_valid(data)
                if not err:
                    if "=" in data:
                        data = data.replace(" ", "")
                        key, value = data.split("=")[0], data.split("=")[1]
                        self.variable.set(key, value)
                        continue
                    else:
                        self.calculate(data)
            self.postfix = deque()

    def calculate(self, expression):
        expression = expression.replace(" ", "")
        data = []
        n = ""
        o = ""
        digit = False
        _ = 0
        for i in expression:
            if i in "+-":
                if digit:
                    data.append(n)
                    n = ""
                    digit = False
                if not i.isdigit():
                    if i == "+" and o == "":
                        o = "+"
                    elif i != "+" and o == "+":
                        data.append(o)
                        o = ""
                    if i == "-":
                        _ += 1
                        o = "-"
                    elif i != "-" and o == "-":
                        if _ % 2:
                            data.append("-")
                        else:
                            data.append("+")
                        o = ""
                        _ = 0
            else:
                if i.isdigit():
                    n += i
                    digit = True
                else:
                    if n:
                        data.append(n)
                        digit = False
                        n = ""
                if o == "+":
                    data.append(o)
                    o = ""
                elif o == "-":
                    if _ % 2:
                        data.append("-")
                    else:
                        data.append("+")
                    o = ""
                    _ = 0
                if not i.isdigit():
                    data.append(i)
        if n:
            data.append(n)
        self.infix_to_postfix(data)
        main = deque()
        for i in self.postfix:
            if isinstance(i, int):
                main.append(i)
            else:
                b = main.pop()
                a = main.pop()
                main.append(eval(f"{a} {i} {b}"))
        if main:
            print(int(main.pop()))

    def infix_to_postfix(self, expression: list):
        for i in expression:
            if i.isdigit():
                i = int(i)
            if isinstance(i, str) and i not in "+-/*()":
                i = self.variable.get(i)
                if not isinstance(i, int):
                    return
            if isinstance(i, int):
                self.postfix.append(i)
            elif not self.operations:  # deque is empty
                self.operations.append(i)
            elif i == "(":
                self.operations.append(i)
            elif i == ")":
                while True:
                    operation = self.operations.pop()
                    if operation != "(":
                        self.postfix.append(operation)
                    else:
                        break
            elif self.operations[-1] == "(":
                self.operations.append(i)
            else:
                while True:
                    if self.operations and self.operations[-1] != '(' and \
                            self.priority(i) <= self.priority(self.operations[-1]):
                        self.postfix.append(self.operations.pop())
                    else:
                        self.operations.append(i)
                        break
        while self.operations:
            self.postfix.append(self.operations.pop())

    @staticmethod
    def priority(z):
        if z in ['×', '*', '/']:
            return 2
        elif z in ['+', '-']:
            return 1

    @staticmethod
    def check_valid(data):
        if data.endswith("+") or data.endswith("-"):
            print("Invalid expression")
            return True
        if ("(" in data and ")" not in data) or ("(" not in data and ")" in data) or "**" in data or "//" in data:
            # 单括号
            print("Invalid expression")
            return True

    @staticmethod
    def command(cmd):
        if cmd == "/help":
            print("A calculator program")
        elif cmd == "/exit":
            print("Bye!")
            exit()
        else:
            print("Unknown command")


class Variable(dict):
    def get(self, key):
        result = super().get(key)
        if isinstance(result, int):
            return result
        else:
            print("Unknown variable")

    def set(self, key, value) -> None:
        v1 = self.test_var(key, mode="key")
        if v1:
            v2 = self.test_var(value, mode="value")
            if v2:
                try:
                    value = int(value)
                except ValueError:
                    value = value = super().get(value)
                self[key] = value

    def test_var(self, v, mode) -> bool:
        if mode == "key":
            for i in string.digits:
                if i in v:
                    print("Invalid identifier")
                    return False
            return True
        elif mode == "value":
            try:
                v = int(v)
            except ValueError:
                value = super().get(v)
                if not isinstance(value, int):
                    print("Invalid assignment")
                else:
                    return True
            else:
                return True  # No ascii letters


if __name__ == "__main__":
    c = Calculator()
    c.main()

    
\\

import calculator_token
import calculator_error
from typing import Union


class Calculator:
    """Process expressions

    input string - command, assignment or expression
    command - /help or /exit
    assignment - variable = expression
    expression contains operands, binary operations and parenthesis
    expressions should be writen in infix notation
    operand - variable or integer
    binary operation - plus '+', minus '-', integer division '/' or subtraction '-'
    """

    @staticmethod
    def parse_expr(expr: str) -> list[calculator_token.Token]:
        result = []
        i = 0
        while i < len(expr):
            if expr[i].isspace():
                i += 1
                continue
            if expr[i].isdigit():
                number = 0
                while i < len(expr) and expr[i].isdigit():
                    number = number * 10 + int(expr[i])
                    i += 1
                result.append(calculator_token.Number(number))
            elif expr[i].isalpha():
                var_name = ""
                while i < len(expr) and expr[i].isalpha():
                    var_name += expr[i]
                    i += 1
                result.append(calculator_token.VariableName(var_name))
            elif expr[i] in {'+', '-'}:
                operation = ""
                while i < len(expr) and expr[i] in {'+', '-'}:
                    operation += expr[i]
                    i += 1
                if operation.count('-') % 2:
                    result.append(calculator_token.Sub())
                else:
                    result.append(calculator_token.Plus())
            elif expr[i] == '*':
                result.append(calculator_token.Mult())
                i += 1
            elif expr[i] == '/':
                result.append(calculator_token.Div())
                i += 1
            elif expr[i] == '(':
                result.append(calculator_token.LeftParenthesis())
                i += 1
            elif expr[i] == ')':
                result.append(calculator_token.RightParenthesis())
                i += 1
            else:
                raise calculator_error.InvalidExpr()
        return result

    def __init__(self):
        self.variables = dict()

    @staticmethod
    def from_infix_to_postfix_notation(tokens: list[calculator_token.Token]) -> list[calculator_token.Token]:
        """uses Shunting-yard-algorithm"""
        result = []
        stack = []
        for token in tokens:
            if isinstance(token, calculator_token.Operand):
                result.append(token)
            elif isinstance(token, calculator_token.BinOp):
                while (stack and isinstance(stack[-1], calculator_token.BinOp)
                       and stack[-1].precedence >= token.precedence):
                    result.append(stack.pop())
                stack.append(token)
            elif isinstance(token, calculator_token.LeftParenthesis):
                stack.append(token)
            elif isinstance(token, calculator_token.RightParenthesis):
                while stack and not isinstance(stack[-1], calculator_token.LeftParenthesis):
                    result.append(stack.pop())
                if not stack:
                    raise calculator_error.InvalidExpr()
                stack.pop()
            else:
                raise calculator_error.InvalidExpr()
        while stack:
            if isinstance(stack[-1], calculator_token.LeftParenthesis):
                raise calculator_error.InvalidExpr()
            result.append(stack.pop())
        return result

    def eval_expression(self, expr: str) -> int:
        tokens = Calculator.parse_expr(expr)
        tokens = self.from_infix_to_postfix_notation(tokens)
        if not tokens:
            raise calculator_error.InvalidExpr()
        values = []
        for token in tokens:
            if isinstance(token, calculator_token.Operand):
                values.append(token.get_value(self.variables))
            elif isinstance(token, calculator_token.BinOp):
                if len(values) < 2:
                    raise calculator_error.InvalidExpr()
                rhs = values.pop()
                lhs = values.pop()
                values.append(token.eval(lhs, rhs))
            else:
                raise calculator_error.InvalidExpr()
        if len(values) != 1:
            raise calculator_error.InvalidExpr()
        return values[0]

    def process_expression(self, expr: str) -> Union[int, None]:
        parts = tuple(expr.split("=", maxsplit=1))
        if len(parts) == 2:
            left_hand, right_hand = parts
            try:
                left_hand_tokens = Calculator.parse_expr(left_hand)
            except:
                raise calculator_error.InvalidId()
            if len(left_hand_tokens) != 1 or type(left_hand_tokens[0]) != calculator_token.VariableName:
                raise calculator_error.InvalidId()
            var_name = left_hand_tokens[0].name
            try:
                self.variables[var_name] = self.eval_expression(right_hand)
            except:
                raise calculator_error.InvalidAssign()
        else:
            return self.eval_expression(parts[0])

    def run(self):
        while True:
            inp = input()
            if not inp:
                continue
            if inp[0] == '/':
                command = inp[1:]
                if command == "exit":
                    print("Bye!")
                    break
                elif command == "help":
                    print(Calculator.__doc__)
                else:
                    print("Unknown command")
            else:
                try:
                    expr_res = self.process_expression(inp)
                    if expr_res is not None:
                        print(expr_res)
                except Exception as e:
                    print(e)


def main():
    calculator = Calculator()
    calculator.run()


main()
calculator/calculator_error.py
class InvalidExpr(Exception):
    def __init__(self):
        super().__init__("Invalid expression")


class InvalidId(Exception):
    def __init__(self):
        super().__init__("Invalid identifier")


class UnknownVar(Exception):
    def __init__(self):
        super().__init__("Unknown variable")


class InvalidAssign(Exception):
    def __init__(self):
        super().__init__("Invalid assignment")
calculator/calculator_token.py
import calculator_error
from abc import ABC, abstractmethod


class Token(ABC):
    pass


class BinOp(Token):
    def __init__(self, precedence: int):
        self.precedence = precedence

    @abstractmethod
    def eval(self, lhs: int, rhs: int) -> int:
        ...


class Plus(BinOp):
    def __init__(self):
        super().__init__(1)

    def eval(self, lhs: int, rhs: int) -> int:
        return lhs + rhs


class Sub(BinOp):
    def __init__(self):
        super().__init__(1)

    def eval(self, lhs: int, rhs: int) -> int:
        return lhs - rhs


class Mult(BinOp):
    def __init__(self):
        super().__init__(2)

    def eval(self, lhs: int, rhs: int) -> int:
        return lhs * rhs


class Div(BinOp):
    def __init__(self):
        super().__init__(2)

    def eval(self, lhs: int, rhs: int) -> int:
        if rhs == 0:
            raise ZeroDivisionError()
        return lhs // rhs


class Operand(Token):
    @abstractmethod
    def get_value(self, variables: dict) -> int:
        ...


class Number(Operand):
    def __init__(self, value):
        self.value = value

    def get_value(self, variables: dict) -> int:
        return self.value


class VariableName(Operand):
    def __init__(self, name):
        self.name = name

    def get_value(self, variables: dict) -> int:
        if self.name not in variables:
            raise calculator_error.UnknownVar
        return variables[self.name]


class LeftParenthesis(Token):
    pass


class RightParenthesis(Token):
    pass
