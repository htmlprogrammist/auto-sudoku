import spreadsheet

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


def main(a):
    global x, y
    print('Первая горизонтальная линия =>', a[0])
    print(is_number_already_in(0, a[0]))
    for i in range(9):
        print('Первая вертикальная линия: ', a[0][i])
    print(a)
