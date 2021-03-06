"""

Instructions:

Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

Example:

array = [[1,2,3],
     [4,5,6],
     [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""


def snail(snail_map):
    result = list()
    if len(snail_map) == 0:
        return result

    row_begin = 0
    row_end = len(snail_map) - 1
    col_begin = 0
    col_end = len(snail_map[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            result.append(snail_map[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end + 1):
            result.append(snail_map[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                result.append(snail_map[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                result.append(snail_map[i][col_begin])
        col_begin += 1

    return result


def snail2(matrix):
    result = list
    while len(matrix):
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result
