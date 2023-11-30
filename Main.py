import numpy as np

ROW = 35
COL = 35


def print_matrix(matrix_for_printing):
    for r in matrix_for_printing:
        print(*r, sep="  ")


def draw_line(mat, x0, y0, x1, y1, inplace=False):
    if not (0 <= x0 < mat.shape[0] and 0 <= x1 < mat.shape[0] and
            0 <= y0 < mat.shape[1] and 0 <= y1 < mat.shape[1]):
        raise ValueError('Invalid coordinates.')

    if not inplace:
        mat = mat.copy()

    if (x0, y0) == (x1, y1):
        mat[x0, y0] = 2
        return mat if not inplace else None

    # Swap axes if Y slope is smaller than X slope
    transpose = abs(x1 - x0) < abs(y1 - y0)
    if transpose:
        mat = mat.T
        x0, y0, x1, y1 = y0, x0, y1, x1
    # Swap line direction to go left-to-right if necessary
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    # Write line ends
    mat[x0, y0] = 2
    mat[x1, y1] = 2
    # Compute intermediate coordinates using line equation
    x = np.arange(x0 + 1, x1)
    y = np.round(((y1 - y0) / (x1 - x0)) * (x - x0) + y0).astype(x.dtype)
    # Write intermediate coordinates
    mat[x, y] = 1
    if not inplace:
        # return mat if not transpose else mat.T
        print_matrix(mat)


x, y = input("Първа точка(х y): ").split()
a, b = input("Втора точка(х y): ").split()

first_point_x = int(x)
first_point_y = int(y)
second_point_x = int(a)
second_point_y = int(b)

print(draw_line(np.zeros((ROW, COL), dtype=str), first_point_x, first_point_y, second_point_x, second_point_y))

