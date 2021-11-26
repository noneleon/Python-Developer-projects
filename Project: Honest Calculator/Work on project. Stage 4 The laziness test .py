'''
Description
Implement the flowchart below. Take a good look — there're two functions. The old blocks are in red. Be careful; some flows can now work differently.

![](https://ucarecdn.com/0706cb45-ffba-4f2e-ab19-ab635467da58/)
Objectives
Implement the flowchart with two functions. Please, mind the recommendations below:

Don't use the built-in function eval() to calculate from a string;
Copy the messages carefully. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter an equation
> 2 / M
You are ... lazy
Yeah... division by zero. Smart move...
Enter an equation
> 1 * M
You are ... lazy ... very lazy ... very, very lazy
0.0
Do you want to store the result? (y / n):
> n
Do you want to continue calculations? (y / n):
> y
Enter an equation
> 899 * 0
You are ... very, very lazy
0.0
Do you want to store the result? (y / n):
> n
Do you want to continue calculations? (y / n):
> n


'''
import re

ops = ['+', '-', '/', '*']


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

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


def is_one_digit(v):
  if v == 0:
    return True
  elif -10 < v < 10 and v.is_integer():
    return True
  else:
    return False

def check(v1, v2, v3):
  msg = ""
  output_1 = is_one_digit(v1)
  output_2 = is_one_digit(v2)

  if output_1 and output_2:
    msg = msg + msg_6
  if (v1 == 1 or v2 == 1) and v3 == "*":
    msg = msg + msg_7
  if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
    msg = msg + msg_8
  if msg != "":
    msg = msg_9 + msg
    print(msg)
  return

def initiate_calcuations(memory):
  print(msg_0)
  user_input = input()
  arr = user_input.split(" ")
  x = check_numeric(arr[0], memory)
  y = check_numeric(arr[2], memory)
  oper = arr[1]

  if check_exceptions(x, y, oper) == True:
    return 

  check(x, y, oper)

  if oper == "/" and y == 0:
    print(msg_3)
    return initiate_calcuations(memory)

  result = calculate_result(x, y, oper)
  print(result)
  memory = check_answer_1(result)

  return check_answer_2(memory)

initiate_calcuations(0)



\\

memory = 0


def msg(x):
    msg_0 = "Enter an equation"
    x == 0 and print(msg_0)
    msg_1 = "Do you even know what numbers are? Stay focused!"
    x == 1 and print(msg_1)
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    x == 2 and print(msg_2)
    msg_3 = "Yeah... division by zero. Smart move..."
    x == 3 and print(msg_3)
    msg_4 = "Do you want to store the result? (y / n):"
    x == 4 and print(msg_4)
    msg_5 = "Do you want to continue calculations? (y / n):"
    x == 5 and print(msg_5)
    msg_6 = " ... lazy"
    x == 6 and print(msg_6)
    msg_7 = " ... very lazy"
    x == 7 and print(msg_7)
    msg_8 = " ... very, very lazy"
    x == 8 and print(msg_8)
    msg_9 = "You are"
    x == 9 and print(msg_9)


def is_one_digit(d):
    if d in range(-10, 11):
        return True
    else:
        return False


def check(v1, v2, v3):
    mes = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        mes += msg_6

    if (v1 == 1 or v2 == 1) and v3 == '*':
        mes += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        mes += msg_8

    if mes != "":
        mes = msg_9 + mes
        print(mes)
    return


def check_input(x, y):
    global memory
    x = memory if 'M' == x else x
    y = memory if 'M' == y else y
    try:
        float(x)
        float(y)
        return float(x), float(y)
    except ValueError:
        msg(1)
        return False


def zero_div(oper, y):
    if oper == '/':
        if y == 0:
            msg(3)
            return False
    else:
        return True


def calc(oper, x, y):
    if oper == '+':
        result = x + y
        return result
    elif '-' in oper:
        result = x - y
        return result
    elif '*' in oper:
        result = x * y
        return result
    elif '/' in oper:
        result = x / y
        return result


def oper_check_perform(oper, x, y):
    if '+' in oper or '-' in oper or '*' in oper or '/' in oper:
        return calc(oper, x, y)
    else:
        msg(2)


def store_result_check(answer):
    if answer == 'y':
        return True
    elif answer == 'n':
        return True
    else:
        return False


def result_store(result):
    global memory
    memory = result
    return memory


def block_1():
    while True:
        msg(0)
        x, oper, y = input().split()
        if not check_input(x, y):
            continue
        x, y = check_input(x, y)
        check(x, y, oper)
        if not zero_div(oper, y):
            continue
        result = oper_check_perform(oper, x, y)
        print(result)
        return result


def block_2(result):
    while True:
        msg(4)
        answer = input()
        if not store_result_check(answer):
            continue
        if 'y' in answer:
            result_store(result)
            break
        if 'n' in answer:
            break


def contin_calc():
    while True:
        msg(5)
        answer = input()
        if 'y' in answer:
            return False
        if 'n' in answer:
            return True
        else:
            continue


def main():
    while True:
        block_2(block_1())
        msg(5)
        answer = input()
        if 'y' in answer:
            continue
        if 'n' in answer:
            break


main()


\\

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if (v1 == "1" or v2 == "1") and v3 == "*":
        msg += messages[7]
    if (v1 == "0" or v2 == "0") and v3 in ["*", "+", "-"]:
        msg += messages[8]
    if msg != "":
        msg = messages[9] + msg
        print(msg)


def is_one_digit(v):
    # Check if v is integer, or if it is a float check if it has decimals
    if (v.isdigit() or v.replace(".", "", 1).isdigit() and float(v) % 1 == 0.0) and -10 < float(v) < 10:
        output = True
    else:
        output = False
    return output


messages = {0: "Enter an equation",
            1: "Do you even know what numbers are? Stay focused!",
            2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            3: "Yeah... division by zero. Smart move...",
            4: "Do you want to store the result? (y / n):",
            5: "Do you want to continue calculations? (y / n):",
            6: " ... lazy",
            7: " ... very lazy",
            8: " ... very, very lazy",
            9: "You are"}

memory = 0
end = False

# Main loop
while not end:

    # Calculation loop
    while True:
        print(messages[0])
        x, oper, y = input().split()
        x = str(memory) if x == "M" else x
        y = str(memory) if y == "M" else y
        if (x.isdigit() or x.replace(".", "", 1).isdigit() and x.count(".") < 2) and \
                (y.isdigit() or y.replace(".", "", 1).isdigit() and y.count(".") < 2):
            pass
        else:
            print(messages[1])
            continue
        if oper not in ["+", "-", "*", "/"]:
            print(messages[2])
            continue
        check(x, y, oper)
        if oper == "+":
            result = float(x) + float(y)
            break  # jump to print result
        if oper == "-":
            result = float(x) - float(y)
            break  # jump to print result
        if oper == "*":
            result = float(x) * float(y)
            break  # jump to print result
        if oper == "/" and float(y):
            result = float(x) / float(y)
            break  # jump to print result
        print(messages[3])

    print(result)

    # Store the result loop
    while True:
        print(messages[4])
        answer = input()
        if answer == "y":
            memory = result
            break  # jump to continue calculations loop
        elif answer != "n":
            continue
        break  # jump to continue calculations loop

    # Continue calculations loop
    while True:
        print(messages[5])
        answer = input()
        if answer == "y":
            break  # jump back to calculation loop
        if answer != "n":
            continue
        end = True  # finish main loop
        break

        


