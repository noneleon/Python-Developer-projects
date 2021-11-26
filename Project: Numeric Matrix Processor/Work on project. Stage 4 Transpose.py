'''
Description
In this stage, you should implement matrix transposition. Matrix transposition is an operation in linear algebra that replaces rows with columns and returns a new matrix as a result. This is an operation on just a single matrix.

The main diagonal of a matrix is a line with elements from a_{1, 1}a 
1,1
​
  to a_{n,n}a 
n,n
​
 :

\begin{pmatrix} {\color{red}a_{1,1}} & a_{1,2} & a_{1,3}& a_{1,4} \\ a_{2,1} & {\color{red}a_{2,2}} & a_{2,3} & a_{2,4} \\ a_{3,1} & a_{3,2} & {\color{red}a_{3,3}} & a_{3,4} \\ a_{4,1} & a_{4,2} & a_{4,3}& {\color{red}a_{4,4}} \end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
a 
1,1
​
 
a 
2,1
​
 
a 
3,1
​
 
a 
4,1
​
 
​
  
a 
1,2
​
 
a 
2,2
​
 
a 
3,2
​
 
a 
4,2
​
 
​
  
a 
1,3
​
 
a 
2,3
​
 
a 
3,3
​
 
a 
4,3
​
 
​
  
a 
1,4
​
 
a 
2,4
​
 
a 
3,4
​
 
a 
4,4
​
 
​
  
⎠
⎟
⎟
⎟
⎞
​
 

The side diagonal of a matrix is a line from a_{1, n}a 
1,n
​
  to a_{n, 1}a 
n,1
​
 :

\begin{pmatrix} a_{1,1} & a_{1,2} & a_{1,3}& {\color{red}a_{1,4}} \\ a_{2,1} & a_{2,2} & {\color{red}a_{2,3}} & a_{2,4} \\ a_{3,1} & {\color{red}a_{3,2}} & a_{3,3} & a_{3,4} \\ {\color{red}a_{4,1}} & a_{4,2} & a_{4,3}& a_{4,4}\end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
a 
1,1
​
 
a 
2,1
​
 
a 
3,1
​
 
a 
4,1
​
 
​
  
a 
1,2
​
 
a 
2,2
​
 
a 
3,2
​
 
a 
4,2
​
 
​
  
a 
1,3
​
 
a 
2,3
​
 
a 
3,3
​
 
a 
4,3
​
 
​
  
a 
1,4
​
 
a 
2,4
​
 
a 
3,4
​
 
a 
4,4
​
 
​
  
⎠
⎟
⎟
⎟
⎞
​
 

In math, there is only one type of matrix transposition: transposition along the main diagonal. In this stage, you should implement the other three types of transposition to practice your array skills. These four types are:

transposition along the main diagonal
transposition along the side diagonal
transposition along the vertical line
transposition along the horizontal line
Transposition along the main diagonal is shown below:

\begin{pmatrix} 1 & 1 & 1 & 1\\ 2 & 2 & 2 & 2\\ 3 & 3 & 3 & 3 \\ 4 & 4 & 4 & 4 \end{pmatrix}^T \to \begin{pmatrix} 1 & 2 & 3 & 4\\ 1 & 2 & 3 & 4\\ 1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4 \end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
1
2
3
4
​
  
1
2
3
4
​
  
1
2
3
4
​
  
1
2
3
4
​
  
⎠
⎟
⎟
⎟
⎞
​
  
T
 → 
⎝
⎜
⎜
⎜
⎛
​
  
1
1
1
1
​
  
2
2
2
2
​
  
3
3
3
3
​
  
4
4
4
4
​
  
⎠
⎟
⎟
⎟
⎞
​
 

Here is what transposition along the side diagonal looks like:

\begin{pmatrix} 1 & 1 & 1 & -1\\ 2 & 2 & 2 & -2\\ 3 & 3 & 3 & -3 \\ 4 & 4 & 4 & -4 \end{pmatrix}^T \to \begin{pmatrix} -4 & -3 & -2 & -1\\ 4 & 3 & 2 & 1\\ 4 & 3 & 2 & 1 \\ 4 & 3 & 2 & 1 \end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
1
2
3
4
​
  
1
2
3
4
​
  
1
2
3
4
​
  
−1
−2
−3
−4
​
  
⎠
⎟
⎟
⎟
⎞
​
  
T
 → 
⎝
⎜
⎜
⎜
⎛
​
  
−4
4
4
4
​
  
−3
3
3
3
​
  
−2
2
2
2
​
  
−1
1
1
1
​
  
⎠
⎟
⎟
⎟
⎞
​
 

The matrix below is transposed along the vertical line:

\begin{pmatrix} 1 & 2 & 3 & 4\\ 5 & 6 & 7 & 8\\ 9 & 10 & 11 & 12 \\ 13 & 14 & 15 & 16 \end{pmatrix}^T \to \begin{pmatrix} 4 & 3 & 2 & 1\\ 8 & 7 & 6 & 5\\ 12 & 11 & 10 & 9 \\ 16 & 15 & 14 & 13 \end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
1
5
9
13
​
  
2
6
10
14
​
  
3
7
11
15
​
  
4
8
12
16
​
  
⎠
⎟
⎟
⎟
⎞
​
  
T
 → 
⎝
⎜
⎜
⎜
⎛
​
  
4
8
12
16
​
  
3
7
11
15
​
  
2
6
10
14
​
  
1
5
9
13
​
  
⎠
⎟
⎟
⎟
⎞
​
 

Finally, here is transposition along the horizontal line:

\begin{pmatrix} 1 & 2 & 3 & 4\\ 5 & 6 & 7 & 8\\ 9 & 10 & 11 & 12 \\ 13 & 14 & 15 & 16 \end{pmatrix}^T \to \begin{pmatrix} 13 & 14 & 15 & 16\\ 9 & 10 & 11 & 12\\ 5 & 6 & 7 & 8 \\ 1 & 2 & 3 & 4 \end{pmatrix} 
⎝
⎜
⎜
⎜
⎛
​
  
1
5
9
13
​
  
2
6
10
14
​
  
3
7
11
15
​
  
4
8
12
16
​
  
⎠
⎟
⎟
⎟
⎞
​
  
T
 → 
⎝
⎜
⎜
⎜
⎛
​
  
13
9
5
1
​
  
14
10
6
2
​
  
15
11
7
3
​
  
16
12
8
4
​
  
⎠
⎟
⎟
⎟
⎞
​
 

Objectives
In this stage, you should add an option to transpose matrices. If the user chooses this option, your program should provide them with 4 types of transposition and ask them to choose one. Then it should read the matrix, transpose it, and output the result. Refer to the example to see the exact format.

Note that your program should still be able to do all operations on matrices that you've implemented in the previous stage.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: > 4

1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: > 1
Enter matrix size: > 3 3
Enter matrix:
> 1 7 7
> 6 6 4
> 4 2 1
The result is:
1 6 4
7 6 2
7 4 1

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
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


# transpose a matrix along the main diagonal
def main_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    new_matrix = map(list, zip(*matrix))
    print('The result is:')
    print_matrix(new_matrix)


# transpose a matrix along the side diagonal
def side_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    for row in matrix:
        row = row.reverse()
    matrix = matrix[::-1]
    new_matrix = map(list, zip(*matrix))
    print('The result is:')
    print_matrix(new_matrix)


# transpose a matrix along the vertical axis
def vert_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    for row in matrix:
        row = row.reverse()
    print('The result is:')
    print_matrix(matrix)


# transpose a matrix along the horizontal axis
def hori_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    matrix = matrix[::-1]
    print('The result is:')
    print_matrix(matrix)


# print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(*row)


# main code
while True:
    print(r'''1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        4. Transpose matrix
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
    elif choice == 4:
        print(r'''1. Main diagonal
            2. Side diagonal
            3. Vertical line
            4. Horizontal line''')
        tr_choice = int(input('Your choice: '))
        if tr_choice == 1:
            main_trans()
        elif tr_choice == 2:
            side_trans()
        elif tr_choice == 3:
            vert_trans()
        elif tr_choice == 4:
            hori_trans()
            
            
\\

from numpy import matrix, rot90, fliplr, flipud


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
          '3. Multiply matrices', '4. Transpose matrix', '0. Exit', sep='\n')
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
    if choice == 4:
        print('1. Main diagonal', '2. Side diagonal',
              '3. Vertical line', '4. Horizontal line')
        choice_ = int(input('Your choice: '))
        first = Matrix('')
        first.matrix_reader()
        print('The result is:')
        result = Matrix('')
        if choice_ == 1:
            result.matrix = first.matrix.T
        if choice_ == 2:
            result.matrix = rot90(rot90(first.matrix).T, 3)
        if choice_ == 3:
            result.matrix = fliplr(first.matrix)
        if choice_ == 4:
            result.matrix = flipud(first.matrix)
        result.print_matrix()
\\

def display_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("0. Exit")
    menu_choice = input("Your choice:")
    return menu_choice


def t_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    t_choice = input("Your choice:")
    return t_choice


def add_matrices():
    n, m = map(int, input("Enter size of first matrix:").split())
    print("Enter first matrix:")
    first_list = [[float(c) for c in input().split()] for r in range(n)]
    a, b = map(int, input("Enter size of second matrix:").split())
    print("Enter second matrix:")
    second_list = [[float(c) for c in input().split()] for r in range(a)]
    if (n, m) == (a, b):
        print("The result is:")
        for r in range(n):
            for c in range(m):
                print(first_list[r][c] + second_list[r][c], end=" ")
            print()
    else:
        print("The operation cannot be performed.")
    print()


def mult_by_const():
    n, m = map(int, input("Enter size of matrix:").split())
    print("Enter matrix:")
    matrix = [[float(c) for c in input().split()] for r in range(n)]
    constant = float(input("Enter constant:"))
    print("The result is:")
    for r in range(n):
        for c in range(m):
            print(matrix[r][c] * constant, end=" ")
        print()
    print()


def mult_matrices():
    n, m = map(int, input("Enter size of first matrix:").split())
    print("Enter first matrix:")
    first_list = [[float(c) for c in input().split()] for r in range(n)]
    a, b = map(int, input("Enter size of second matrix:").split())
    print("Enter second matrix:")
    second_list = [[float(c) for c in input().split()] for r in range(a)]
    if m == a:
        result = [[0 for c in range(b)] for r in range(n)]
        # iterate through rows of first matrix
        for r in range(n):
            # iterate through columns of second matrix
            for c in range(b):
                # iterate through the rows of second matrix
                for s in range(a):
                    result[r][c] += first_list[r][s] * second_list[s][c]
        print("The result is:")
        for r in range(n):
            for c in range(b):
                print(result[r][c], end=" ")
            print()
        print()
    else:
        print("The operation cannot be performed.")
    print()


def get_t_matrix():
    n, m = map(int, input("Enter matrix size:").split())
    print("Enter matrix:")
    matrix = [[float(c) for c in input().split()] for r in range(n)]
    return matrix


def main_diagonal(matrix):
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return t_matrix


def vertical_line(matrix):
    for r in matrix:
        r.reverse()
    return matrix


def horizontal_line(matrix):
    t_matrix = []
    for row in matrix:
        t_matrix.insert(0, row)
    return t_matrix


def side_diagonal(matrix):
    t_matrix = vertical_line(matrix)
    t_matrix = horizontal_line(t_matrix)
    t_matrix = main_diagonal(t_matrix)
    return t_matrix


def print_result(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end=" ")
        print()
    print()


def transpose():
    t_choice = ()
    while t_choice not in ("1", "2", "3", "4"):
        t_choice = t_menu()
    t_matrix = get_t_matrix()
    if t_choice == "1":
        result = main_diagonal(t_matrix)
    if t_choice == "2":
        result = side_diagonal(t_matrix)
    if t_choice == "3":
        result = vertical_line(t_matrix)
    if t_choice == "4":
        result = horizontal_line(t_matrix)
    print_result(result)


choice = ()
while choice != "0":
    choice = ()
    while choice not in ("1", "2", "3", "4", "0"):
        choice = display_menu()
    if choice == "1":
        add_matrices()
    if choice == "2":
        mult_by_const()
    if choice == "3":
        mult_matrices()
    if choice == "4":
        transpose()











