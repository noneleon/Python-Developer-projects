'''
Description
Things are heating up! Our university has become trendy, so the applicants are rushing in. Your program has to be adapted to this — unfortunately, we cannot enroll everybody. The program will need to rank the potential students and determine who's going to get admitted. At this stage, you'll need to work with the Grade Point Average (GPA). It is the mean grade of all high school courses. We don't need the threshold, for now, a certain number of applicants with the best GPA will be accepted instead.

Theory
To proceed further we need to understand the basics of sorting. To use more than one attribute for list sorting, use the following syntax:

not_sorted_list = [['c', 11], ['a', 11], ['c', 10]]
sorted_list = sorted(not_sorted_list, key = lambda x: (x[0], x[1]))
print(sorted_list)
# [['a', 11], ['c', 10], ['c', 11]]
In this example, the first value (x[0]) of each element of the not_sorted_list is used for sorting in the first place. If these values are equal, the second value (x[1]) is used to determine which element is greater.

A problem may occur if you want to sort the list in ascending order by the first value and in the descending order by the second value. For example, you have two values to sort the list by: score and time.

# the first element in each nested list is score
# the second element is time
not_sorted_list = [[531, 11.76], [401, 5.11], [531, 10.05]]
You want to sort your list in such a way that the elements with the highest score and the smallest time value would go before the elements with a lower score and greater time value. To do this, you can simply inverse one of the values by adding a minus in front of it:

# both lines will lead to the same result
sorted_list = sorted(not_sorted_list, key = lambda x: (-x[0], x[1]))
sorted_list = sorted(not_sorted_list, reverse=True, key = lambda x: (x[0], -x[1]))
print(sorted_list)
# [[531, 10.05], [531, 11.76], [401, 5.11]]
Objectives
At this stage, your program should:

Read the first input, an N integer representing the total number of applicants.
Read the second input, an M integer representing the number of applicants that should be accepted to the university.
Read N lines from the input. Each line contains the first name, the last name, and the applicant's GPA. These values are separated by one whitespace character. A GPA is a floating-point number with two decimals.
Output the Successful applicants: message.
Output M lines for applicants with the top-ranking GPAs. Each line should contain the first and the last name of the applicant separated by a whitespace character. Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on.
If two applicants have the same GPA, rank them in alphabetical order using their full names (we know it's not really fair to choose students by their names, but what choice do we have?)
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> 5
> 3
> Cole Collins 3.68
> Dolores Baldwin 3.40
> Brett Boyer 2.45
> Nora Alston 3.71
> Jessy Moore 3.14
Successful applicants:
Nora Alston
Cole Collins
Dolores Baldwin
Example 2: applicants with equal GPA, note that the full name is used to sort these applicants

> 3
> 2
> Albert Collins 3.02
> Albert Nelson 3.02
> Cole Allen 3.02
Successful applicants:
Albert Collins
Albert Nelson
'''

# write your code here
N = int(input())
n = int(input())
x = {}
for i in range(N):
    a,b,c = input().split()
    d = a + " "+ b
    x[d] = c
sorted_list = sorted(x.items(), key=lambda x: x[1], reverse=True)
print("Successful applicants:")
for i in range(n):
    print(sorted_list[i][0])
    
\\

applicantsnum = int(input())
toaccept = int(input())

applicants = [[f"{el[0]} {el[1]}", float(el[2])] for el in [input().split() for _ in range(applicantsnum)]]
accepted = sorted(applicants, key=lambda ap: (-ap[1], ap[0]))[:toaccept]
print("Successful applicants:", *[accepted[0] for accepted in accepted], sep="\n")

\\

# write your code here
def initial_code():
    mark = [int(input()) for _ in range(3)]
    mean_score = sum(mark) / len(mark)
    print(mean_score)

    if mean_score >= 60:
        print("Congratulations, you are accepted!")
    else:
        print("We regret to inform you that we will not be able to offer you admission.")


N = int(input())
M = int(input())

student_list = []

for x in range(N):
    student_list.append(input().split())
    student_list[x][2] = float(student_list[x][2])

student_list.sort(key=lambda x: (-x[2], x[0], x[1]))

success_applicant = [student_list[x] for x in range(M)]

print('Successful applicants:')
for student in success_applicant:
    print(student[0], student[1])

    
    
\\

def read_scores(num_applicants):
    scores = []
    for _ in range(num_applicants):
        first_name, last_name, gpa = input().split()
        scores.append([first_name, last_name, float(gpa)])
    return scores


def successful_applicants(num_acceptable, scores):
    return sorted(scores, key=lambda x: (-x[2], f"{x[0]} {x[1]}"))[:num_acceptable]


def print_successful_applicants(num_acceptable, scores):
    print("Successful applicants:")
    for successful_applicant in successful_applicants(num_acceptable, scores):
        print(successful_applicant[0], successful_applicant[1])


def task():
    num_applicants = int(input())
    num_acceptable = int(input())
    scores = read_scores(num_applicants)
    print_successful_applicants(num_acceptable, scores)


if __name__ == '__main__':
    task()



