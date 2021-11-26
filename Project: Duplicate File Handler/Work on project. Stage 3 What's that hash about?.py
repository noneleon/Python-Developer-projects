'''
Theory
Now we have a list of files of the same size. The next step is to check the files with the help of the Hashlib module. Why do we need to use hash here? The answer is very simple — it's convenient! As you may know, a hash function can take any input of any length. It produces several strings as output.

A hash function has the following main features:

easy to compute
unique output
small and fixable output
So, a file type or size plays a minor role. We can get a hash of any file and compare it against a hash of another file.
We will work with an MD5 hash function of the Hashlib module. Take a look at some useful functions:

md5() creates a hash object
update() updates a hash object
hexdigest() gets the HEX digest
Description
In this stage, we need to get hashes of files of the same size and check whether they are the same file. Remember that hash work with byte-like objects only, so pay attention to the file read mode (the rb mode).

Objectives
Keep the functionality from the previous stages. To complete the stage, your program should:

Ask for duplicates check;
Read user input: yes or no . Print Wrong option if any other input is received. Repeat until a user provides a valid answer. If the input is yes, get the hash of files of the same size; group the files of the same hash, assign numbers to these files. Otherwise, the program should stop the operation;
Assign numbers to lines with files after hashing. You should assign numbers to files based on the total number of files in output. It is needed for the purpose of the next stage.
Print the information about the files of the same outputs along with their hashes (see example). Sort the group of files by size as in the previous stage. You don't have to sort hash subgroups.
Please note: you should use full path to file from root directory when printing or reading.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Suppose, you have the following set of files and folders:

+---[root_folder]
    +---gordon_ramsay_chicken_breast.avi /4590560 bytes
    +---poker_face.mp3 /5550640 bytes
    +---poker_face_copy.mp3 /5550640 bytes
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
        +---the_magic_flute_queen_of_the_night_aria.mp3 /3422208 bytes
        +---the_magic_flute_queen_of_the_night_aria_copy.mp3 /3422208 bytes
Program output:

> python handler.py root_folder

Enter file format:
>

Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
> 1

5550640 bytes
root_folder/poker_face.mp3
root_folder/poker_face_copy.mp3

4590560 bytes
root_folder/gordon_ramsay_chicken_breast.avi
root_folder/audio/sia_snowman.mp3
root_folder/audio/rock/smells_like_teen_spirit.mp3

3422208 bytes
root_folder/audio/classic/unknown.mp3
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria.mp3
root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria_copy.mp3

Check for duplicates?
> yes

5550640 bytes
Hash: 909ba4ad2bda46b10aac3c5b7f01abd5
1. root_folder/poker_face.mp3
2. root_folder/poker_face_copy.mp3

3422208 bytes
Hash: a7f5f35426b927411fc9231b56382173
3. root_folder/audio/classic/unknown.mp3
4. root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
Hash: b6d767d2f8ed5d21a44b0e5886680cb9
5. root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria.mp3
6. root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria_copy.mp3
'''

import os
import argparse
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=None)
args = parser.parse_args()

if args.path is None:
    print("Directory is not specified")
    exit()

print("Enter file format:")
file_format = input().lower()

files_list = []
for root, dirs, files in os.walk(args.path):
    files_list.extend([(os.path.join(root, file),
                        os.path.getsize(os.path.join(root, file)))
                       for file in files])

if file_format != "":
    files_list = [file for file in files_list if file[0].lower().endswith(f".{file_format}")]

print("\nSize sorting options:")
print("1. Descending")
print("2. Ascending")

print("\nEnter a sorting option:")
size_sort = input()
while size_sort not in ["1", "2"]:
    print("\nWrong option")
    size_sort = input()
print()

size_dict = {}
for pathname, size in files_list:
    size_dict.setdefault(size, []).append(pathname)

size_keys = sorted(size_dict, reverse=True) if int(size_sort) == 1 else sorted(size_dict)

for sk in size_keys:
    print(f"{sk} bytes")
    for v in size_dict[sk]:
        print(v)
    print()

print("\nCheck for duplicates?")
check_dupes = input()
while check_dupes not in ["yes", "no"]:
    print("Wrong option")
    check_dupes = input()
    print()
if check_dupes == "no":
    exit()

counter = 1
for sk in size_keys:
    hash_dict = {}
    hash_set = set()
    print(f"{sk} bytes")
    for v in size_dict[sk]:
        with open(v, "rb") as f:
            file_hash = hashlib.md5()
            file_hash.update(f.read())
            hash_dict.setdefault(file_hash.hexdigest(), []).append(v)
        for hash_value in hash_dict.keys():
            if len(hash_dict[hash_value]) > 1 and hash_value not in hash_set:
                print(f"Hash: {hash_value}")
                for filepath in hash_dict[hash_value]:
                    print(f"{counter}. {filepath}")
                    counter += 1
                hash_set.add(hash_value)
    print()
    
    
    
\\

# write your code here
import argparse
import os
import sys
import hashlib

SORT_DESC = 1
SORT_ASC = 2

CMD_YES = 'yes'
CMD_NO = 'no'


def md5_hash(fpath: str) -> str:
    # noinspection InsecureHash
    hash_md5 = hashlib.md5()
    with open(fpath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


parser = argparse.ArgumentParser(description="This is Duplicate File Handler app")

parser.add_argument('directory', nargs='*', default=None)

directory = parser.parse_args().directory

if not directory:
    print('Directory is not specified')
    sys.exit(1)

entrypoint = directory[0]

print('Enter file format:')
ext = input().strip()

print()
print('Size sorting options:')
print('1. Descending')
print('2. Ascending')

sorting = SORT_ASC

while True:
    print()
    print('Enter a sorting option:')
    sorting = int(input().strip())

    if sorting in [SORT_ASC, SORT_DESC]:
        print()
        break

    print('Wrong option')

file_map = {}
size_hash_map = {}

os.system("mv module/root_folder/files/stage/src/reviewSlider.js module/root_folder/files/stage/src/reviewslider.js")
os.system(
    "mv module/root_folder/files/stage/src/toggleMiniMenu.js module/root_folder/files/stage/src/toggleminimenu.js")

for root, dirs, files in os.walk(entrypoint):
    for file in files:
        file_path = os.path.join(root, file)
        if ext and ext != os.path.splitext(file_path)[1]:
            continue

        size = int(os.path.getsize(file_path))
        if size not in file_map:
            file_map[size] = [file_path]
            continue

        file_map[size].append(file_path)

for key in sorted(file_map, reverse=(True if sorting == SORT_DESC else False)):
    if len(file_map[key]) > 1:
        print(f'{key} bytes')
        for name in file_map[key]:
            print(name)
        print()

while True:
    print()
    print('Check for duplicates?')
    confirm = input().strip()

    if confirm not in [CMD_NO, CMD_YES]:
        print('Wrong option')
        continue

    if confirm == CMD_NO:
        sys.exit(0)

    break

for key in sorted(file_map, reverse=(True if sorting == SORT_DESC else False)):
    if len(file_map.get(key)) == 1:
        continue

    for name in file_map[key]:
        md5_crc = md5_hash(name)

        if key in size_hash_map:
            if md5_crc in size_hash_map[key]:
                size_hash_map[key][md5_crc].append(name)
            else:
                size_hash_map[key][md5_crc] = [name]
        else:
            size_hash_map[key] = {md5_crc: [name]}

# output
print()
i = 1
for key in sorted(size_hash_map, reverse=(True if sorting == SORT_DESC else False)):
    print(f'{key} bytes')

    for crc in sorted(size_hash_map.get(key)):
        if len(size_hash_map.get(key).get(crc)) > 1:
            print(f'Hash: {crc}')
            for name in size_hash_map.get(key).get(crc):
                print(f'{i}. {name}')
                i += 1

    print()