'''
Description
It'd be great if universities could enroll everybody, but it's not very realistic, is it? Let's refine our algorithm. In this stage we need to set a threshold of the mean score — if the mean score of the applicant is equal to or greater than 60.0, the program should notify the applicant about the acceptance to the university. Otherwise, inform them about the rejection.

Objectives
At this stage, your program should:

Read the numbers and output the mean score, as in the previous stage.
If the mean score is equal to or greater than 60.0, output the following message: Congratulations, you are accepted!
If the mean score is less than 60.0, output the following message: We regret to inform you that we will not be able to offer you admission.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: the applicant is enrolled

> 70
> 56
> 81
69.0
Congratulations, you are accepted!
Example 2: the applicant is rejected

> 100
> 43
> 27
56.666666666666664
We regret to inform you that we will not be able to offer you admission.


'''

# write your code here
a = int(input())
b = int(input())
c = int(input())
d= (a+b+c)/3
print(d)
if d >= 60.0:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
    
\\
class Candidate:
    def __init__(self):
        self.exams = []
        self.mean_result = 0

    def set_mean_results(self):
        self.mean_result = (sum(self.exams)) / 3.0


def main():
    candidate = Candidate()
    candidate.exams = [int(input()) for i in range(3)]
    candidate.set_mean_results()

    print(candidate.mean_result)
    if candidate.mean_result >= 60:
        print("Congratulations, you are accepted!")
    else:
        print("We regret to inform you that we will not be able to offer you admission.")


if __name__ == "__main__":
    main()
\\

from statistics import mean
m = mean([int(input()) for _ in range(3)])
print(m)
print("Congratulations, you are accepted!" if m >= 60 else 
    "We regret to inform you that we will not be able to offer you admission.")
