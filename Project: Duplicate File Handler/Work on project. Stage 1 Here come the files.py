'''
Theory
Let's get straight to the point. For our task, we need the os.walk method. The Tutorial's Point guide can shed some light on how to use it.

Description
A computer is a great thing. It helps us store and manage tons of information. Every user knows how to work with folders. In this step, we will learn how to get a list of files and folders within a specific directory.

Objectives
In this stage, your program should:

Accept a command-line argument that is a root directory with files and folders. Print Directory is not specified if there is no command-line argument;
Iterate over folders and print file names with their paths. The direction of the slashes in the printed out paths do not matter. Tests are platform independent, so different style of slashes ("/" or "\") are valid.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Suppose, you have the following set of files and folders:

+---[root_folder]
    |
    +---wall.png
    +---pass.txt
    +---[docs]
    |   |
    |   +---project.py
    |   +---calc.xls
    |   +---tutorial.mp4
    |   +---[res]
    |       |
    |       +---data.json
    |   +---[output]
    |       |
    |       +---result.json
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3
Program output:

> python handler.py root_folder

root_folder/wall.png
root_folder/pass.txt
root_folder/docs/project.py
root_folder/docs/calc.xls
root_folder/docs/tutorial.mp4
root_folder/docs/res/data.json
root_folder/docs/output/result.json
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

'''
# write your code here
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("root_dir", nargs='?', default=None, type=str)
    args = parser.parse_args()
    if args.root_dir is None:
        print("Directory is not specified")
    else:
        os.chdir(str(args.root_dir))
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                print(os.path.join(root, file))
                
\\

import sys
import os

# sys.argv = [sys.argv[0], "../../Duplicate File Handler"]
try:
    directory = sys.argv[1]
except IndexError:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))
            
\\

import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Duplicate File Handler")
parser.add_argument("directory", help="Directory is not specified")
if len(sys.argv) < 2:
    print("Directory is not specified")
    SystemExit()
args = parser.parse_args()
for root, dirs, files in os.walk(args.directory, topdown=True):
    for file in files:
        print(os.path.join(root, file))

