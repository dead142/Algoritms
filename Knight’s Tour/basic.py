# Author: Andrei V. Berezhkov
# date: 2018-11-05
# Essential Algorithms by Rod Stephens, p. 199

from pprint import pprint

""" Запрос количества строк и столюцов поля"""
NumRows = int(input("Введите колество строк"))
NumCols = int(input("Введите количество столбцов"))

# Размер поля. Более 6 на 6 вычислять будет очень долго
h = [[0 for j in range(NumRows)] for i in range(NumCols)]

def KnightTour(row, col, h, num_moves_taken, NumRows, NumCols):
    countSteps = NumRows * NumCols + 1;  # так как начинаем с 0
    h[row][col] = num_moves_taken
    num_moves_taken += 1
    if (num_moves_taken == countSteps):
        pprint(h)
        print("Все ходы сделаны")
        return False
    dRows = [-2, -2, -1, 1, 2, 2, 1, -1]
    dCols = [-1, 1, 2, 2, 1, -1, -2, -2]

    for i in range(7):
        r = row + dRows[i]
        c = col + dCols[i]
        # h[r][c] IndexError: list index out of range
        try:
            if ((r >= 0) and (r < NumRows) and (c >= 0) and (c < NumCols) and (h[r][c] == 0)):
                if (KnightTour(r, c, h, num_moves_taken, NumCols, NumRows)):
                    return True
        except IndexError:
            continue

    h[row][col] = 0
    return False


KnightTour(0, 0, h, 1, NumRows, NumCols)
