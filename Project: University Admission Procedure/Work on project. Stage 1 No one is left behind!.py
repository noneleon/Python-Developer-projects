'''
Description
Let's create a program that will help the university to determine the best candidates for enrolling!

The first step is very simple. An applicant needs to take three exams and submit the scores. The score of an exam can vary from 0 to 100. Your program should read the numbers representing the exam scores, calculate the mean exam score, and output it. And enroll the applicant to the university, as there are no other contestants yet.

Objectives
At this stage, your program should:

Take three inputs as integer numbers. They are the exam results.
Calculate the mean score of all three numbers. If the mean is a fractional number, don't discard the fractional part.
Print the resulting number.
Print the Congratulations, you are accepted! line.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

> 75
> 90
> 68
77.66666666666667
Congratulations, you are accepted!

'''

# write your code here
a = int(input())
b = int(input())
c = int(input())
print((a+b+c)/3)
print("Congratulations, you are accepted!")


\\


