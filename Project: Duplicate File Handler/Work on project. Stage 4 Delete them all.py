'''
Description
During previous stages, we have created a program that can find file duplicates. In this stage, we need to add the ability to delete files and print the information about them.

Objectives
Keep the functionality from the previous stages. To complete this stage, your program should do the following:

Ask a user whether they want to delete files. Expect either yes or no as the answer. Print Wrong option if it receives any other input. Repeat until a user provides a valid answer. If yes, read what files a user wants to delete and then delete them. Otherwise, abort the program;
Read a sequence of files that a user wants to delete and then delete them. Input should contain only file numbers separated by spaces. Print Wrong format if it receives empty string or any other input. Repeat until a user provides a valid answer;
Print the total freed up space in bytes.
Please note: you should use full path to file from root directory when printing or reading.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

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

Delete files?
> yes

Enter file numbers to delete:
> 1 2 5

Wrong format

Enter file numbers to delete:
> 1 2 4

Total freed up space: 14523488 bytes
 Report a typo

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
dupe_list = []
free_space = 0
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
                    dupe_list.append([filepath, sk])
                    counter += 1
                hash_set.add(hash_value)
    print()

print("Delete files?")
delete_files = input()
while delete_files not in ["yes", "no"]:
    print("Wrong option")
    delete_files = input()
    print()
if delete_files == "no":
    exit()

print("Enter file numbers to delete:")
file_numbers = [x for x in input().split()]
while len(file_numbers) < 1 or any(not x.isdigit() for x in file_numbers):
    print("wrong format")
    file_numbers = [x for x in input().split()]
while max(int(x) for x in file_numbers) > (len(dupe_list)):
    print("wrong format")
    file_numbers = [x for x in input().split()]

for file_num in file_numbers:
    full_path = dupe_list[int(file_num) - 1][0]
    os.remove(full_path)
    free_space += dupe_list[int(file_num) - 1][1]

print(f"Total freed up space: {free_space} bytes")



########################
# Classes/Structures:
# BinaryTree:
# - Each tree leaf contains a file size and pointer to list of hashes (Linked List Structure)
# - Root leaf contains information about number of duplicated files
#
# HashTable:
# - Each element contains file hash value, number of files with the hash
# - and pointer to list of files with the same hash (Linked List Structure)
#
# LinkedList:
# - each element contains full path to the file
#
# Finder
# - Class contains methods to read directory and files and build data structures
#
# Menu
# - Class contains methods to display program menus
#
#######################
import os
import sys
import hashlib


class WrongNumber(Exception):
    pass


if len(sys.argv) < 2:
    print('Directory is not specified')
    sys.exit(-1)

if_dir = [sys.argv[1]]


class BinaryTree:
    def __init__(self, size, file_hash, file_path):
        self.size = size
        self.hash_table = HashTable(file_hash, file_path)
        self.no_of_dup = 1
        self.freed = 0
        self.left = None
        self.right = None

    def tree_size(self, root):
        if root is None:
            return 0
        return 1 + self.tree_size(root.left) + self.tree_size(root.right)

    def add(self, root, node):
        if root.size > node.size:
            if root.left is None:
                root.left = node
                return
            self.add(root.left, node)
        else:
            if root.right is None:
                root.right = node
                return
            self.add(root.right, node)

    def update(self, tree_node, size, file_hash, file_path):
        if tree_node is None:
            return False
        if tree_node.size == size:
            if tree_node.hash_table.exists(tree_node.hash_table, file_hash):
                tree_node.hash_table.update(tree_node.hash_table, file_hash, file_path)
            else:
                tree_node.hash_table = tree_node.hash_table.add(tree_node.hash_table, HashTable(file_hash, file_path))
            return True
        if self.update(tree_node.left, size, file_hash, file_path):
            return
        self.update(tree_node.right, size, file_hash, file_path)

    def exists(self, tree_node, size):
        if tree_node is None:
            return False
        if tree_node.size == size:
            return True
        if self.exists(tree_node.left, size):
            return True
        if self.exists(tree_node.right, size):
            return True
        return False

    @staticmethod
    def _print(node):
        print(node.size, 'bytes')
        node.hash_table.files()

    def _print_duplicates(self, node):
        self.no_of_dup = node.hash_table.duplicates(no_of_duplicates=self.no_of_dup, size=node.size)

    def _delete(self, node, file_lst):
        no_of_del_files = node.hash_table.delete(file_lst)
        self.freed += no_of_del_files * node.size

    def process(self, node, duplicates=False, files_lst=None):
        if duplicates:
            self._print_duplicates(node)
        elif files_lst:
            self._delete(node, files_lst)
        else:
            self._print(node)

    def ascending(self, node, duplicates=False, files_to_delete=None):
        if node is None:
            return
        self.ascending(node.left, duplicates=duplicates, files_to_delete=files_to_delete)
        self.process(node, duplicates=duplicates, files_lst=files_to_delete)
        self.ascending(node.right, duplicates=duplicates, files_to_delete=files_to_delete)

    def descending(self, node, duplicates=False, files_to_delete=None):
        if node is None:
            return
        self.descending(node.right, duplicates=duplicates, files_to_delete=files_to_delete)
        self.process(node, duplicates=duplicates, files_lst=files_to_delete)
        self.descending(node.left, duplicates=duplicates, files_to_delete=files_to_delete)


class HashTable:
    def __init__(self, hash_value, file_path):
        self.hash_value = hash_value
        self.files_list = LinkedLists(file_path)
        self.no_of_files = 1
        self.next = None

    @staticmethod
    def add(head, hash_node):
        hash_node.next = head
        return hash_node

    @staticmethod
    def update(head, hash_value, file_path):
        node = head
        while node is not None:
            if node.hash_value == hash_value:
                node.files_list = node.files_list.add(node.files_list, LinkedLists(file_path))
                node.no_of_files += 1
                return
            node = node.next

    @staticmethod
    def exists(head, hash_value):
        node = head
        while node is not None:
            if node.hash_value == hash_value:
                return True
            node = node.next
        return False

    def files(self):
        node = self
        while node is not None:
            node.files_list.files(node.files_list)
            node = node.next

    def duplicates(self, no_of_duplicates=None, size=None):
        node = self
        found = None
        while node is not None:
            if node.no_of_files > 1:
                if found is None:
                    print(size, 'bytes')
                    found = True
                print('Hash: ', node.hash_value)
                no_of_duplicates = node.files_list.duplicates(node.files_list, no_of_duplicates)
            node = node.next
        return no_of_duplicates

    def delete(self, file_lst):
        node = self
        no_of_deleted = 0
        while node is not None:
            no_of_deleted += node.files_list.delete(node.files_list, file_lst)
            node = node.next
        return no_of_deleted


class LinkedLists:
    def __init__(self, file_path):
        self.file_path = file_path
        self.record = 0
        self.next = None

    @staticmethod
    def add(head, file_node):
        file_node.next = head
        return file_node

    @staticmethod
    def files(head):
        node = head
        while node is not None:
            print(node.file_path)
            node = node.next

    @staticmethod
    def duplicates(head, no_dup):
        node = head
        while node is not None:
            print(f'{no_dup}.', node.file_path)
            node.record = no_dup
            no_dup += 1
            node = node.next
        return no_dup

    @staticmethod
    def delete(head, files_to_delete):
        node = head
        no_of_deleted = 0
        while node is not None:
            if node.record in files_to_delete:
                os.remove(node.file_path)
                no_of_deleted += 1
            node = node.next
        return no_of_deleted


class Finder:
    def __init__(self, extension):
        self.tree = None
        self.extension = extension

    @staticmethod
    def _calculate_hash(path):
        with open(path, "rb") as fn:
            return hashlib.md5(fn.read()).hexdigest()

    def create_tree_node(self, file_path):
        file_hash = self._calculate_hash(file_path)
        file_size = os.stat(file_path).st_size
        if self.tree is None:
            self.tree = BinaryTree(file_size, file_hash, file_path)
        elif self.tree.exists(self.tree, file_size):
            self.tree.update(self.tree, file_size, file_hash, file_path)
        else:
            self.tree.add(self.tree, BinaryTree(file_size, file_hash, file_path))

    def get(self, directory):
        while directory:
            dirname = directory.pop()
            files = os.listdir(dirname)
            for file in files:
                file_path = os.path.join(dirname, file)
                if os.path.isfile(file_path) and file.endswith(self.extension):
                    self.create_tree_node(file_path)
                if os.path.isdir(file_path):
                    directory.append(file_path)


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def format():
        print('Enter file format:')
        return input()

    @staticmethod
    def sort():
        while True:
            print('Enter a sorting option:')
            print('1. Descending')
            print('2. Ascending')
            opt = int(input())
            if 1 <= opt <= 2:
                return opt
            print('Wrong option')

    @staticmethod
    def duplicates():
        while True:
            print('Check for duplicates?')
            opt = input().lower()
            if opt == 'no' or opt == 'yes':
                return True if opt == 'yes' else False
            print('Wrong options')

    @staticmethod
    def _files(nums):
        available_files = list(range(nums))
        while True:
            print('Enter file numbers to delete:')
            f_to_del = input()
            try:
                nums = [int(n) for n in f_to_del.split()]
                for n in nums:
                    if n not in available_files:
                        raise WrongNumber
                if not nums:
                    raise WrongNumber
                return nums
            except (ValueError, WrongNumber):
                print('Wrong format')

    def delete(self, nums):
        while True:
            print('Delete files?')
            opt = input().lower()
            if opt == 'no':
                return False
            elif opt == 'yes':
                return self._files(nums)
            else:
                print('Wrong format')


menu = Menu()

file_extension = menu.format()

finder = Finder(file_extension)
finder.get(if_dir)

if finder.tree is None:
    print('No files found')
    sys.exit(-1)

opt = menu.sort()
reverse = True if opt == 1 else False

if reverse:
    finder.tree.descending(finder.tree)
else:
    finder.tree.ascending(finder.tree)

opt = menu.duplicates()

if opt:
    if reverse:
        finder.tree.descending(finder.tree, duplicates=True)
    else:
        finder.tree.ascending(finder.tree, duplicates=True)

f_to_delete = menu.delete(finder.tree.no_of_dup)
if f_to_delete:
    if reverse:
        finder.tree.descending(finder.tree, files_to_delete=f_to_delete)
    else:
        finder.tree.ascending(finder.tree, files_to_delete=f_to_delete)

    print(f'Total freed up space: {finder.tree.freed} bytes')
    
    
by Adam Kwarcinski
