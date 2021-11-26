'''
Matrices have a wide range of applications in programming: they're used for digital image processing, graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.

Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. In this project, you will learn how to read and output matrices, do operations on them, and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, and later the elements will be floating-point numbers.

Description
Let’s start with matrix addition.

For two matrices to be added, they must have an equal number of rows and columns. The sum of matrices AA and BB will be a matrix with the same number of rows and columns as AA or BB. The sum of AA and BB, denoted A + BA+B or B + AB+A, is computed by adding the corresponding elements of AA and BB: (A + B)_{n,m} = A_{n, m} + B_{n, m}(A+B) 
n,m
​
 =A 
n,m
​
 +B 
n,m
​
 . Notice that n in the index _{n,m} 
n,m
​
  represents the row and m represents the column.

Here is a simple example with numbers:

\begin{pmatrix} 2 & 4 &5 & 6 \\ 6 & 6 &7 & 8 \\ 5 & 0 &0 & 1 \\ 8 & 8 &2 & 9 \\ \end{pmatrix} +\begin{pmatrix} 7 & 7 &0 & 1 \\ 9 & 9 &9 & 2 \\ 5 & 4 &3 & 12 \\ 0 & 6 &5 & 6 \\ \end{pmatrix} = \begin{pmatrix} 2+7 & 4+7 &5+0 & 6+1 \\ 6+9 & 6+9 &7+9 & 8+2 \\ 5+5 & 0+4 &0+3 & 1+12 \\ 8+0 & 8+6 &2+5 & 9+6 \\ \end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
2
6
5
8
​
  
4
6
0
8
​
  
5
7
0
2
​
  
6
8
1
9
​
  
⎠
⎟
⎟
⎟
⎞
​
 + 
⎝
⎜
⎜
⎜
⎛
​
  
7
9
5
0
​
  
7
9
4
6
​
  
0
9
3
5
​
  
1
2
12
6
​
  
⎠
⎟
⎟
⎟
⎞
​
 = 
⎝
⎜
⎜
⎜
⎛
​
  
2+7
6+9
5+5
8+0
​
  
4+7
6+9
0+4
8+6
​
  
5+0
7+9
0+3
2+5
​
  
6+1
8+2
1+12
9+6
​
  
⎠
⎟
⎟
⎟
⎞
​
 

Objectives
In this stage, you should write a program that:

Reads matrix AA from the input.
Reads matrix BB from the input.
Outputs their sum if it is possible to add them. Otherwise, it should output the ERROR message.
Each matrix in the input is given in the following way: the first line contains the number of rows nn and the number of columns mm. Then nn lines follow, each containing mm integers representing one row of the matrix.

Output the result in the same way but don't print the dimensions of the matrix.

Examples
Example 1:

Input:

4 5
1 2 3 4 5
3 2 3 2 1
8 0 9 9 1
1 3 4 5 6
4 5
1 1 4 4 5
4 4 5 7 8
1 2 3 9 8
1 0 0 0 1
Output:

2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7
Example 2:

Input:

2 3
1 4 5
4 5 5
4 5
0 1 0 4 5
1 7 8 9 4
1 2 3 5 6
1 3 4 3 8
Output:

ERROR
 Report a typo

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


# add two matrices together
def add_matrix(matrixA, matrixB, size):
    matrix = []
    for x in range(size[0]):
        for y in range(size[1]):
            matrix[x][y] = matrixA[x][y] + matrixB[x][y]
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
b_size = [int(b) for b in input().split()]
b_matrix = get_matrix(b_size)
if a_size[0] != b_size[0] or a_size[0] != b_size[0]:
    print('ERROR')
else:
    sum_matrix = [[a_matrix[x][y] + b_matrix[x][y] for y in range(a_size[1])] for x in range(a_size[0])]
    print_matrix(sum_matrix)

    
    
\\

from numpy import matrix


class Matrix:

    def __init__(self):
        self.n = None
        self.m = None
        self.matrix = []

    def matrix_reader(self):
        self.n, self.m = map(int, input().split())
        self.matrix = [list(map(int, input().split())) for _ in range(self.n)]

    def __eq__(self, other):
        return self.n == other.n and self.m == other.m

    def __add__(self, other):
        return (matrix(self.matrix) + matrix(other.matrix)).tolist()


def print_matrix(arr):
    for col in arr:
        print(*col)


a = Matrix()
a.matrix_reader()
b = Matrix()
b.matrix_reader()
if a == b:
    print_matrix(a + b)
else:
    print('ERROR')


\\
def get_int(matrix):
    matrix_size = matrix.split(' ')
    matrix_size = [int(nr) for nr in matrix_size]
    return matrix_size


matrix_a = []
matrix_a_size = get_int(input())
for index in range(matrix_a_size[0]):
    matrix_a.append(get_int(input()))
matrix_b = []
matrix_b_size = get_int(input())
for index in range(matrix_b_size[0]):
    matrix_b.append(get_int(input()))
result = []
if matrix_b_size == matrix_a_size:
    for index in range(matrix_a_size[0]):
        result = [matrix_a[index][nr] + matrix_b[index][nr] for nr in range(matrix_a_size[1])]
        print(*result)
else:
    print('ERROR')



