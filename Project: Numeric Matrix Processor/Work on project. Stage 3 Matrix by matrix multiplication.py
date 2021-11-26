'''
Description
The next stage is the multiplication of matrices. This operation is a little more complex because it’s not enough to simply multiply the corresponding elements.

Unlike with addition, the sizes of the matrices can be different: the only restriction is that the number of columns in the first matrix should equal the number of rows for the second matrix. Check out a comprehensive video by 3Blue1Brown about matrix multiplication.

The multiplication of AA matrix with nn rows and mm columns and BB matrix with mm rows and kk columns is C_{n , k} = A_{n , m} \times B_{m, k}C 
n,k
​
 =A 
n,m
​
 ×B 
m,k
​
 .

The resulting matrix has nn rows and kk columns, where every element is a sum of the multiplication of mm elements across the rows of matrix AA by mm elements down the columns of matrix BB.

Another really important thing is that A_{i , j} \times B_{j , k}A 
i,j
​
 ×B 
j,k
​
  is not equal to B_{j, k} \times A_{i , j}B 
j,k
​
 ×A 
i,j
​
 . In fact, these are not even possible to multiply if k \ne i.k

=i. If k = ik=i, the resulting matrices would still be different.

Take a look at this example of matrix multiplication:

\begin{pmatrix} 1 & 7 & 7 \\ 6 & 6 & 4 \\ 4 & 2 & 1 \end{pmatrix} \times \begin{pmatrix} 3 & 2 & 4 \\ 5 & 5 & 9 \\ 8 & 0 & 10 \end{pmatrix} = \begin{pmatrix} 1\times3+7\times5+7\times8 & 1\times2+7\times5+7\times0 & 1\times4+7\times9+7\times10 \\ 6\times3+6\times5+4\times8 & 6\times2+6\times5+4\times0 & 6\times4+6\times9+4\times10 \\ 4\times3+2\times5+1\times8 & 4\times2+2\times5+1\times0 & 4\times4+2\times9+1\times10 \end{pmatrix} = \begin{pmatrix} 94 & 37 & 137 \\ 80 & 42 & 118 \\ 30 & 18 & 44 \end{pmatrix} 
⎝
⎛
​
  
1
6
4
​
  
7
6
2
​
  
7
4
1
​
  
⎠
⎞
​
 × 
⎝
⎛
​
  
3
5
8
​
  
2
5
0
​
  
4
9
10
​
  
⎠
⎞
​
 = 
⎝
⎛
​
  
1×3+7×5+7×8
6×3+6×5+4×8
4×3+2×5+1×8
​
  
1×2+7×5+7×0
6×2+6×5+4×0
4×2+2×5+1×0
​
  
1×4+7×9+7×10
6×4+6×9+4×10
4×4+2×9+1×10
​
  
⎠
⎞
​
 = 
⎝
⎛
​
  
94
80
30
​
  
37
42
18
​
  
137
118
44
​
  
⎠
⎞
​
 

Objectives
In this stage, you should write a program that can do all operations on matrices that you've learned.

Write a program that does the following:

Prints a menu consisting of 4 options. The example shows what the menu should look like.
Reads the user's choice.
Reads all data (matrices, constants) needed to perform the chosen operation. The example shows the input format in each case.
Calculates the result and outputs it. The example shows how your output should look like.
Repeats all these steps.
The program should keep repeating this until the "Exit" option is chosen.

If some operation cannot be performed, output a warning message.

Also, you should support floating-point numbers.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 1
Enter size of first matrix: > 4 5
Enter first matrix:
> 1 2 3 4 5
> 3 2 3 2 1
> 8 0 9 9 1
> 1 3 4 5 6
Enter size of second matrix: > 4 5
Enter second matrix:
> 1 1 4 4 5
> 4 4 5 7 8
> 1 2 3 9 8
> 1 0 0 0 1
The result is:
2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 2
Enter size of matrix: > 2 2
Enter matrix:
> 1.5 7.0
> 6.0 5.0
Enter constant: > 0.5
The result is:
0.75 3.5
3.0 2.5

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 3
Enter size of first matrix: > 3 3
Enter first matrix:
> 1 7 7
> 6 6 4
> 4 2 1
Enter size of second matrix: > 3 3
Enter second matrix:
> 3 2 4
> 5 5 9
> 8 0 10
The result is:
94 37 137
80 42 118
30 18 44

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 1
Enter size of first matrix: > 2 2
Enter first matrix:
> 1 2
> 3 2
Enter size of second matrix: > 1 1
Enter second matrix:
> 1
The operation cannot be performed.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 0

'''

# create matrix from user input
def get_matrix(size):
    matrix = []
    for x in range(size[0]):
        row = input().split()
        for y in range(size[1]):
            row[y] = float(row[y])
        matrix.append(row)
    return matrix


# multiply matrix by constant
def mult_const():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    multiplier = float(input('Enter constant: '))
    prod_matrix = [[matrix[x][y] * multiplier for y in range(size[1])] for x in range(size[0])]
    print('The result is:')
    print_matrix(prod_matrix)


# multiply two matrices together
def mult_matrices():
    a_size = [int(a) for a in input('Enter size of first matrix: ').split()]
    print('Enter first matrix:')
    a_matrix = get_matrix(a_size)
    b_size = [int(b) for b in input('Enter size of second matrix: ').split()]
    print('Enter second matrix:')
    b_matrix = get_matrix(b_size)
    prod_matrix = [[sum(a*b for a,b in zip(a_row,b_col)) for b_col in zip(*b_matrix)] for a_row in a_matrix]
    print_matrix(prod_matrix)


# add two matrices together
def add_matrices():
    a_size = [int(a) for a in input('Enter size of first matrix: ').split()]
    print('Enter first matrix:')
    a_matrix = get_matrix(a_size)
    b_size = [int(b) for b in input('Enter size of second matrix: ').split()]
    print('Enter second matrix:')
    b_matrix = get_matrix(b_size)
    if a_size[0] != b_size[0] or a_size[0] != b_size[0]:
        print('ERROR')
    else:
        sum_matrix = [[a_matrix[x][y] + b_matrix[x][y] for y in range(a_size[1])] for x in range(a_size[0])]
        print_matrix(sum_matrix)


# print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(*row)


# main code
while True:
    print(r'''1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        0. Exit''')
    choice = int(input('Your choice: '))
    if choice == 0:
        exit()
    elif choice == 1:
        add_matrices()
    elif choice == 2:
        mult_const()
    elif choice == 3:
        mult_matrices()
        
        
\\

from numpy import matrix


class Matrix:
    def __init__(self, name):
        self.name = name
        self.n, self.m = None, None
        self.matrix = None

    def matrix_reader(self):
        self.n, self.m = map(int, input(f'Enter size of {self.name}matrix: ').split())
        print(f'Enter {self.name}matrix:')
        self.matrix = matrix([list(map(float, input().split())) for _ in range(self.n)])

    def __eq__(self, other):
        return self.n == other.n and self.m == other.m

    def __add__(self, other):
        return self.matrix + other.matrix

    def mul(self, number):
        return self.matrix * number

    def __mul__(self, other):
        return self.matrix * other.matrix

    def print_matrix(self):
        for col in self.matrix.tolist():
            print(*col)


while True:
    print('1. Add matrices', '2. Multiply matrix by a constant',
          '3. Multiply matrices', '0. Exit', sep='\n')
    choice = int(input('Your choice: '))
    if choice == 0:
        exit()
    if choice == 1:
        first = Matrix('first ')
        first.matrix_reader()
        second = Matrix('second ')
        second.matrix_reader()
        print('The result is:')
        if first == second:
            result = Matrix('')
            result.matrix = first + second
            result.print_matrix()
        else:
            print('The operation cannot be performed.')
    if choice == 2:
        first = Matrix('')
        first.matrix_reader()
        const = float(input('Enter constant: '))
        result = Matrix('')
        result.matrix = first.mul(const)
        print('The result is:')
        result.print_matrix()
    if choice == 3:
        first = Matrix('first ')
        first.matrix_reader()
        second = Matrix('second ')
        second.matrix_reader()
        print('The result is:')
        if first.m == second.n:
            result = Matrix('')
            result.matrix = first * second
            result.print_matrix()
        else:
            print('The operation cannot be performed.')
\\

def read_matrix(num=""):
    dim = [int(x) for x in input(f"Enter size of {num}matrix: ").split()]
    print(f"Enter {num}matrix:")
    matrix = []
    for i in range(dim[0]):
        matrix.append([float(x) if '.' in x else int(x) for x in input().split()])
    return {"dim": (dim[0], dim[1]), "matrix": matrix}


def read_scalar():
    num = input("Enter constant: ")
    if '.' in num:
        num = float(num)
    else:
        num = int(num)
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


def multiply_matrices(m1, m2):
    result = []
    for i in range(m1["dim"][0]):  # rows
        row = []
        for j in range(m2["dim"][1]):  # columns
            elem = 0
            for k in range(m1["dim"][1]):
                elem += m1["matrix"][i][k] * m2["matrix"][k][j]
            row.append(elem)
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(x) for x in row]))


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    choice = int(input("Your choice: "))
    return choice


def mode_1():  # add matrices
    matrix_1 = read_matrix('first ')
    matrix_2 = read_matrix('second ')
    if matrix_1["dim"] != matrix_2["dim"]:
        print("The operation cannot be performed.")
        return

    print("The result is:")
    print_matrix(addition(matrix_1, matrix_2))


def mode_2():  # scalar multiply
    matrix = read_matrix()
    scalar = read_scalar()

    print("The result is:")
    print_matrix(scalar_multiply(matrix, scalar))


def mode_3():  # multiply matrices
    matrix_1 = read_matrix('first ')
    matrix_2 = read_matrix('second ')
    if matrix_1["dim"][1] != matrix_2["dim"][0]:
        print("The operation cannot be performed.")
        return

    print("The result is:")
    print_matrix(multiply_matrices(matrix_1, matrix_2))


def main():
    while True:
        mode = menu()
        if mode == 1:
            mode_1()
        elif mode == 2:
            mode_2()
        elif mode == 3:
            mode_3()
        else:
            break
        print()


if __name__ == "__main__":
    main()

