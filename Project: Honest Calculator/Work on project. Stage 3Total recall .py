'''
Take a look at the upgraded flowchart. As before, the old blocks are red-colored. Be careful; some flows can now work differently.

![](https://ucarecdn.com/4a899d94-c524-48f1-8bfe-04ea9139172b/)
Objectives
To complete this stage, you need to implement the flowchart above. While doing it, please, follow our recommendations below:

Don't use the built-in function eval() to calculate from a string;
The memory variable must be of a float type;
There are no tests when M is negative. For example, there will be no test input like this: -M + 6;
Copy two messages. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter an equation
> 3 + 3
6
Do you want to store the result? (y / n):
>y
Do you want to continue calculations? (y / n):
>y
> 5 + M
11
Do you want to store the result? (y / n):
>y
Do you want to continue calculations? (y / n):
>n
'''

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

running = True
memory = 0
while running:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split()

    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    valid_oper = "+-*/"
    if oper not in valid_oper:
        print(msg_2)
        continue

    result = 0
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        if y == 0.0:
            print(msg_3)
            continue
        else:
            result = x / y

    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            running = False
\\

# FLOWCHARTS


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

operations = ['+', '-', '*', '/']

memory = 0.0

def askq():
    global calc, x, y, oper
    calc = input(f"{msg_0} \n")
    x, oper, y = calc.split(" ")

def checknum():
    global x, y, oper
    if x == "M":
        x = memory
    elif y == "M":
        y = memory
    elif x.isalpha():
        print(msg_1)
        play()
    elif y.isalpha():
        print(msg_1)
        play()

def division_by_zero():
    global x, y, oper
    if oper == "/" and float(y) == 0:
        print(msg_3)
        play()

def operation_check():
    global x, y, oper
    if oper not in operations:
        print(msg_2)
        play()

def print_calc():
    global x, y, oper, result
    if oper == "+":
        result = float(x) + float(y)
    elif oper == "-":
        result = float(x) - float(y)
    elif oper == "*":
        result = float(x) * float(y)
    elif oper == "/":
        result = float(x) / float(y)
    print(result)

def store_result():
    global memory, result
    print(msg_4)
    answ  = input()
    if answ == 'y':
        memory = result

def more_calcs():
    print(msg_5)
    answ  = input()
    if answ == 'y':
        calculator()


def play():
    askq()
    checknum()
    operation_check()
    division_by_zero()

def calculator():
    play()
    print_calc()
    store_result()
    more_calcs()

calculator()


\\

messages = {'msg_0': 'Enter an equation',
            'msg_1': 'Do you even know what numbers are? Stay focused!',
            'msg_2': 'Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?',
            'msg_3': 'Yeah... division by zero. Smart move...',
            'msg_4': 'Do you want to store the result? (y / n):',
            'msg_5': 'Do you want to continue calculations? (y / n):'}


def is_valid(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def calculate(x, operator, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y


def get_answer():
    usr_input = input().lower()
    while usr_input not in ('y', 'n'):
        usr_input = input().lower()
    return usr_input


memory = 0

while True:
    print(messages['msg_0'])
    x, operator, y = input().split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    if not (is_valid(x) and is_valid(y)):
        print(messages['msg_1'])
    elif operator not in ('+', '-', '*', '/'):
        print(messages['msg_2'])
    elif operator == '/' and float(y) == 0:
        print(messages['msg_3'])
    else:
        result = calculate(float(x), operator, float(y))
        print(result)
        print(messages['msg_4'])
        answer = get_answer()
        if answer == 'y':
            memory = result
        print(messages['msg_5'])
        answer = get_answer()
        if answer == 'n':
            break

\\


import re

ops = ['+', '-', '/', '*']


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

def check_numeric(n, memory_val):
  integer_pattern = re.compile('[0-9]+')
  float_pattern = re.compile('[0-9]+\.[0-9]+')
  if n == "M":
    return memory_val
  elif integer_pattern.match(n):
    return float(n)
  elif float_pattern.match(n):
    return float(n)
  else:
    return "unknown symbol"

def calculate_result(x, y, oper):
  if oper == "/":
    return x / y
  elif oper == "*":
    return x * y
  elif oper == "+":
    return x + y 
  elif oper == "-":
    return x - y 


def check_exceptions(x, y, oper):
  if x == "unknown symbol" or y == "unknown symbol":
    print(msg_1)
    return True
  elif oper not in ops:
    print(msg_2)
    return True

def check_answer_1(result):
  print(msg_4)
  answer_1 = input()
  if answer_1 == 'y':
    return result
  elif answer_1 == 'n':
    return 0
  else:
    check_answer_1(result)


def check_answer_2(memory):
  print(msg_5)
  answer_2 = input()
  if answer_2 == 'y':
    initiate_calcuations(memory)
  elif answer_2 == 'n':
    return
  else:
    check_answer_2()


def initiate_calcuations(memory):
  print(msg_0)
  user_input = input()
  arr = user_input.split(" ")
  x = check_numeric(arr[0], memory)
  y = check_numeric(arr[2], memory)
  oper = arr[1]

  if oper == "/" and y == 0:
    print(msg_3)
    return initiate_calcuations(memory)

  if check_exceptions(x, y, oper) == True:
    return 

  result = calculate_result(x, y, oper)
  print(result)
  memory = check_answer_1(result)

  return check_answer_2(memory)

initiate_calcuations(0)
