'''
Description
In this stage, you should write a program that calculates a determinant of a matrix. You can check out some videos about linear algebra to understand the essence of the determinant and why it is important. To see how to calculate the determinant of any square matrix, watch a video about minors and cofactors and computing the nxn determinant. Also, here's nice graphic explanation on minors and cofactors.

A determinant is a single number that can be computed from the elements of a square matrix. There is a classical way to find the determinant of a matrix with an order <3<3.

A determinant of a 2-order matrix is equal to the difference between the product of elements on the main diagonal and the product of elements on the side diagonal:

\det\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = a_{11}\times a_{22} - a_{12}\times a_{21}det( 
a 
11
​
 
a 
21
​
 
​
  
a 
12
​
 
a 
22
​
 
​
 )=a 
11
​
 ×a 
22
​
 −a 
12
​
 ×a 
21
​
 

Now let's move on to the minor and the cofactor of a matrix.

Minor_{(i, j)}Minor 
(i,j)
​
  of a matrix is the determinant of the submatrix we get from the remaining elements after removing the i row and j column from this matrix.

Below is an example of Minor_{(2, 2)}Minor 
(2,2)
​
  for matrix A_{3 \times 3}A 
3×3
​
 :

M_{2,2}\begin{pmatrix} a_{1,1} & {\color{red}a_{1,2}}&a_{1,3} \\ {\color{red}a_{2,1}} & {\color{red}a_{2,2}} &{\color{red}a_{2,3}} \\ a_{3,1} & {\color{red}a_{3,2}} & a_{3,3} \end{pmatrix} =\det\begin{pmatrix} a_{1,1} & a_{1,3} \\ a_{3,1} & a_{3,3} \end{pmatrix}M 
2,2
​
  
⎝
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
 
​
  
⎠
⎞
​
 =det( 
a 
1,1
​
 
a 
3,1
​
 
​
  
a 
1,3
​
 
a 
3,3
​
 
​
 )

Cofactor_{(i, j)}Cofactor 
(i,j)
​
  of a matrix is the corresponding Minor_{(i, j)}Minor 
(i,j)
​
  multiplied by (-1)^{i+j}(−1) 
i+j
 . Notice that the cofactor is always preceded by a positive ++ or negative -− sign.

We often need to find the determinant of a matrix of the order greater than 22. In this case, we have to use expansion by rows or columns where the determinant is equal to a sum of a single row or a single column multiplied by the cofactors of the elements in the corresponding row or column. To do this, you should use a recursive method.

Below is an example of computing the determinant of a matrix of order 44 by first-row expansion, where cc stands for the CofactorCofactor :

\det\begin{pmatrix} a_{1,1} & a_{1,2} & a_{1,3} & a_{1,4} \\ a_{2,1} & a_{2,2} & a_{2,3} & a_{2,4} \\ a_{3,1} & a_{3,2} & a_{3,3} & a_{3,4} \\ a_{4,1} & a_{4,2} & a_{4,3} & a_{4,4} \end{pmatrix} = M_{1,1}\times c_{1,1} + M_{1,2}\times c_{1,2}+M_{1,3}\times c_{1,3} +M_{1,4}\times c_{1,4}det 
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
 =M 
1,1
​
 ×c 
1,1
​
 +M 
1,2
​
 ×c 
1,2
​
 +M 
1,3
​
 ×c 
1,3
​
 +M 
1,4
​
 ×c 
1,4
​
 

Objectives
In this stage, your program should support calculating the determinant of a matrix. Refer to the example to see how it should be implemented.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice: > 5
Enter matrix size: > 3 3
Enter matrix:
> 1 7 7
> 6 6 4
> 4 2 1
The result is:
-16

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice: > 5
Enter matrix size: > 5 5
Enter matrix:
> 1 2 3 4 5
> 4 5 6 4 3
> 0 0 0 1 5
> 1 3 9 8 7
> 5 8 4 7 11
The result is:
191

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
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


# calculate the determinant for a matrix
def calc_det(matrix, total=0):
    indices = list(range(len(matrix)))
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val
    for focus in indices:
        submatrix = [row[:] for row in matrix]
        submatrix = submatrix[1:]
        height = len(submatrix)
        for i in range(height):
            submatrix[i] = submatrix[i][0:focus] + submatrix[i][focus+1:]
        sign = (-1) ** (focus % 2)
        sub_det = calc_det(submatrix)
        total += sign * matrix[0][focus] * sub_det
    return total


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
        5. Calculate a determinant
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
    elif choice == 5:
            det_size = [int(a) for a in input('Enter size of matrix: ').split()]
            print('Enter matrix:')
            det_matrix = get_matrix(det_size)
            determ = calc_det(det_matrix)
            print('The result is:')
            print(str(determ))
            
\\

from numpy import matrix, rot90, fliplr, flipud, linalg


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
          '3. Multiply matrices', '4. Transpose matrix',
          '5. Calculate a determinant', '0. Exit', sep='\n')
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
    if choice == 5:
        first = Matrix('')
        first.matrix_reader()
        print('The result is:')
        print(linalg.det(first.matrix))

\\

from typing import List


class Matrix:
    def __init__(self, rows: int, columns: int, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix


class MatrixFunctions:
    ERROR = "The operation cannot be performed"

    def __init__(self, working_matrix: Matrix):
        self.working_matrix = working_matrix

    def add(self, operation_matrix: Matrix):
        is_same_rows: bool = self.working_matrix.rows == operation_matrix.rows
        is_same_columns: bool = self.working_matrix.columns == operation_matrix.columns

        if is_same_rows and is_same_columns:
            for i in range(self.working_matrix.rows):
                for x in range(self.working_matrix.columns):
                    self.working_matrix.matrix[i][x] += operation_matrix.matrix[i][x]
        else:
            self.error()

    def multiply_by_constant(self, constant):
        for i in range(self.working_matrix.rows):
            self.working_matrix.matrix[i] = map(lambda x: x * constant, self.working_matrix.matrix[i])

    def multiply_by_matrix(self, operation_matrix: Matrix):
        if self.working_matrix.columns == operation_matrix.rows:
            place_holder = [[] for _ in range(self.working_matrix.rows)]
            for i in range(self.working_matrix.rows):
                for x in range(operation_matrix.columns):
                    sum_ = 0
                    for y in range(self.working_matrix.columns):
                        sum_ += self.working_matrix.matrix[i][y] * operation_matrix.matrix[y][x]
                    place_holder[i].append(sum_)
            self.working_matrix.matrix = place_holder
        else:
            self.error()

    def transpose(self, operation_num):
        place_holder = []
        if operation_num == 1:
            for x in range(self.working_matrix.columns):
                place_holder.append([])
                for y in range(self.working_matrix.rows):
                    place_holder[x].append(self.working_matrix.matrix[y][x])
            self.working_matrix.matrix = place_holder
        elif operation_num == 2:
            for x in range(self.working_matrix.columns)[::-1]:
                place_holder.append([])
                for y in range(self.working_matrix.rows)[::-1]:
                    place_holder[self.working_matrix.columns - x - 1].append(self.working_matrix.matrix[y][x])
            self.working_matrix.matrix = place_holder
        elif operation_num == 3:
            for i in range(self.working_matrix.rows):
                self.working_matrix.matrix[i] = self.working_matrix.matrix[i][::-1]
        elif operation_num == 4:
            self.working_matrix.matrix = self.working_matrix.matrix[::-1]

    def calc_determinant(self, rec_mat=None):
        rec_mat = self.working_matrix.matrix if rec_mat is None else rec_mat
        rows = len(rec_mat[0])
        total, plus_or_minus = 0, 0
        if rows > 2:
            for i in range(rows):
                if plus_or_minus == 0:
                    total += rec_mat[0][i] * self.calc_determinant(list(map(lambda row: row[:i] + row[i + 1:], rec_mat[1:])))
                    plus_or_minus -= 1
                else:
                    total -= rec_mat[0][i] * self.calc_determinant(list(map(lambda row: row[:i] + row[i + 1:], rec_mat[1:])))
                    plus_or_minus += 1
            return total
        elif rows == 1:
            return rec_mat[0][0]
        else:
            return rec_mat[0][0] * rec_mat[1][1] - rec_mat[0][1] * rec_mat[1][0]

    def print_matrix(self):
        for row in self.working_matrix.matrix:
            print(' '.join(map(str, row)))

    def error(self):
        print(self.ERROR, "\n")
        run()


class GetInputs:
    def __init__(self, type_):
        self.values = []
        self.RESULT = "The result is:"
        self.type_ = type_
        if type_ == 1 or type_ == 3:
            self.n_of_matrices = 2
            self.MESSAGE = ["Enter size of first matrix: ", "Enter size of second matrix: "]
            self.MESSAGE2 = ["Enter first matrix:", "Enter second matrix:"]
        elif type_ == 2 or type_ == 5:
            self.n_of_matrices = 1
            self.MESSAGE = ["Enter size of matrix: "]
            self.MESSAGE2 = ["Enter matrix:"]
            self.MESSAGE3 = "Enter constant: "
        elif type_ == 4:
            self.n_of_matrices = 1
            self.MESSAGE = ["Enter size of matrix: "]
            self.MESSAGE2 = ["Enter matrix:"]
            self.MESSAGE3 = '\n'.join(["1. Main diagonal",
                                       "2. Side diagonal",
                                       "3. Vertical line",
                                       "4. Horizontal line",
                                       "Your choice: "])

    def get_input(self):
        if self.type_ == 4:
            self.values.append(int(input(self.MESSAGE3)))
        for i in range(self.n_of_matrices):
            rows, columns = map(int, input(self.MESSAGE[i]).split())
            print(self.MESSAGE2[i])
            matrix = [list(map(lambda x: float(x) if '.' in x else int(x), input().split())) for _ in range(rows)]
            self.values.append(Matrix(rows, columns, matrix))

        if self.type_ == 2:
            self.values.append((lambda x: float(x) if '.' in x else int(x))(input(self.MESSAGE3)))


def run():
    print("1. Add matrices\n"
          "2. Multiple matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrix\n"
          "5. Calculate a determinant\n"
          "0. Exit")
    input_ = int(input("Your choice: "))

    if input_ == 1:
        input_ = GetInputs(input_)
        input_.get_input()
        o = MatrixFunctions(input_.values[0])
        o.add(input_.values[1])
        print(input_.RESULT)
        o.print_matrix()
        run()
    elif input_ == 2:
        input_ = GetInputs(input_)
        input_.get_input()
        o = MatrixFunctions(input_.values[0])
        o.multiply_by_constant(input_.values[1])
        print(input_.RESULT)
        o.print_matrix()
        run()
    elif input_ == 3:
        input_ = GetInputs(input_)
        input_.get_input()
        o = MatrixFunctions(input_.values[0])
        o.multiply_by_matrix(input_.values[1])
        print(input_.RESULT)
        o.print_matrix()
        run()
    elif input_ == 4:
        input_ = GetInputs(input_)
        input_.get_input()
        o = MatrixFunctions(input_.values[1])
        o.transpose(input_.values[0])
        print(input_.RESULT)
        o.print_matrix()
        run()
    elif input_ == 5:
        input_ = GetInputs(input_)
        input_.get_input()
        o = MatrixFunctions(input_.values[0])
        print(input_.RESULT)
        print(o.calc_determinant())
    elif input_ == 0:
        quit()


if __name__ == '__main__':
    run()


