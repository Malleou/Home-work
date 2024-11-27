def get_matrix(n, m, value):

    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
value = int(input('Введите наполнение матрицы: '))

matrix = get_matrix(n, m, value)
print(matrix)