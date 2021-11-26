'''
Description
As many coders say, naming is one of the hardest things in programming. Good naming makes your code more readable and uniform. Names should also follow style guides. In Python, the basic requirement is using snake_case for function names and CamelCase for class names. Also, there should be only one space between the construction name and the object name. Checking these rules is the next feature that we need to implement.

Check out the Python tutorial about regular expressions: they will help you implement the checks.

Objectives
In this stage, we need to add three new checks to the program:

[S007] Too many spaces after construction_name (def or class);

[S008] Class name class_name should be written in CamelCase;

[S009] Function name function_name should be written in snake_case.

Note that:

Functions names may start and end with underscores (__fun, __init__).

To simplify the task, we will assume that classes are always written as in the following examples:

# a simple class
class MyClass:
    pass

# a class based on inheritance
class MyClass(AnotherClass):
    pass
In reality, it's possible to declare a class this way:

class \
        S:
    pass
However, since it is not a common way to declare classes, you can ignore it.

Another assumption is that functions are always declared like this:

def do_magic():
    pass
As before:

The program obtains the path to the file or directory via command-line arguments:

> python code_analyzer.py directory-or-file
All the previously implemented checks should continue to work properly.

Examples
Here is an input example:

class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')
The expected output for this code is:

/path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
/path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
'''
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
    if re.match(r'^(\s{4})*?([\S].*?)?$', file_line):
        return True
    else:
        return False

def get_multispaces_word(file_line):
    r = re.search(r'(def|class)\s{2,}', file_line)
    if r:
        return r.group()
    else:
        return None

def get_bad_classname(file_line):
    r = re.search(r'class\s+.*?_.*?(\(|:)', file_line)
    if r:
        w = r.group().split(' ',2)[1].strip().rstrip('(:')
        return(w)
    r = re.search(r'class\s+[a-z].*?(\(|:)', file_line)
    if r:
        w = r.group().split(' ',2)[1].strip().rstrip('(:')
        return(w)
    else:
        return None


def get_bad_function(file_line):
    r = re.search(r'def\s+.*?[A-Z].*?(\(|:)', file_line)
    if r:
        w = r.group().split(' ', 2)[1].strip().rstrip('(:')
        return (w)
    else:
        return None

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
            multi_space_word = get_multispaces_word(line)
            if multi_space_word:
                print(f"{file_name}: Line {line_num}: S007 Too many spaces after construction_name '{multi_space_word.strip()}'")
            class_name = get_bad_classname(line)
            if class_name:
                print(f"{file_name}: Line {line_num}: S008 Class name '{class_name}' should be written in CamelCase")
            function_name = get_bad_function(line)
            if function_name:
                print(f"{file_name}: Line {line_num}: S009 Function name '{function_name}' should use snake_case")

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

# write your code here
import sys
import os
import re


def s001(_res, _count, _line, _fpath):
    if len(_line) > 79:
        _res += f"{_fpath}: Line {_count}: S001 Too long",


def s002(_res, _count, _line, _fpath):
    ind = next(i for i, c in enumerate(_line) if c != " ")
    if ind % 4 != 0:
        _res += f"{_fpath}: Line {_count}: S002 Indentation is not a multiple of four",


def s003(_res, _count, _line, _fpath):
    _line = re.sub('#.*', "", _line).strip()
    if _line and _line[-1] == ";":
        _res += f"{_fpath}: Line {_count}: S003 Unnecessary semicolon after a statement",


def s004(_res, _count, _line, _fpath):
    match = re.search("#", _line.strip())
    if match:
        ind = match.span()[0]
        if ind and _line[ind-2:ind] != '  ':
            _res += f"{_fpath}: Line {_count}: S004 Less than two spaces before inline comments",


def s005(_res, _count, _line, _fpath):
    if re.search("#", _line):
        _line = re.sub('.*#', "", _line).strip().lower()
        if re.search("todo", _line):
            _res += f"{_fpath}: Line {_count}: S005 TODO found",


def s006(_res, _count, _fpath):
    _res += f"{_fpath}: Line {_count}: S006 More than two blank lines preceding a code line",


def strip_function_or_class(construction, _line):
    match = re.search(construction, _line)
    if match:
        _line = _line[match.span()[1]:]
    return match, _line


def s007(_res, _count, _line, _fpath):
    match, _line = strip_function_or_class("(class|def)", _line)
    if match:
        if re.match(r"  +", _line):
            _res += f"{_fpath}: Line {_count}: S007 Too many spaces after construction_name",


def s008(_res, _count, _line, _fpath):
    match, _line = strip_function_or_class("class", _line)
    _line = _line.strip()
    if match:
        if not re.match(r"[A-Z][a-z]+[A-z0-9]*", _line):
            _res += f"{_fpath}: Line {_count}: S008 Class name class_name should be written in CamelCase",


def s009(_res, _count, _line, _fpath):
    match, _line = strip_function_or_class("def", _line)
    _line = _line.strip()
    if match:
        if not re.match(r"(_{,2}[a-z]+_{,2})+", _line):
            _res += f"{_fpath}: Line {_count}: S009 Function name function_name should be written in snake_case.",


def analyzer(_res, _file):
    count = 0
    with open(_file, 'r') as f:
        empty = 0
        for line in f:
            count += 1
            if line == "\n":
                empty += 1
            else:
                s001(_res, count, line, _file)
                s002(_res, count, line, _file)
                s003(_res, count, line, _file)
                s004(_res, count, line, _file)
                s005(_res, count, line, _file)
                if empty > 2:
                    s006(_res, count, _file)
                s007(_res, count, line, _file)
                s008(_res, count, line, _file)
                s009(_res, count, line, _file)

                empty = 0


arg = sys.argv[1]

res = []
if os.path.isdir(arg):
    for file in sorted(os.listdir(arg)):
        if re.match(r".+\.py", file):
            analyzer(res, arg + "/" + file)
elif os.path.isfile(arg):
    analyzer(res, arg)

for x in res:
    print(x)
