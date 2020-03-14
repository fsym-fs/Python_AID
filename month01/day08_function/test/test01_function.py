"""
test01_function
"""


def square_traspose(list_square):
    """

    :param list_square: list型--->一个待转置的方阵
    :return:返回一个转置后的方阵
    """
    for line in range(len(list_square) - 1):
        for column in range(line + 1, len(list_square)):
            list_square[line][column], list_square[column][line] = list_square[column][line], list_square[line][column]


list01 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square_traspose(list01)
print(list01)


def matrix_transpose(list_matrix):
    """
    转置矩阵
    :param list_matrix  list型:一个待转置的矩阵
    :return: 转置后的矩阵
    """
    list03 = []
    for i in range(len(list_matrix[1])):
        list04 = []
        for j in range(len(list_matrix)):
            list04.append(list_matrix[j][i])
        list03.append(list04)
    return list03


list02 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix_transpose(list02))
