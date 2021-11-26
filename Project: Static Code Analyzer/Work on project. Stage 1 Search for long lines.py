'''
Description
To make sure your Python code is beautiful and consistently formatted, you should follow the PEP8 specification and best practices recommended by the Python community. This is not always easy, especially for beginners. Luckily, there are special tools called static code analyzers (pylint, flake8, and others) that automatically check that your code meets all the standards and recommendations. These tools don't execute your code but just analyze it and output all the issues they find.

In this project, you will create a small static analyzer tool that finds some common stylistic mistakes in Python code. This way, you will familiarize yourself with the concept of static code analysis and improve your Python skills along the way.

PEP8 requires that we should "limit all lines to a maximum of 79 characters", which is designed to make your code more readable. So let's first make a program that checks that code lines are not too long.

Objectives
In this stage, your program should read Python code from a specified file and perform a single check: the length of code lines should not exceed 79 characters.

Note that:

The path to the file is obtained from standard input.
The general output format is:
Line X: Code Message
In the format:

X is the number of the line where the issue was found. The count starts from one.

Code is the code of the discovered stylistic issue (like S001).

Message is a human-readable description of the issue (optional).

For example:

Line 3: S001 Too long
This format will be used throughout the project with some minor changes.

The order of the lines should always be first to last.
Your program can output another message instead of Too long. The rest of the output must exactly match the provided example. In the code S001, S means a stylistic issue, and 001 is the internal number of the issue.
Examples
Here is an example of the file's contents:

print('What\'s your name?')
name = input()
print(f'Hello, {name}')  # here is an obvious comment: this prints a greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)
This code contains two long lines (>79 characters): lines 3 and 5.

Here is the expected output for the given example:

Line 3: S001 Too long
Line 5: S001 Too long
'''
def main():
    path = input()
    with open(path, 'r') as file:
        for i, line in enumerate(file.readlines()):
            if len(line) > 79:
                print(f'Line {i + 1}: S001 Too long')


if __name__ == '__main__':
    main()
    
\\

def check_line(line, number_of_line):
    try:
        assert len(line) <= 79, 'Stylistic Issue'
    except AssertionError:
        stylistic_issues_printer(number_of_line)


def stylistic_issues_printer(line):
    print(f'Line {line}: S001 Too Long, Baby')


def main():
    with open(input(), 'r') as python_file:
        line_counter = 1
        for python_line in python_file.readlines():
            check_line(python_line, line_counter)
            line_counter += 1


if __name__ == '__main__':
    main()
