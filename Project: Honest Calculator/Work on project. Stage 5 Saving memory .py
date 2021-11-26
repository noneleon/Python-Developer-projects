'''
Description
To complete the project, you need to implement the flowchart below. The old blocks are red-colored. Be careful; some flows can work differently. The functions from the previous stage have not been changed.
![](https://ucarecdn.com/955100ee-f944-4f79-bcbd-88411017a134/)
Objectives
Implement the flowchart. Please, follow the recommendations below:

Don't use the built-in function eval() to calculate from a string;
Copy the messages below. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter an equation
2 + 3
You are ... lazy
5.0
Do you want to store the result? (y / n):
y
Are you sure? It is only one digit! (y / n)
y
Don't be silly, it's just one number! Add to the memory? (y / n)
n
Do you want to continue calculations? (y / n):
y
Enter an equation
5 + M
You are ... lazy ... very, very lazy
5.0
Do you want to store the result? (y / n):
y
Are you sure? It is only one digit! (y / n)
y
Don't be silly, it's just one number! Add to memory? (y / n)
y
Last chance! Do you really want to embarrass yourself? (y / n)
y
Do you want to continue calculations? (y / n):
y
Enter an equation
M / M
You are ... lazy
1.0
Do you want to store the result? (y / n):
n
Do you want to continue calculations? (y / n):
n
'''
class Calculator:
    def __init__(self):
        self.equation = self.result = self.memory = '0'

    def run(self):
        self.get_equation()
        self.calculate()
        print(self.result)
        self.save()

    def get_equation(self):
        print('Enter an equation')
        self.equation = input().split()
        try:
            for index, choice in enumerate(self.equation):
                if choice == 'M':
                    self.equation[index] = str(self.memory)
            self.check_difficulty()
            float(self.equation[0]) + float(self.equation[2])
            if self.equation[1] not in ['+', '-', '*', '/']:
                print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
                self.get_equation()
            elif self.equation[1] + self.equation[2] == '/0':
                print('Yeah... division by zero. Smart move...')
                self.get_equation()
            else:
                return self.equation
        except ValueError:
            print('Do you even know what numbers are? Stay focused!')
            self.get_equation()

    def calculate(self):
        if self.equation[1] == '+':
            self.result = float(self.equation[0]) + float(self.equation[2])
        elif self.equation[1] == '-':
            self.result = float(self.equation[0]) - float(self.equation[2])
        elif self.equation[1] == '*':
            self.result = float(self.equation[0]) * float(self.equation[2])
        elif self.equation[1] == '/':
            self.result = float(self.equation[0]) / float(self.equation[2])
        return self.result

    def save(self):
        answer = input('Do you want to store the result? (y / n):\n')
        chances = ['Are you sure? It is only one digit! (y / n)\n',
                   "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
                   "Last chance! Do you really want to embarrass yourself? (y / n)\n"]
        if answer == 'y':
            if self.is_one_digit(self.result):
                for chance in chances:
                    answer = input(chance)
                    if answer == 'y':
                        if chance != chances[2]:
                            pass
                        else:
                            self.memory = self.result if int(float(self.result)) != float(self.result) else int(self.result)
                            break
                    elif answer == 'n':
                        break
            else:
                self.memory = self.result if int(float(self.result)) != float(self.result) else int(self.result)
        answer = input('Do you want to continue calculations? (y / n):\n')
        if answer == 'y':
            self.run()
        else:
            exit()

    def check_difficulty(self):
        number1, operator, number2 = self.equation
        message = ''
        if self.is_one_digit(number1) and self.is_one_digit(number2):
            message += ' ... lazy'
        if operator == '*' and '1' in self.equation:
            message += ' ... very lazy'
        if operator in '*+-' and '0' in self.equation:
            message += ' ... very, very lazy'
        if message:
            print(f'You are{message}')

    @staticmethod
    def is_one_digit(number):
        if int(float(number)) == float(number) and -10 < int(float(number)) < 10:
            return True
        else:
            return False


if __name__ == '__main__':
    smart_calc = Calculator()
    smart_calc.run()
    
    
    
\\

run = True
memory = '0'
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = "Are you sure? It is only one digit! (y / n)"
msg_7 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_8 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8]
operations = ['+', '-', '*', '/']
answer = ['y', 'n']


def check_number(number):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    dot = '.'
    digits = list(number)
    size = len(digits)
    counter = 0
    answer = True
    if digits[counter] in numbers:
        counter += 1
        while counter <= size - 2:  # checking for a dot from second position to second-to-last (first and last cannot be dots)
            if digits[counter] in numbers or dot:
                if digits[counter] == dot:  # checking only for digits after we found a dot
                    counter += 1
                    while counter <= size - 1:
                        if digits[counter] in numbers:
                            counter += 1
                        else:
                            answer = False
                            break
                    break
            counter += 1
        if (counter == (size - 1)) and (digits[counter] not in numbers): # checking last digit if dot isn`t present
            answer = False
    else:
        answer = False
    if answer:
        converted_number = float(number)
    else:
        converted_number = 'null'
    return answer, converted_number  # boolean + float if number, boolean = string if isn`t
    
def is_a_digit(number):
    if (-10 < number < 10) and (number == round(number)):
        is_digit = True
    else:
        is_digit = False
    return is_digit
    
def check(number_1, operator, number_2):
    msg_c = ''
    msg_9 = " ... lazy"
    msg_10 = " ... very lazy"
    msg_11 = " ... very, very lazy"
    msg_12 = "You are"
    if is_a_digit(number_1) and is_a_digit(number_2):
        msg_c = msg_c + msg_9
    if (number_1 == 1 or number_2 == 1) and operator == '*':
        msg_c = msg_c + msg_10
    if (number_1 == 0 or number_2 == 0) and (operator == '*' or operator == '+' or operator == '-'):
        msg_c = msg_c + msg_11
    if msg_c != '':
        msg_c = msg_12 + msg_c
        print(msg_c)
    

while run:
    msg_counter = 6
    print(msg[0])
    user_input = input()
    x, oper, y = user_input.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    isx = check_number(x)
    isy = check_number(y)
    if not (isx[0] and isy[0]): 
        print(msg[1])
    elif oper not in operations:
        print(msg[2])
    else:
        check(isx[1], oper, isy[1])
        if oper == operations[0]:
            result = isx[1] + isy[1]
        elif oper == operations[1]:
            result = isx[1] - isy[1]
        elif oper == operations[2]:
            result = isx[1] * isy[1]
        elif oper == operations[3]:
            if isy[1] == 0:
                result = msg[3]
            else:
                result = isx[1] / isy[1]
        print(result)
        if result != msg[3]:
            print(msg[4])
            choose = input()
            if choose == answer[0] and is_a_digit(result): # loop with silly questions
                while msg_counter < 9:
                    print(msg[msg_counter])
                    choose = input()
                    if choose == answer[0]:
                        msg_counter += 1
                    else:
                        break
            if choose == answer[0] or msg_counter == 9:  # msg_counter will always be 9 with answer yes
                memory = str(result)                     # choosing 'no' in the loop will give us 2 falses
            print(msg[5])
            choose = input()
            if choose == answer[1]:
                run = False
                
                
                
rom math import trunc

messages = {'msg_0': 'Enter an equation',
            'msg_1': 'Do you even know what numbers are? Stay focused!',
            'msg_2': 'Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?',
            'msg_3': 'Yeah... division by zero. Smart move...',
            'msg_4': 'Do you want to store the result? (y / n):',
            'msg_5': 'Do you want to continue calculations? (y / n):',
            'msg_6': ' ... lazy',
            'msg_7': ' ... very lazy',
            'msg_8': ' ... very, very lazy',
            'msg_9': 'You are',
            'msg_10': "Are you sure? It is only one digit! (y / n)",
            'msg_11': "Don't be silly! It's just one number! Add to the memory? (y / n)",
            'msg_12': "Last chance! Do you really want to embarrass yourself? (y / n)"}


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
    while usr_input not in 'yn':
        usr_input = input().lower()
    return usr_input


def is_one_digit(v):
    return float(v) == trunc(float(v)) and -10 < float(v) < 10


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages['msg_6']
    if v1 == '1' or v2 == '1' and v3 == '*':
        msg += messages['msg_7']
    if v1 == '0' or v2 == '0' and v3 in '*+-':
        msg += messages['msg_8']
    if msg:
        msg = messages['msg_9'] + msg
        print(msg)


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
    elif operator not in '+-*/':
        print(messages['msg_2'])

    else:
        check(str(x), str(y), operator)
        if operator == '/' and float(y) == 0:
            print(messages['msg_3'])
            continue
        result = calculate(float(x), operator, float(y))
        print(result)
        print(messages['msg_4'])
        answer = get_answer()
        if answer == 'y':
            if is_one_digit(result):
                for idx, message in list(messages.items())[-3:]:
                    print(message)
                    answer = get_answer()
                    if answer == 'n':
                        break
                    if idx == 'msg_12':
                        memory = result
            else:
                memory = result
        print(messages['msg_5'])
        answer = get_answer()
        if answer == 'n':
            break


