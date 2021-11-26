'''Description
In this stage, you should find the inverse of a matrix.

The inverse matrix A^{−1}A 
−1
  is the matrix whose product with the original matrix AA is equal to the identity matrix.

A \times A^{-1} = A^{-1} \times A = IA×A 
−1
 =A 
−1
 ×A=I

Watch a video about the inverse of a matrix to get the basic idea. To get a deeper understanding, check out the 3Blue1Brown channel.

The identity matrix is a matrix where all elements of the main diagonal are ones, and other elements are zeros. Here is an example of a 4, 44,4 identity matrix:

I_{4,4} = \begin{pmatrix} 1 & 0 & 0 &0\\ 0 & 1 & 0 &0 \\ 0 & 0 & 1&0 \\0 & 0 & 0 &1\end{pmatrix}I 
4,4
​
 = 
⎝
⎜
⎜
⎜
⎛
​
  
1
0
0
0
​
  
0
1
0
0
​
  
0
0
1
0
​
  
0
0
0
1
​
  
⎠
⎟
⎟
⎟
⎞
​
 

The inverse of a matrix can be found using this formula:

A^{-1} = \dfrac{1}{det(A)} \times C^TA 
−1
 = 
det(A)
1
​
 ×C 
T
 

As you can see, it contains a lot of operations you implemented in the previous stages: finding cofactors of all the elements of the matrix, transposition of the matrix, finding the determinant of a matrix, and multiplication of a matrix by a constant.

det(A)det(A) is the determinant of matrix AA, and C^TC 
T
  is the matrix consisting of cofactors of all elements of the matrix AA transposed along the main diagonal. The inverse matrix can’t be found if det(A)det(A) equals zero. You can look up a calculation example.

Objectives
In this stage, your program should support finding the inverse of a matrix. Refer to the example to see how it should be implemented.

Note that in some cases the inverse of a matrix does not exist. In such cases, your program should output a warning message.

Additional improvements
Although it's not required in this stage and we won't check, you can implement a method that prints a matrix in a readable way so that every column is correctly aligned and all elements are rounded to a fixed number of digits.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 6
Enter matrix size: > 3 3
Enter matrix:
> 2 -1 0
> 0 1 2
> 1 1 0
The result is:
 0.33   0  0.33
-0.33   0  0.66
 0.16 0.5 -0.33

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 6
Enter matrix size: > 2 2
Enter matrix:
> 2 1
> 4 2
This matrix doesn't have an inverse.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 0
 Report a typo
'''
def input_matrix(number = ''):
    mess = 'Enter matrix size: '
    mess1 = 'Enter matrix: '
    if number != '':
        mess = f'Enter size of {number} matrix: '
        mess1 = f'Enter {number} matrix: '
    x, y = [int(i) for i in input(mess).split()]
    print(mess1)
    matrix = list()
    for _ in range(x):
        matrix.append([float(i) for i in input().split()])
    return x, y, matrix


def print_menu():
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')


def print_transpose_menu():
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')


def print_result(matrix):
    print('The result is:')
    for line in matrix:
        print(line)
    print()


def print_error():
    print('The operation cannot be performed.')


def add():
    x1, y1, a = input_matrix('first')
    x2, y2, b = input_matrix('second')
    res = list()
    if x1 == x2 and y1 == y2:
        for i in range(0, x1):
            line = ''
            for j in range(0, x2):
                line += str(a[i][j] + b[i][j]) + ' '
            res.append(line)
        print_result(res)
    else:
        print_error()


def multiply_constant():
    x1, y1, a = input_matrix('first')
    c = float(input('Enter constant:'))
    res = list()
    for i in range(0, x1):
        line = ''
        for j in range(0, y1):
            line += str(a[i][j] * c) + ' '
        res.append(line)
    print_result(res)


def multiply():
    x1, y1, a = input_matrix('first')
    x2, y2, b = input_matrix('second')
    res = list()
    if x2 == y1:
        t = 0
        for i in range(0, x1):
            s = ''
            for j in range(0, y2):
                t = 0
                for k in range(0, y1):
                    t += a[i][k] * b[k][j]
                s += str(t) + ' '
            res.append(s)
        print_result(res)
    else:
        print_error()


def transpose_main(m, x, y):
    res = list()
    for i in range(0, x):
        line = ''
        for j in range(0, y):
            line += str(m[j][i]) + ' '
        res.append(line)
    print_result(res)


def transpose_side(m, x, y):
    res = list()
    for i in reversed(range(0, x)):
        line = ''
        for j in reversed(range(0, y)):
            line += str(m[j][i]) + ' '
        res.append(line)
    print_result(res)


def transpose_vertical(m, x, y):
    res = list()
    for i in range(0, x):
        line = ''
        for j in reversed(range(0, y)):
            line += str(m[i][j]) + ' '
        res.append(line)
    print_result(res)


def transpose_horizontal(m, x, y):
    res = list()
    for i in reversed(range(0, x)):
        line = ''
        for j in range(0, y):
            line += str(m[i][j]) + ' '
        res.append(line)
    print_result(res)


def transpose():
    print_transpose_menu()
    t = input('Your choice:')
    x, y, matrix = input_matrix()
    if t == '1':
        transpose_main(matrix, x, y)
    elif t == '2':
        transpose_side(matrix, x, y)
    elif t == '3':
        transpose_vertical(matrix, x, y)
    elif t == '4':
        transpose_horizontal(matrix, x, y)


def cofactor(i, j, x, matrix):
    new = list()
    for k in range(x):
        if k == i:
            continue
        line = list()
        for m in range(x):
            if m == j:
                continue
            line.append(matrix[k][m])
        new.append(line)
    return ((-1) ** (i + j)) * calc_determinant(x - 1, new)


def calc_determinant(x, matrix):
    if x == 1:
        return matrix[0][0]
    if x == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(x):
        det += matrix[0][i] * cofactor(0, i, x, matrix)
    return det


def determinant():
    x, y, matrix = input_matrix()
    print('The result is:')
    print(calc_determinant(x, matrix))


def inverse():
    x, y, matrix = input_matrix()
    det = calc_determinant(x, matrix)

    if x != y or det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        res = list()
        for i in range(x):
            line = ''
            for j in range(x):
                line += str(cofactor(j, i, x, matrix) / det) + ' '
            res.append(line)
        print_result(res)


while True:
    print_menu()
    s = input('Your choice:')
    if s == '0':
        break
    elif s == '1':
        add()
    elif s == '2':
        multiply_constant()
    elif s == '3':
        multiply()
    elif s == '4':
        transpose()
    elif s == '5':
        determinant()
    elif s == '6':
        inverse()
        

\\
import copy


def show_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")


def axis_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")


def get_choice(choices: set) -> int:
    while True:
        choice = input("Your choice: ")
        if choice in choices:
            return int(choice)


def print_matrix(matrix):
    if isinstance(matrix, str):
        print(matrix)
    print("The result is:")
    if isinstance(matrix, (float, int)):
        print(matrix)
    elif isinstance(matrix, list):
        for row in matrix:
            print(*map(lambda x: str(round(x, 3)).rjust(6), row))
    print()


def get_matrices():
    rows_1, cols_1 = [int(x) for x in input("Enter size of first matrix: ").split()]
    print("Enter first matrix:")
    first_matrix = [[float(x) for x in input().split()] for _ in range(rows_1)]
    rows_2, cols_2 = [int(x) for x in input("Enter size of second matrix: ").split()]
    print("Enter second matrix:")
    second_matrix = [[float(x) for x in input().split()] for _ in range(rows_2)]
    return first_matrix, second_matrix


def get_matrix():
    rows, columns = [int(x) for x in input("Enter size of matrix: ").split()]
    print("Enter matrix:")
    return [[float(x) for x in input().split()] for _ in range(rows)]


def add_matrices():
    first, second = get_matrices()
    if len(first) == len(second) and len(first[0]) == len(second[0]):
        return [[f + s for f, s in zip(F, S)] for F, S in zip(first, second)]
    return "The operation cannot be performed."


def scalar_multiplication():
    matrix = get_matrix()
    scalar = float(input("Enter constant: "))
    return scale(matrix, scalar)


def scale(matrix, scalar):
    return [[scalar * x if x else 0 for x in row] for row in matrix]


def matrix_multiplication():
    first, second = get_matrices()
    if len(first[0]) == len(second):
        sec = transpose(second)
        return [[sum(f * s for f, s in zip(row, col)) for col in sec] for row in first]
    return "The operation cannot be performed."


def transpose(matrix, axis=1):
    if axis == 1:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    elif axis == 2:
        return [[matrix[-i-1][-j-1] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    elif axis == 3:
        return [row[::-1] for row in matrix]
    elif axis == 4:
        return [row for row in matrix[::-1]]


def matrix_transposition():
    axis_menu()
    axis_choice = get_choice(set('1234'))
    matrix = get_matrix()
    return transpose(matrix, axis_choice)


def determinant_calculation():
    matrix = get_matrix()
    if len(matrix) == len(matrix[0]):
        return determinant(matrix)
    return "Non square matrix does not have a determinant"


def minor(matrix, i, j):
    minor_matrix = copy.deepcopy(matrix)
    for row in minor_matrix:
        row.pop(j)
    minor_matrix.pop(i)
    return minor_matrix


def cofactor(matrix, i, j):
    return pow(-1, i + j) * determinant(minor(matrix, i, j))


def cofactor_matrix(matrix):
    return [[cofactor(matrix, i, j) for j, _ in enumerate(row)] for i, row in enumerate(matrix)]


def determinant(matrix, i=0):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum(matrix[i][j] * cofactor(matrix, i, j) for j in range(n))


def matrix_inversion():
    matrix = get_matrix()
    return invert(matrix)


def adjugate(matrix):
    return transpose(cofactor_matrix(matrix))


def invert(matrix):
    try:
        return scale(adjugate(matrix), pow(determinant(matrix), -1))
    except ZeroDivisionError:
        return "This matrix doesn't have an inverse."


def main():
    while True:
        show_menu()
        users_choice = get_choice(set('0123456'))
        if users_choice == 0:
            break
        elif users_choice == 1:
            result = add_matrices()
        elif users_choice == 2:
            result = scalar_multiplication()
        elif users_choice == 3:
            result = matrix_multiplication()
        elif users_choice == 4:
            result = matrix_transposition()
        elif users_choice == 5:
            result = determinant_calculation()
        elif users_choice == 6:
            result = matrix_inversion()
        print_matrix(result)


if __name__ == "__main__":
    main()
\\

import numpy as np

import re


def matrix_builder(dim_message=None, matrix_message=None) -> dict(description="matrix", type=np.ndarray):
    dim = input(dim_message).strip()
    if not re.match(r"\A\d+\s*\d+$", dim):
        print("Invalid input!")
        return main()
    else:
        n_rows, n_cols = [int(x) for x in dim.split()]
        print(matrix_message)
        matrix = [[float(el) for el in input().split()]for _ in range(n_rows)]
        """ shape validation """
        for row in range(len(matrix)):
            try:
                message = f"Invalid row length, row {row + 1}"
                assert len(matrix[row]) == n_cols, message
            except AssertionError as err:
                print(err)
                return main()

        return np.array(matrix)


def matrix_printer(result):
    print("The result is:")
    for r in result:
        print(*r)


def add_matrices(m1: np.ndarray, m2: np.ndarray) -> dict(description="matrix", type=np.ndarray):
    if not all([m1.shape[0] == m2.shape[0],
                m1.shape[1] == m2.shape[1]]):
        print("ERROR")
        return main()
    return np.add(m1, m2)


def multiply_by_constant(matrix: np.ndarray, const) -> dict(description="matrix", type=np.ndarray):
    return matrix * const


def take_constant() -> int:
    try:
        cnstnt = int(input())
    except ValueError:
        print("provide constant for multiplying")
        return take_constant()
    return cnstnt


def multiply_matrices(m1: np.ndarray, m2: np.ndarray) -> dict(description="matrix", type=np.ndarray):
    try:
        result = np.matmul(m1, m2)  # https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
    except ValueError:
        print("ERROR")
        return main()
    return result


def main():
    """ main menu"""
    while True:
        option = input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multipl matrices\n4. Transpose matrix\n5. Calculate a determinant\nInverse matrix\n0. Exit\nYour choice: ")
        if option == "0":
            exit()

        elif option in {"1", "3"}:
            """ Add two matrices / Multiply two matrices"""
            matrix_a = matrix_builder("Enter size of first matrix: ", "Enter first matrix:")
            matrix_b = matrix_builder("Enter size of second matrix: ", "Enter second matrix:")
            result = add_matrices(matrix_a, matrix_b) if option == "1" else multiply_matrices(matrix_a, matrix_b)
            matrix_printer(result)

        elif option == "2":
            """ Multiply matrix by a constant """
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            constant = take_constant()
            result = multiply_by_constant(matrix_a, constant)
            matrix_printer(result)

        elif option == "4":
            """ Transpose matrix """
            transposition_type = input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: ")
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")

            transpositions = {"1": matrix_a.transpose(),  # standard main diagonal transposion
                              "2":  np.fliplr(np.rot90(matrix_a, 1)),  # side diagonal transposion is done throug one 90 degree counterclock-wise rotation and horizontal - line flip (simply row = row [::-1].
                              "3": np.flip(matrix_a, 1),  # reversing order of elements along the given axis
                              "4": np.flipud(matrix_a),  # vertical flip, replacing the sequence of rows moving the top ones to the bottom. Similar to stack operations
                              }  # can be stored as tuple to save some memory

            try:
                matrix_printer(transpositions[transposition_type])
            except KeyError:
                print("Invalid option chosen.")
                return main()

        elif option == "5":
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            result = np.linalg.det(matrix_a)
            print(result)

        elif option == "6":
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            det = np.linalg.det(matrix_a)
            if det == 0:
                print("This matrix doesn't have an inverse.")
            else:
                result = np.linalg.inv(matrix_a)
                matrix_printer(result)

        else:
            print("Invalid option chosen.")
            return main()


if __name__ == '__main__':
    main()
\\

def get_matrix(matrix_name=''):
    n, m = map(int, input(f'Enter size of{matrix_name} matrix:').split())
    print(f'Enter{matrix_name} matrix:')
    matrix = [list(map(int_float, input().split())) for _ in range(n)]
    return matrix


def int_float(n):
    try:
        return int(n)
    except ValueError:
        return float(n)


def output_matrix(matrix):
    for row in matrix:
        print(*row)


def add_matrix():
    matrix_1 = get_matrix(' first')
    matrix_2 = get_matrix(' second')
    if any([len(matrix_1) != len(matrix_2), len(matrix_1[0]) != len(matrix_2[0])]):
        print('The operation cannot be performed.')
    else:
        print('The result is:')
        result_matrix = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
        output_matrix(result_matrix)
        

def scalar_multiplication():
    matrix = get_matrix()
    scalar = float(input('Enter constant:'))
    result_matrix = [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    print('The result is:')
    output_matrix(result_matrix)

    
def matrix_multiplication():
    matrix_1 = get_matrix(' first')
    matrix_2 = get_matrix(' second')
    if len(matrix_1[0]) != len(matrix_2):
        print('The operation cannot be performed.')
    else:
        print('The result is:')
        result_matrix = [['?' for j_2 in range(len(matrix_2[0]))] for i_1 in range(len(matrix_1))]
        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[0])):
                result_matrix[i][j] = sum([matrix_1[i][k] * matrix_2[k][j] for k in range(len(matrix_1[0]))])
        output_matrix(result_matrix)    


def transpose_matrix():
    print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', sep='\n')
    transposition_type = input('Your choice:')
    matrix = get_matrix()
    if transposition_type in ('1', '2'):
        matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    if transposition_type in ('3', '2'):
        matrix = [matrix[i][::-1] for i in range(len(matrix))]
    if transposition_type in ('4', '2'):
        matrix = matrix[::-1]
    print('The result is:')
    output_matrix(matrix)

    
def get_determinant():
    matrix = get_matrix()
    if len(matrix) != len(matrix[0]):
        print('The operation cannot be performed.')
    else:
        print('The result is:')
        print(determinant(matrix))


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum([matrix[0][k] * (-1) ** k * determinant(minor_ij(matrix, 0, k)) for k in range(len(matrix))])


def minor_ij(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in matrix[:i] + matrix[i + 1:]]


def get_inverse_matrix():
    matrix = get_matrix()
    if len(matrix) != len(matrix[0]):
        print('The operation cannot be performed.')
    else:
        det_matrix = determinant(matrix)
        if det_matrix:
            print('The result is:')
            size = len(matrix)
            inv_matrix = [[(-1) ** (i + j) * determinant(minor_ij(matrix, i, j)) for j in range(size)] for i in range(size)]
            inv_matrix = [[1 / det_matrix * inv_matrix[j][i] for j in range(size)] for i in range(size)]
            output_matrix(inv_matrix)
        else:
            print("This matrix doesn't have an inverse.")


def main_menu():
    print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '4. Transpose matrix',
          '5. Calculate a determinant', '6. Inverse matrix', '0. Exit', sep='\n')    
    action = input('Your choice:')
    if action == '0':
        return False
    if action == '1':
        add_matrix()
    elif action == '2':
        scalar_multiplication()
    elif action == '3':
        matrix_multiplication()
    elif action == '4':
        transpose_matrix()
    elif action == '5':
        get_determinant()
    elif action == '6':
        get_inverse_matrix()
    return True


while main_menu():
    print()



