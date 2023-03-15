def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        inner = []
        for i in row:
            inner.append(i ** 2)
        new.append(inner)
    return new
#    new = [[i**2 for i in row] for row in matrix]
#    return new
