'''
Description
As a rule, real projects contain more than a single file. Also, project directories often contain not only Python files, and we don't need to check if an HTML file follows PEP8.

We recommend that you check out a tutorial on realpython.com that can help you to work with files and directories.

Objectives
In this stage, you need to improve your program so that it can analyze all Python files inside a specified directory.

Please note that:

You also need to change the input format. Instead of reading the path from the standard input, the program must obtain it as a command-line argument:

> python code_analyzer.py directory-or-file
The output format also needs to be changed slightly. It should include the path to the analyzed file:

Path: Line X: Code Message 
All output lines must be sorted in ascending order according to the file name, line number, and issue code.

Non-Python files must be skipped.

Once again:

It is important that all the checks implemented in the previous stages continue to work properly.

If a line contains the same stylistic issue several times, your program must print the information only once. If a line has several issues with different types of error codes, they should be printed in ascending order.

To simplify the solution, we consider it acceptable if your program finds some false-positive stylistic issues in strings, especially in multi-lines ('''...''' and """...""").

We recommend that you break your program code into a set of functions and classes to avoid confusion.

Examples
Only a single file is specified as the input:

> python code_analyzer.py /path/to/file/script.py
/path/to/file/script.py: Line 1: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 2: S003 Unnecessary semicolon
/path/to/file/script.py: Line 3: S001 Too long line
/path/to/file/script.py: Line 3: S003 Unnecessary semicolon
/path/to/file/script.py: Line 6: S001 Too long line
/path/to/file/script.py: Line 11: S006 More than two blank lines used before this line
/path/to/file/script.py: Line 13: S003 Unnecessary semicolon
/path/to/file/script.py: Line 13: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 13: S005 TODO found
The input path is a directory; the output should contain all Python files from it:

> python code_analyzer.py /path/to/project
/path/to/project/__init__.py: Line 1: S001 Too long line
/path/to/project/script1.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script1.py: Line 2: S003 Unnecessary semicolon
/path/to/project/script2.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script2.py: Line 3: S001 Too long line
/path/to/project/somedir/script.py: Line 3: S001 Too long line
/path/to/project/test.py: Line 3: Line 13: S003 Unnecessary semicolon
'''

import re
import os
import sys


class CodeAnalyzer:
    errors_codes = {'S001': lambda f, i: f'{f}: Line {i}: S001 Too long',
                    'S002': lambda f, i: f'{f}: Line {i}: S002 Indentation is not a multiple of four',
                    'S003': lambda f, i: f'{f}: Line {i}: S003 Unnecessary semicolon after a statement',
                    'S004': lambda f, i: f'{f}: Line {i}: S004 At least two spaces required before inline comments',
                    'S005': lambda f, i: f'{f}: Line {i}: S005 TODO found',
                    'S006': lambda f, i: f'{f}: Line {i}: S006 More than two blank lines used before this line'}

    def __init__(self):
        self.file = None
        self.lines = None
        self.issues = {}

    def read_file(self, path):
        self.file = path
        with open(self.file, 'r') as file:
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

    def check_all(self):
        self.check_s001()
        self.check_s002()
        self.check_s003()
        self.check_s004()
        self.check_s005()
        self.check_s006()

    def print_issues(self):
        for i in sorted(self.issues):
            for code in self.issues[i]:
                print(self.errors_codes[code](self.file, i))


class FilesAnalyzer(CodeAnalyzer):

    def __init__(self, path):
        super().__init__()
        path = path.lstrip('/')
        if path[-3:] == '.py':
            self.files = [path]
        else:
            self.files = sorted(
                [f'{path}{os.sep}{file}' for file in os.listdir(f'{path}{os.sep}') if file[-3:] == '.py'])

    def analyze_all_files(self):
        for file in self.files:
            self.issues = {}
            self.read_file(file)
            self.check_all()
            self.print_issues()


if __name__ == '__main__':
    analyzer = FilesAnalyzer(sys.argv[-1])
    analyzer.analyze_all_files()
    
    
\\

# write your code here
import re
import sys
import os

args = sys.argv
file_or_dir = args[1]

# g_file_name = input()
# g_prev_multiline_sep = ''
# g_line_tokens = []

''' line_parse will become a list of dictionaries of the following format
[{type: 'mlcomment' or 'comment' or 'string' or 'normal'
  text: some text without separator}
]
This will allow us to ignore text lines or comments in most of our checks 
    and use normal "contains" function for all validations

Parsing logics:
process every line to get tokens of text in a dictionary
({'type': normal or comment or mlcomment or strings
   'text': token text})
after that it's handy to process only 'normal' text not to mix it with comments or strings

1) look for multiline separators, if any - add to the list with the remaining part
2) look for strings, if any - add to list (process correctly '' or "" casaes) with 
the remaining part
3)  add "normal" part to the list
4) apply all normal part validations
5) update prev_multiline_comment and prev_multiline_sep for multiline 
separator cases for future lines and go to nextline processing

'''
ESCAPES = ((r'\\', '%%BWSLASH%%'), (r"\'", '%%QUOTE1%%'), (r'\"', '%%QUOTE2%%'))


# let's escape sequences of \\ or \' or \" not to get them processed by normal strings split operation
def encode_escapes(str_1):
    str_2 = str_1
    for i in ESCAPES:
        str_2 = str_2.replace(i[0], i[1])
    return str_2


# decode original sequences
def decode_escapes(str_1):
    str_2 = str_1
    for i in ESCAPES:
        str_2 = str_2.replace(i[1], i[0])
    return str_2


def check_indentation(file_line):
    if re.match(r'^(\s{4})*([\S].*)?$', file_line):
        return True
    else:
        return False


# Get separator with minimum position (to find 1st occurence of (''' or """), (' or ") - etc)
def get_min_sep(file_line, *args):
    sep_positions = {s: file_line.find(s) for s in args if file_line.find(s) >= 0}
    if sep_positions:
        # print(sep_positions)
        return min(sep_positions, key=sep_positions.get)
    else:
        return None


# take string from unprocessed part till separator (or till end of line)
# and put it to previous part of certain type
def add_token(list, type, sep):
    if sep:
        split_tokens = list[-1]['text'].split(sep, maxsplit=1)
    else:
        split_tokens = [list[-1]['text']]

    list.insert(-1, {"type": type, "text": split_tokens[0]})

    if len(split_tokens) < 2:
        list[-1]['text'] = ""
    else:
        list[-1]['text'] = split_tokens[1]
    return split_tokens


def parse_new_line(file_line, line_tokens=[], prev_multiline_sep=""):
    # print('file line: ', file_line)
    # nonlocal prev_multiline_sep
    # start parsing, create 1st record in tokens list
    if not line_tokens:  # empty tokens list - 1st run
        line_tokens.append({"type": 'unprocessed', "text": file_line})

    # print('line_tokens', line_tokens)
    # print(line_tokens[-1])
    # if this is a multiline comment - find next separator of previous multiline

    # while there is something to parse
    next_sep = ""
    while line_tokens[-1]['text']:

        # handle ending of previous multiline comments first
        if prev_multiline_sep:
            split_tokens = add_token(line_tokens, 'mlcomment', prev_multiline_sep)
            # print('test', line_tokens)
            # split_tokens = line_tokens[-1]['text'].split(prev_multiline_sep, maxsplit=1)
            # line_tokens.insert(-1, {"type": 'mlcomment', "text": splitted_tokens[0]})

            if len(split_tokens) == 1:
                # no separator till the end of line - whole line reminder should become a comment
                # line_tokens[-1]['text'] = ""
                return True
            else:
                # line_tokens[-1]['text'] = split_tokens[1]
                prev_multiline_sep = ''
                continue

        # continue with other separators
        if not next_sep:
            # try to find next separator
            next_sep = get_min_sep(line_tokens[-1]['text'], '"""', "'''", '"', "'", '#')
            if not next_sep:
                # convert last piece to "normal" text and return
                add_token(line_tokens, 'normal', '')
                return True
            else:
                # add new "normal" token - text before specific separators
                split_tokens = add_token(line_tokens, 'normal', next_sep)
        elif next_sep in ("'''", '"""'):
            prev_multiline_sep = next_sep
            next_sep = ""
            continue
        elif next_sep in ("'", '"'):
            split_tokens = add_token(line_tokens, 'string', next_sep)
            next_sep = ""
            continue
        elif next_sep == '#':
            # convert last piece to "comment" text and return - whole line reminder should become a comment
            add_token(line_tokens, 'comment', '')
            return True


def check_one_file(file_name):
    empty_counter = 0
    with open(file_name, 'r') as file_:
        for line_num, line in enumerate(file_, start=1):
            # print(line_num, line)
            line_tokens = []
            prev_multiline_sep = ''
            line_encoded = encode_escapes(line)
            parse_new_line(line_encoded, line_tokens, prev_multiline_sep)

            for i in line_tokens:
                i['text'] = decode_escapes(i['text'])

            if len(line) > 79:
                print(f"{file_name}: Line {line_num}: S001 The line is too long")
            if not check_indentation(line):
                print(f"{file_name}: Line {line_num}: S002 Indentation is not a multiple of four")
            # check for semicolon in "normal" text
            if ';' in (''.join([i['text'] for i in line_tokens if i['type'] == 'normal'])):
                print(
                    f"{file_name}: Line {line_num}: S003 Unnecessary semicolon after a statement (note that semicolons are acceptable in comments")
            if line[0] != '#' \
                    and len(line_tokens) > 2 and line_tokens[-2]['type'] == 'comment' \
                    and (line_tokens[-3]['type'] != 'normal' \
                         or line_tokens[-3]['type'] == 'normal' \
                         and line_tokens[-3]['text'][-2:] != '  '):
                print(f"{file_name}: Line {line_num}: S004 Less than two spaces before inline comments")

            if 'TODO' in ''.join([i['text'].upper() for i in line_tokens if i['type'] == 'comment']):
                print(f"{file_name}: Line {line_num}: S005 TODO found (in comments only and case-insensitive)")
            if line == '\n':
                empty_counter += 1
            else:
                if empty_counter > 2:
                    print(
                        f"{file_name}: Line {line_num}: S006 More than two blank lines preceding a code line (applies to the first non-empty line")
                empty_counter = 0

# main part starts here
#print(os.path.isfile(file_or_dir))
#print(os.path.isdir('test'))
#print(file_or_dir)
if os.path.isfile(file_or_dir):
    check_one_file(file_or_dir)
elif os.path.isdir(file_or_dir):
    files = [os.path.join(file_or_dir, f) for f in os.listdir(path=file_or_dir) if f.endswith('.py')]
    for file_name in files:
        check_one_file(file_name)
        
\\