'''
Description
In this stage, we start by identifying files of the same size in bytes. The os.path module allows you to get access to file extension and size. The Official Documentation can help you with that.

Of course, we cannot be absolutely sure that files of the same size and format are duplicates. This will help us, however, narrow down the search. It is also important to keep track of the scanned files. Add an ability to search for files of a specific file format and then sort the found files by size.

Hint

Objectives
Keep the functionality from the previous stage. To complete this stage, your program should:

Accept a command-line argument that is a root directory with files and folders. Print Directory is not specified if there is no command-line argument;
Read user input that specifies the file format (see examples). Empty input should match any file format;
Print a menu with two sorting options: Descending and Ascending. They both represent the respective order by size of groups of files. Read the input. Print Wrong option if any other input is entered. Repeat until a correct input is provided;
Iterate over folders and print the information about files of the same size: their size, path, and names.
Please note: you should use full path to file from root directory when printing or reading.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Suppose, you have the following set of files and folders:

+---[root_folder]
    +---gordon_ramsay_chicken_breast.avi /4590560 bytes
    +---[audio]
    |   |
    |   +---voice.mp3 /2319746 bytes
    |   +---sia_snowman.mp3 /4590560 bytes
    |   +---nea_some_say.mp3 /3232056 bytes
    |   +---[classic]
    |   |   |
    |   |   +---unknown.mp3 /3422208 bytes
    |   |   +---vivaldi_four_seasons_winter.mp3 /9158144 bytes
    |   |   +---chopin_waltz7_op64_no2.mp3 /9765504 bytes
    |   +---[rock]
    |       |
    |       +---smells_like_teen_spirit.mp3 /4590560 bytes
    |       +---numb.mp3 /5786312 bytes
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3 /3422208 bytes
Program output:

> python handler.py root_folder

Enter file format:
>mp3

Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
> 3

Wrong option

Enter a sorting option:
> 2

3422208 bytes
root_folder/audio/classic/unknown.mp3
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

4590560 bytes
root_folder/audio/rock/smells_like_teen_spirit.mp3
root_folder/audio/sia_snowman.mp3
'''

import os
import sys


def check_args():
    args = sys.argv
    if len(args) == 1:
        print("Directory is not specified")
        sys.exit(0)
    return args[1]


def get_fileformat():
    print("Enter file format:")
    ff = input()
    print()
    return ff


def issortingorder_asc():
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    print()
    while True:
        print("Enter a sorting option:")
        sort_no = int(input())
        if sort_no == 1 or sort_no == 2:
            if sort_no == 1:
                return True
            else:
                return False
        else:
            print()
            print("Wrong option")
            print()


def files_size(arrange, fyl_format):
    files_dic = {}
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if fyl_format in file:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size in files_dic.keys():
                    files_ls = files_dic.get(file_size)
                    files_ls.append(file_path)
                    files_dic.update({file_size: files_ls})
                else:
                    files_dic.update({file_size: [file_path]})
    size_ls = list(files_dic.keys())
    size_ls.sort(reverse=arrange)
    for size in size_ls:
        print(size, " bytes")
        files = files_dic.get(size)
        for file in files:
            print(file)
    return files_dic


if __name__ == '__main__':
    root_dir = check_args()
    file_format = "."+get_fileformat()
    sort_order = issortingorder_asc()
    os.chdir(str(root_dir))
    size_dic = files_size(arrange=sort_order, fyl_format=file_format)
    
    
\\

import os
import sys
from os.path import splitext, getsize

args = sys.argv
if len(args) < 2:
    print("Directory is not specified")
else:
    ext = input("Enter file format:\n")
    print("Size sorting options:\n1. Descending\n2. Ascending\n")

    while True:
        n = input("Enter a sorting option:\n")
        if n in ("1", "2"):
            rev = True if n == "1" else False
            break
        else:
            print("Wrong option")

    dic = {}
    for root, dirs, files in os.walk(args[1]):
        for name in files:
            ex = splitext(name)[1]
            if ext and ex != '.' + ext:
                continue
            fn = os.path.join(root, name)
            size = getsize(fn)
            data = dic[size] if size in dic else []
            data.append(fn)
            dic[size] = data

    for size in sorted(dic, reverse=rev):
        print(f"\n{size} bytes")
        print(*dic[size], sep='\n')
 
\\


import os
import sys
from collections import defaultdict

try:
    root_folder = sys.argv[1]
except IndexError:
    print("Directory is not specified")
    sys.exit()

file_ext = "." + input("Enter file format:\n")

print("Size sorting options:", "1. Descending", "2. Ascending\n", sep="\n")
while (reverse := input("Enter a sorting option:\n")) not in "12":
    print("Wrong option\n")
else:
    reverse = reverse == "1"

files_by_size = defaultdict(list)

for root, _, files in os.walk(root_folder):
    for name in files:
        path = os.path.join(root, name)
        if file_ext in os.path.splitext(name)[1]:
            files_by_size[os.path.getsize(path)].append(path)

for size, files in sorted(files_by_size.items(), reverse=reverse):
    if len(files) > 1:
        print(f"\n{size} bytes", *files, sep="\n")

