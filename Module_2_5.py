def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('строки матрицы: '))
m = int(input('столбцы матрицы: '))
value = int(input('значение матрицы: '))

matrix = get_matrix(n, m, value)