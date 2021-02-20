import eel
import spreadsheet

eel.init("")
# eel.start("index.html", size=(1020, 800))

# line1 = list(map(int, input().split()))
# line2 = list(map(int, input().split()))
# line3 = list(map(int, input().split()))
# line4 = list(map(int, input().split()))
# line5 = list(map(int, input().split()))
# line6 = list(map(int, input().split()))
# line7 = list(map(int, input().split()))
# line8 = list(map(int, input().split()))
# line9 = list(map(int, input().split()))
matrix = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split())),
          list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split())),
          list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]


def check_horizontal(index):
    global x, y
    return 1


def check_vertical(index):
    global x, y
    return 2


def check_square():
    global x, y
    return 3


def is_number_already_in(number, line):
    equality = False
    for i in line:
        if i == number:
            equality = True
    if equality:
        return True
    else:
        return False


@eel.expose()
def main(a):
    global x, y
    print('Первая горизонтальная линия =>', a[0])
    print(is_number_already_in(0, a[0]))
    for i in range(9):
        print('Первая вертикальная линия: ', a[0][i])
    print(a)


main(matrix)  # 1 2 3 4 5 6 7 8 9
"""
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8
"""