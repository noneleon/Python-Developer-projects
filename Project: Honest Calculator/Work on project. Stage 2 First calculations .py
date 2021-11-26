'''
Description
In this stage, we will continue with the flowchart. Note that the blocks from the previous stage are in red. Be careful; some flows can work differently.


![](https://ucarecdn.com/14a82832-1487-4df0-8e1c-1893247d5193/)
Objectives
Implement the flowchart above. While doing it, please, follow our recommendations:

Don't use the built-in functions to calculate from a string;
The result variable must be of the float type;
Copy the message. The tests will check if the correct message appears in the correct order. So don't add extra lines or characters: msg_3 = "Yeah... division by zero. Smart move..."
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter an equation
> 2 + m
Do you even know what numbers are? Stay focused!
Enter an equation
> 3 n 3
Yes ... an interesting math operation. You've slept through all classes, haven't you?
Enter an equation
> 4 / 0
Yeah... division by zero. Smart move...
Enter an equation
> 4 * 5.2
20.8
Example 2:

Enter an equation
> 411 - 211
200.0
'''

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

running = True
while running:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split()

    try:
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
        print(result)
    elif oper == "-":
        result = x - y
        print(result)
    elif oper == "*":
        result = x * y
        print(result)
    elif oper == "/":
        if y == 0.0:
            print(msg_3)
            continue
        else:
            result = x / y
            print(result)

    running = False
    
\\
# write your code here
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."


def is_digit(x, y):
    try:
        float(x) or int(x)
        float(y) or int(y)
        return float(x), float(y)

    except ValueError:
        return False


def arithmetic_operator(oper):
    if oper not in ['+', '-', '*', '/']:
        return False


def calc(x, oper, y):
    if oper == '-':
        result = x - y
        return result
    elif oper == '+':
        result = x + y
        return result
    if oper == '*':
        result = x * y
        return result
    if oper == '/':
        result = x / y
        return result


print(msg_0)
x, oper, y = input().split()

while True:
    if arithmetic_operator(oper) == False:
        print(msg_2, msg_0, sep='\n')
        x, oper, y = input().split()

    elif is_digit(x, y) == False:
        print(msg_1, msg_0, sep='\n')
        x, oper, y = input().split()

    elif oper == '/' and y == '0':
        print(msg_3, msg_0, sep='\n')
        x, oper, y = input().split()

    else:
        break

x, y = is_digit(x, y)

print(calc(x, oper, y))



\\\
messages = dict({
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move..."
})

operators = dict({
    "+": "add", "-": "sub", "*": "mul", "/": "div"
})

operations = dict(
    add=lambda a, b: a + b,
    sub=lambda a, b: a - b,
    mul=lambda a, b: a * b,
    div=lambda a, b: a / b
)


def read_calc():
    print(messages.get(0))
    data_input = input()
    return data_input.split()


while True:
    x, operator, y = read_calc()
    try:
        x = float(x)
        y = float(y)
        assert operator in list(operators.keys())
        result = operations.get(operators.get(operator))(x, y)
        print(result)
        break
    except ValueError:
        print(messages.get(1))
    except AssertionError:
        print(messages.get(2))
    except ZeroDivisionError:
        print(messages.get(3))

        
\\

while True:
    print("Enter an equation")
    calc = input().split(' ')
    try:
        float(calc[0]) and float(calc[2])
    except:
        print("Do you even know what numbers are? Stay focused!")
        continue
    if calc[1] in '*/+-':
        if calc[1] == '-':
            print(float(calc[0]) - float(calc[2]))
        elif calc[1] == '+':
            print(float(calc[0]) + float(calc[2]))
        elif calc[1] == '*':
            print(float(calc[0]) * float(calc[2]))
        elif calc[1] == '/' and calc[2] != '0':
            print(float(calc[0]) / float(calc[2]))
        else:
            print("Yeah... division by zero. Smart move...")
            continue
        break
    else:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")


