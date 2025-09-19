def checkmatrix(matrix):
    for i in matrix:
        if len(i) != len(matrix[0]): return True

def transpose(orig):
    if orig == []: return []
    if checkmatrix(orig): return ValueError
    return [[orig[j][i] for j in range(len(orig))] for i in range(len(orig[0]))]

def row_sums(orig):
    if checkmatrix(orig): return ValueError
    return [sum(i) for i in orig]

def col_sums(orig):
    return [sum(i) for i in transpose(orig)]