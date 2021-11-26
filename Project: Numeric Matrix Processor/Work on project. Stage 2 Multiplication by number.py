'''
Description
In this stage, you are going to implement the multiplication of a matrix by a constant. To do this, you need to multiply every element of the matrix by that constant. You can see the example below:

{\color{red}C} \times \begin{pmatrix} a_{1,1} & a_{1,2} & a_{1,3} \\ a_{2,1} & a_{2,2} & a_{2,3} \end{pmatrix} = \begin{pmatrix} {\color{red}C} \times a_{1,1} & {\color{red}C} \times a_{1,2} & {\color{red}C} \times a_{1,3} \\ {\color{red}C} \times a_{2,1} & {\color{red}C} \times a_{2,2} & {\color{red}C} \times a_{2,3}\end{pmatrix}C×( 
a 
1,1
​
 
a 
2,1
​
 
​
  
a 
1,2
​
 
a 
2,2
​
 
​
  
a 
1,3
​
 
a 
2,3
​
 
​
 )=( 
C×a 
1,1
​
 
C×a 
2,1
​
 
​
  
C×a 
1,2
​
 
C×a 
2,2
​
 
​
  
C×a 
1,3
​
 
C×a 
2,3
​
 
​
 )

Objectives
Write a program that:
1. reads a matrix and a constant,
2. outputs the result of their multiplication.

The first line of the input contains the number of rows and the number of columns of the matrix. The next lines contain rows of the matrix. The last line contains the constant.

The constant and the elements of the matrix are integers.

Examples
Example 1:

Input:

3 3
1 2 3
4 5 6
7 8 9
3
Output:

3 6 9
12 15 18
21 24 27
Example 2:

Input:

2 3
1 2 3
4 5 6
0
Output:

0 0 0
0 0 0

'''

# create matrix from user input
def get_matrix(size):
    matrix = []
    for x in range(size[0]):
        row = input().split()
        for y in range(size[1]):
            row[y] = int(row[y])
        matrix.append(row)
    return matrix


# print a matrix
def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=' ')
        print()


# main code
a_size = [int(a) for a in input().split()]
a_matrix = get_matrix(a_size)
multiplier = int(input())
prod_matrix = [[a_matrix[x][y] * multiplier for y in range(a_size[1])] for x in range(a_size[0])]
print_matrix(prod_matrix)


\\

from numpy import matrix


class Matrix:
    def __init__(self):
        self.n = None
        self.m = None
        self.matrix = None

    def matrix_reader(self):
        self.n, self.m = map(int, input().split())
        self.matrix = matrix([list(map(int, input().split())) for _ in range(self.n)])

    def __eq__(self, other):
        return self.n == other.n and self.m == other.m

    def __add__(self, other):
        return matrix(self.matrix) + matrix(other.matrix)

    def mul(self, number):
        self.matrix *= number

    def print_matrix(self):
        for col in self.matrix.tolist():
            print(*col)


a = Matrix()
a.matrix_reader()
a.mul(int(input()))
a.print_matrix()


\\

def read_matrix():
    dim = [int(x) for x in input().split()]
    matrix = []
    for i in range(dim[0]):
        matrix.append([int(x) for x in input().split()])
    return {"dim": (dim[0], dim[1]), "matrix": matrix}


def read_scalar():
    num = int(input())
    return num


def addition(m1, m2):
    result = []
    for i in range(m1["dim"][0]):
        row = map(lambda a, b: a + b, m1["matrix"][i], m2["matrix"][i])
        result.append(row)
    return result


def scalar_multiply(matrix, number):
    result = []
    for i in range(matrix["dim"][0]):
        row = map(lambda a: a * number, matrix["matrix"][i])
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(x) for x in row]))


def main():
    matrix = read_matrix()
    number = read_scalar()
    print_matrix(scalar_multiply(matrix, number))


if __name__ == "__main__":
    main()

    
\\

def get_dimensions():
    try:
        n, m = [int(x) for x in input().split()]
    except ValueError:
        print("Invalid input!")
        return None
    else:
        return n, m


def fill_matrix(n):
    return [[int(x) for x in input().split()] for _ in range(n)]


def get_matrix():
    n, m = get_dimensions()
    matrix = None
    if n:
        matrix = fill_matrix(n)
    return matrix


def add_matrices(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return [[x + y for x, y in zip(row_A, row_B)] for row_A, row_B in zip(A, B)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def scalar_multiplication(matrix, scalar):
    return [[scalar * x for x in row] for row in matrix]


def main():
    matrix = get_matrix()
    scalar = int(input())
    end_matrix = scalar_multiplication(matrix=matrix, scalar=scalar)
    print_matrix(end_matrix)


if __name__ == "__main__":
    main()
