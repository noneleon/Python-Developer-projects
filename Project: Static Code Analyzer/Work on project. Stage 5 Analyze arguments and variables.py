'''
Theory
In this stage, it is preferable to make use of the ast module (Abstract Syntactic Tree). If you feel that you need to know more about it, here are two tutorials that can help you work with it:

A short tutorial: How to use AST to understand code
A long tutorial that complements the standard documentation
ast module also contains many classes that represent different elements of Python's syntax. For example, the class FunctionDef is a node of the tree representing a definition of some function in the code, the class arguments represents function's arguments, the class Assign represents an expression where a value gets assigned to some variable. You can use all these (and other) classes to find places of the code (names of the variables and so on) that you want to check for correctness:

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        function_name = node.name
        # check whether the function's name is written in camel_case
        pass
Don't be shy to check some other classes and functions of this module to feel confident while using it.

Description
In this final stage, you need to improve your program to check that all the names of function arguments as well as local variables meet the requirements of PEP8. The program must not force the names of variables outside of functions (for example, in modules or classes). The most convenient way to do this is to use the Abstract Syntactic Tree (AST) from the ast module.

Also, your program must check that the given code does not use mutable values (lists, dictionaries, and sets) as default arguments to avoid errors in the program.

Objectives
You need to add three new checks to your analyzer:

[S010] Argument name arg_name should be written in snake_case;

[S011] Variable var_name should be written in snake_case;

[S012] The default argument value is mutable.

Please note that:

Names of functions, as well as names of variables in the body of a function should be written in snake_case. However, the error message for an invalid function name should be output only when the function is defined. The error message for an invalid variable name should be output only when this variable is assigned a value, not when this variable is used further in the code.

To simplify the task, you only need to check whether the mutable value is directly assigned to an argument:

def fun1(test=[]):  # default argument value is mutable
    pass


def fun2(test=get_value()):  # you can skip this case to simplify the problem
    pass
If a function contains several mutable arguments, the message should be output only once for this function.

Variable and argument names are assumed to be valid if they are written in snake_case. Initial underscores (_) are also acceptable.

As before:

You can use other messages, but the check codes must be exactly as given above.

All the previously implemented checks should continue to work correctly, and the program should be able to read from one or more files.

Examples
Here is an input example:

CONSTANT = 10
names = ['John', 'Lora', 'Paul']


def fun1(S=5, test=[]):  # default argument value is mutable
    VARIABLE = 10
    string = 'string'
    print(VARIABLE)
The expected output for this code is:

/path/to/file/script.py: Line 5: S010 Argument name 'S' should be snake_case
/path/to/file/script.py: Line 5: S012 Default argument value is mutable
/path/to/file/script.py: Line 6: S011 Variable 'VARIABLE' in function should be snake_case
Note that the message for the line print(VARIABLE) is not printed since it was already output for line 5, where the variable VARIABLE is assigned a value.

Extra
You can also use AST to rewrite some of the checks implemented before. It would be especially convenient for checking the names of functions and classes.

If you would like to continue improving this project, you can also:

implement all of the standard PEP8 checks;

display column numbers;

disable some of the checks via command-line arguments.


'''
import re
import sys
import os
import ast


def check_s001(local_path, sample: str, i: int):
    if len(sample) > 79:
        print(f'{local_path}: Line {i}: S001 Too long')


def check_s002(local_path, sample: str, i: int):
    if sample.startswith(' '):
        l = 1
        while sample[l] == ' ':
            l += 1
        if l % 4 != 0:
            print(f'{local_path}: Line {i}: S002 Indentation is not a multiple of four')


def check_s003(local_path, sample: str, i: int):
    semicolon = sample.find(';')
    comment = sample.find('#')
    if semicolon != -1:
        if comment != -1 and semicolon > comment:
            pass
        else:
            if re.search("[\'\"].*;.*[\'\"]", sample):
                pass
            else:
                print(f'{local_path}: Line {i}: S003 Unnecessary semicolon')


def check_s004(local_path, sample: str, i: int):
    comment = sample.find('#')
    if comment and comment >= 2:
        if sample[comment-1] == ' ' and sample[comment-2] == ' ':
            pass
        else:
            print(f'{local_path}: Line {i}: S004 At least two spaces required before inline comments')


def check_s005(local_path, sample: str, i: int):
    comment = sample.find('#')
    todo = sample.lower().find('todo')
    if comment != -1 and comment < todo:
        print(f'{local_path}: Line {i}: S005 TODO found')


def check_s006(local_path, i: int):
    if content[i] != '\n':
        if content[i - 1].strip() == '' and content[i - 2].strip() == '' and content[i - 3].strip() == '':
            print(f'{local_path}: Line {i + 1}: S006 More than two blank lines used before this line')


def check_s007(local_path, sample: str, i: int):
    words = ['def', 'class']
    for word in words:
        if word in sample:
            if re.search(f'{word} [^\s]', sample):
                pass
            else:
                print(f'{local_path}: Line {i}: S007 Too many spaces after {word}')


def check_s008(local_path, sample: str, i: int):
    if 'class' in sample:
        temp = re.findall(r'class \w+:', sample)
        for equal in temp:
            class_name = equal[6:-1]
            if '(' in class_name:
                index = class_name.index('(')
                class_name = class_name[:index]
            if re.fullmatch(r'([A-Z][a-z0-9]*)*', class_name):
                pass
            else:
                print(f'{local_path}: Line {i}: S008 Class name {class_name} should be written in CamelCase')


def check_s009(local_path, sample: str, i: int):
    if 'def' in sample:
        temp = re.findall(r'def \w+\(', sample)
        def_name = temp[0][4:-1]
        if re.fullmatch(r'[a-z0-9_]*', def_name):
            pass
        else:
            print(f'{local_path}: Line {i}: S009 Function name {def_name} should be written in snake_case')


def check_s010(local_path, sample: str, i: int):
    if 'def' in sample:
        temp = re.findall(r'def \w+\(', sample)
        def_name = temp[0][4:-1]
        script = open(local_path).read()
        func_parse = ast.walk(ast.parse(script))
        for node in func_parse:
            if isinstance(node, ast.FunctionDef) and node.name == def_name:
                args = [a.arg for a in node.args.args]
                for arg in args:
                    if re.fullmatch(r'[a-z0-9_]+', arg):
                        pass
                    else:
                        print(f'{local_path}: Line {i}: S010 Argument name \'{arg}\' should be written in snake_case')


def check_s011(local_path, sample: str, i: int):
    if re.match(r'\w+.=', sample.strip()):
        variable = re.search(r'\w+ =', sample.strip()).group()[:-2]
        if re.fullmatch('[a-z0-9_]+', variable):
            pass
        else:
            print(f'{local_path}: Line {i}: S011 Variable \'\' in function should be snake_case')


def check_s012(local_path, sample: str, i: int):
    if 'def' in sample:
        temp = re.findall(r'def \w+\(', sample)
        def_name = temp[0][4:-1]
        script = open(local_path).read()
        func_parse = ast.walk(ast.parse(script))
        for node in func_parse:
            if isinstance(node, ast.FunctionDef) and node.name == def_name:
                d_args = [d for d in node.args.defaults]
        for a in d_args:
            if isinstance(a, ast.List):
                print(f'{local_path}: Line {i}: S012 Default argument value {a} is mutable')


path_name = sys.argv[1]

total_list = []

if os.path.isdir(path_name):
    for path, dirs, files in os.walk(path_name):
        for name in files:
            element = os.path.join(path, name)
            total_list.append(element)
else:
    total_list.append(path_name)

for element in total_list:
    if element.endswith('.py'):
        f = open(element, 'r', encoding='utf-8')
        content = f.readlines()
        i = 0
        for line in content:
            check_s001(element, line, i + 1)
            check_s002(element, line, i + 1)
            check_s003(element, line, i + 1)
            check_s004(element, line, i + 1)
            check_s005(element, line, i + 1)
            if i >= 2:
                check_s006(element, i)
            check_s007(element, line, i + 1)
            check_s008(element, line, i + 1)
            check_s009(element, line, i + 1)
            check_s010(element, line, i + 1)
            check_s011(element, line, i + 1)
            check_s012(element, line, i + 1)
            i += 1
        f.close()
        
\\

# write your code here
import sys
import os
import re
import ast


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


def s010(_res, file_text, _fpath):
    tree = ast.parse("".join(file_text))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if any([not bool(re.match(r"(_{,2}[a-z]+_{,2})+", a.arg)) for a in node.args.args]):
                ind = 0
                for i in range(len(file_text)):
                    if re.search(node.name, file_text[i]):
                        ind = i + 1
                        break
                _res += f"{_fpath}: Line {ind}: S010 Argument name arg_name should be written in snake_case.",


def s011(_res, file_text, _fpath):
    tree = ast.parse("".join(file_text))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.targets[0], ast.Name):
                names = [node.targets[0].id]
            elif isinstance(node.targets[0], ast.Attribute):
                names = [node.targets[0].value.id, node.targets[0].attr]
            if any(not is_snake(x) for x in names):
                ind = 0
                for i in range(len(file_text)):
                    if re.search(f"{names[-1]} *=", file_text[i]):
                        ind = i + 1
                        break
                _res += f"{_fpath}: Line {ind}: S011 Variable var_name should be written in snake_case",


def s012(_res, file_text, _fpath):
    tree = ast.parse("".join(file_text))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if any(isinstance(x, (ast.Dict, ast.Set, ast.List)) for x in node.args.defaults):
                ind = 0
                for i in range(len(file_text)):
                    if re.search(node.name, file_text[i]):
                        ind = i + 1
                        break
                _res += f"{_fpath}: Line {ind}: S012 The default argument value is mutable",


def is_snake(text):
    return bool(re.match(r"(_{,2}[a-z]+_{,2}[a-z]*)+\b", text))


def analyzer(_res, _file):
    count = 0

    with open(_file, 'r') as f:
        text = f.readlines()
        empty = 0
        for line in text:
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

        s010(_res, text, _file)
        s011(_res, text, _file)
        s012(_res, text, _file)


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
    
\\

from file_handler import FileHandler
import sys
import re
import ast
from ast_parsing import AstParser
from messages import STYLE_MESSAGES, NAMED_MESSAGES


def get_name(line):
    """
    Return class or function name from given string
    :param line: string, one line of code
    :return: Class or function name
    """
    return re.search(r"(def|class) +(\w+).*$", line).group(2)


def get_construction_name(line):
    """
    Get construction name (def or class)
    :param line: string, one line of code
    :return: construction name
    """
    return re.search(r"(def|class)", line).group(1)


class Analyzer():
    def __init__(self, file_handler):
        """
        Parsers directory for py files if given
        :param file_handler: Object of FileHandler class
        """
        self.files = file_handler.get_filter_files('py')
        self.errors = []
        self.name_issues = {}

    def analyze_all(self):
        """
        Analyzes single file or all files in directory
        :return: formatted dic {Path: {Line: Code}}
        """
        issues = {}
        for file in self.files:  # py file
            self.name_issues = {}
            issues[file] = self.perform_checks(file)
            for pos, value in issues[file].items():  # {pos = line_number: value = [issues_list]}
                for error in value:  # issues in line №(pos)
                    if error in NAMED_MESSAGES:
                        message = STYLE_MESSAGES[error].replace("-", self.name_issues[pos][error])
                    else:
                        message = STYLE_MESSAGES[error]
                    print(f"{file}: Line {pos}: {error} {message}")

    def perform_checks(self, path):
        """
        checks specified file
        :param path: path to py file to check
        :return: dic {Line: [Codes]}
        """
        pyfile = open(path)
        file_errors = {}
        blank_counter = 0
        blank_issue = False
        for num, line in enumerate(pyfile):
            line = line.strip('\n')
            if not line or line.isspace():
                blank_counter += 1
                blank_issue = True if blank_counter > 2 else False
                continue
            file_errors.update(self.get_line_issues(num+1, line, blanks=blank_issue))

            blank_counter = 0
            blank_issue = False
        pyfile.close()
        ast_errors = self.perform_ast_checks(path)
        for line_error in ast_errors:
            if line_error in file_errors:
                file_errors[line_error].extend(ast_errors[line_error])
            else:
                file_errors[line_error] = ast_errors[line_error]
        return file_errors

    def perform_ast_checks(self, path):
        with open(path) as file:
            tree = ast.parse(file.read())
            ast_parser = AstParser()
            ast_parser.visit(tree)
            for line_name in ast_parser.name_errors:
                if line_name in self.name_issues:
                    self.name_issues[line_name].update(ast_parser.name_errors[line_name])
                else:
                    self.name_issues[line_name] = ast_parser.name_errors[line_name]
        return ast_parser.errors


    def get_line_issues(self, num, line, blanks=False):
        """
        Get all issues in line
        :param num: line number
        :param line: line text
        :param blanks: true if more than two preceding blank lines
        :return: {num: [list of errors in line]}
        """
        self.errors = []
        if "class" in line or "def" in line:
            self.get_naming_issues(num, line)
        self.check_len(line)
        self.check_comments(line)
        self.check_indentation(line)
        self.check_unnec_symbs(line)
        if blanks:
            self.errors.append("S006")
        return {num: sorted(self.errors)}

    def get_naming_issues(self, num, line):
        """
        Issues related with function or class name
        :param num: line number
        :param line: line text
        :return: True if found at least one issue
        """
        self.name_issues[num] = {}
        s007 = self.check_spaces(line)
        if s007 is not None:
            self.name_issues[num]["S007"] = s007

        s008 = self.check_class_name(line)
        if s008 is not None:
            self.name_issues[num]["S008"] = s008

        s009 = self.check_def_name(line)
        if s009 is not None:
            self.name_issues[num]["S009"] = s009
        return self.name_issues is not None


    def check_len(self, line):  # S001
        if len(line) > 79:
            self.errors.append("S001")

    def check_comments(self, line):  # S004 S005
        if '#' in line:
            index = line.index('#')
            if (line[index - 1] != ' ' or line[index - 2] != ' ') and index > 1:
                self.errors.append("S004")
            if line.upper().find("TODO") != -1:
                self.errors.append("S005")

    def check_indentation(self, line):  # S002
        for index, char in enumerate(line):
            if char != ' ':
                if index % 4 != 0:
                    self.errors.append("S002")
                break

    def check_unnec_symbs(self, line):  # S003
        if '#' in line:
            line = line[:line.index('#')]
        for char in reversed(line):
            if char != ' ':
                if char == ';':
                    self.errors.append("S003")
                break

    def check_spaces(self, line):  # S007
        match = re.search(r"(class|def)  +.*$", line)
        if match:
            self.errors.append("S007")
            return match.group(1)
        return None

    def check_class_name(self, line):  # S008
        if get_construction_name(line) == "class":
            match = re.search(r"class +([A-Z][a-z0-9]*)+[(:]", line)
            if match is None:
                self.errors.append("S008")
                return get_name(line)
        return None

    def check_def_name(self, line):  # S009
        if get_construction_name(line) == "def":
            match = re.search(r"def +[a-z0-9_]+\(.*$", line)
            if match is None:
                self.errors.append("S009")
                return get_name(line)
        return None


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        analyzer = Analyzer(FileHandler(args[1]))
        analyzer.analyze_all()
    else:
        print("USAGE: python code_analyzer.py directory-or-file")
//

import os
import glob


class FileHandler:
    def __init__(self, path):
        self.path = path

    def get_filter_files(self, extension=None):
        """
        Get all files in given path if path - directory, otherwise path will be returned
        :param extension: files with specified extension will be returned
        :return: all files within directory
        """
        if os.path.isfile(self.path):
            return [self.path]
        os.chdir(self.path)
        return [self.path + '\\' + file for file in glob.glob("**/*." + extension, recursive=True)]
analyzer/messages.py
STYLE_MESSAGES = {"S001": "More than 79 symbols",
                  "S002": "Indentation is not a multiple of four",
                  "S003": "Unnecessary semicolon after a statement",
                  "S004": "Less than two spaces before inline comments",
                  "S005": "TODO found",
                  "S006": "More than two blank lines preceding a code line",
                  "S007": "Too mane spaces after '-'",
                  "S008": "Class name '-' should be written in CamelCase",
                  "S009": "Function name '-' should be written in snake_case",
                  "S010": "Argument name '-' should be written in snake_case",
                  "S011": "Variable '-' should be written in snake_case",
                  "S012": "The default argument value is mutable"}

NAMED_MESSAGES = ["S007", "S008", "S009", "S010", "S011"]


