'''
Description
Your task is to make a smart calculator. What do you usually expect from a calculator? Of course, it is bound to support 4 basic operations: multiplication, division, addition, and subtraction. But we don't stop there and add the ability to calculate expressions containing parenthesis and the ability to remember the previous result. This will be a console application, which you will improve gradually, from simple to complex.
So, the first version of the calculator will only support the addition operation for two numbers. In this version, you will not receive the plus symbol (+) as an input, you will accept this as an unwritten rule (because only one operation is supported).

Objective
Write a program that reads two integer numbers from the same line and prints their sum in the standard output. Numbers can be positive, negative, or zero.

Example
The example below shows the input and the corresponding output. Your program should work in the same way. Do not add extra characters after the output!

The greater-than symbol followed by a space (> ) represents the user input. Notice that it's not the part of the input.

> 5 8
13

'''

# write your code here
a, b = input().split()
print(int(a) + int(b))

\\

print(sum([int(x) for x in input().split()]))