'''
Description
Let's add a few more checks to the program. All of them are consistent with the PEP8 style guide.

Objectives
In this stage, you need to add checks for the following five errors to your program:

[S002] Indentation is not a multiple of four;

[S003] Unnecessary semicolon after a statement (note that semicolons are acceptable in comments);

[S004] Less than two spaces before inline comments;

[S005] TODO found (in comments only and case-insensitive);

[S006] More than two blank lines preceding a code line (applies to the first non-empty line).

Please note that:

If a line contains the same stylistic issue several times, your program should print the information only once. However, if a single line has several issues with different types of error codes, they should be printed as a sorted list.

To simplify the task, we consider it acceptable if your program finds some false-positive stylistic issues in strings, especially in multi-lines ('''...''' and """...""").

We recommend that you break your code into a set of functions to avoid confusion.

Once again:

The path to the file with Python code is obtained from standard input.

The general output format is:

Line X: Code Message
The lines with found issues must be output in ascending order.
Examples
Here is an example of badly styled Python code (please never write code like this!):

print('What\'s your name?') # reading an input
name = input();
print(f'Hello, {name}');  # here is an obvious comment: this prints a greeting with a name


very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)



def some_fun():
    print('NO TODO HERE;;')
    pass; # Todo something
It contains nine code style issues:

Line 1: S004 At least two spaces required before inline comments
Line 2: S003 Unnecessary semicolon
Line 3: S001 Too long
Line 3: S003 Unnecessary semicolon
Line 6: S001 Too long
Line 11: S006 More than two blank lines used before this line
Line 13: S003 Unnecessary semicolon
Line 13: S004 At least two spaces required before inline comments
Line 13: S005 TODO found
'''

# write your code here
import re
count = 0


def s001(_res, _count, _line):
    if len(_line) > 79:
        _res += f"Line {_count}: S001 Too long",


def s002(_res, _count, _line):
    ind = next(i for i, x in enumerate(_line) if x != " ")
    if ind % 4 != 0:
        _res += f"Line {_count}: S002 Indentation is not a multiple of four",


def s003(_res, _count, _line):
    semicolon = False
    last = True
    found_last = False
    for i in reversed(_line):
        if not found_last and i not in [";", " ", "\n"]:
            last = False
            found_last = True
        if i == ";":
            semicolon = True
            if not found_last:
                found_last = True
                last = True
        if i == "#":
            semicolon = False
            found_last = False
            last = True

    if semicolon and last:
        _res += f"Line {_count}: S003 Unnecessary semicolon after a statement",


def s004(_res, _count, _line):
    try:
        ind = _line.index("#")
    except ValueError:
        ind = None

    if ind:
        if _line[ind-2:ind] != '  ':
            _res += f"Line {_count}: S004 Less than two spaces before inline comments",


def s005(_res, _count, _line):
    try:
        ind = _line.index("#")
    except ValueError:
        ind = -1

    if ind >= 0:
        if "todo" in line[ind:].lower():
            _res += f"Line {_count}: S005 TODO found",


def s006(_res, _count):
    _res += f"Line {_count}: S006 More than two blank lines preceding a code line",


with open(input(), 'r') as f:
    res = []
    empty = 0
    for line in f:
        count += 1
        if line == "\n":
            empty += 1
        else:
            s001(res, count, line)
            s002(res, count, line)
            s003(res, count, line)
            s004(res, count, line)
            s005(res, count, line)

            if empty > 2:
                s006(res, count)
                first = False
                empty = 0


for x in res:
    print(x)
    
\\

import re

file = input()
blank_lines_counter = 0


def check_line(line, number_of_line):
    long_line(line, number_of_line)
    indentation(line, number_of_line)
    semicolon(line, number_of_line)
    comments(line, number_of_line)
    todo_comment(line, number_of_line)
    blank_lines(line, number_of_line)


def long_line(line, number_of_line):  # S001
    if len(line) > 79:
        issue_printer(number_of_line, 'S001 Too Long, baby')


def indentation(line, number_of_line):  # S002
    if not bool(re.match(r'(\w|#|\n)|( {4}\w)|( {8})', line)):
        issue_printer(number_of_line, 'S002 Learn how to indent')


def semicolon(line, number_of_line):  # S003
    if re.search(r'([^#][^\t\n\r\f\v]+;)($|[ ]*#)', line) and not re.search(r'#.*;', line):
        issue_printer(number_of_line, 'S003 WTH with the semicolon')


def comments(line, number_of_line):  # S004
    if bool(re.match(r'#', line)) == False and re.search(r'#', line):
        if not bool(re.search(r'([^\#][^\t\n\r\f\v]+)(  \#)', line)):
            issue_printer(number_of_line, 'S004 put two spaces before the comment!')


def todo_comment(line, number_of_line):  # S005
    if re.search(r'\# [^\t\n\r\f\v]*TODO', line, re.I):
        issue_printer(number_of_line, 'S005 come on!')


def blank_lines(line, number_of_line):  # S006
    global blank_lines_counter
    if line == '\n':
        blank_lines_counter += 1
    elif line != '' and blank_lines_counter > 2:
        blank_lines_counter = 0
        issue_printer(number_of_line, 'S006 More than two blank lines, man!')


def issue_printer(number_of_line, error_message):
    print(f'Line {number_of_line}: {error_message}')


def main():
    with open(file, 'r') as python_file:
        line_counter = 1
        for python_line in python_file.readlines():
            check_line(python_line, line_counter)
            line_counter += 1


if __name__ == '__main__':
    main()
    
\\
import re


class CodeAnalyzer:

    errors_codes = {'S001': lambda i: f'Line {i}: S001 Too long',
                    'S002': lambda i: f'Line {i}: S002 Indentation is not a multiple of four',
                    'S003': lambda i: f'Line {i}: S003 Unnecessary semicolon after a statement',
                    'S004': lambda i: f'Line {i}: S004 At least two spaces required before inline comments',
                    'S005': lambda i: f'Line {i}: S005 TODO found',
                    'S006': lambda i: f'Line {i}: S006 More than two blank lines used before this line'}

    def __init__(self):
        self.lines = None
        self.issues = {}

    def read_file(self, path):
        with open(path, 'r') as file:
            self.lines = file.readlines()
    
    def check_s001(self):
        for i, line in enumerate(self.lines):
            if len(line) > 79:
                self.issues.setdefault(i + 1, []).append('S001')

    def check_s002(self):
        for i, line in enumerate(self.lines):
            if not re.search(r'^( {4})+\b|^[^ ]', line):
                self.issues.setdefault(i + 1, []).append('S002')

    def check_s003(self):
        for i, line in enumerate(self.lines):
            if ';' in line and not re.search(r'''#.*;|['"].*;.*['"]''', line):
                self.issues.setdefault(i + 1, []).append('S003')

    def check_s004(self):
        for i, line in enumerate(self.lines):
            if '#' in line and not re.search(r'^#| {2}#', line):  # (?=((?<!^)#))(?=((?<! {2})#))
                self.issues.setdefault(i + 1, []).append('S004')

    def check_s005(self):
        for i, line in enumerate(self.lines):
            if re.search(r'#.*todo', line, re.IGNORECASE):
                self.issues.setdefault(i + 1, []).append('S005')

    def check_s006(self):
        counter = 0
        for i, line in enumerate(self.lines):
            if line == '\n':
                counter += 1
            else:
                if counter > 2:
                    self.issues.setdefault(i + 1, []).append('S006')
                counter = 0

    def print_issues(self):
        for i in sorted(self.issues):
            for code in self.issues[i]:
                print(self.errors_codes[code](i))


if __name__ == '__main__':
    analyzer = CodeAnalyzer()
    analyzer.read_file(input())
    analyzer.check_s001()
    analyzer.check_s002()
    analyzer.check_s003()
    analyzer.check_s004()
    analyzer.check_s005()
    analyzer.check_s006()
    analyzer.print_issues()
