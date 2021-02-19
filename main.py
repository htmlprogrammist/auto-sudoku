import eel

eel.init("")
eel.start("index.html", size=(1020, 800))


def check_horizontal():
    # pass
    return 1


def check_vertical():
    # pass
    return 2


def check_square():
    # pass
    return 3


@eel.expose()
def main():
    # pass
    check_horizontal()
    check_vertical()
    check_square()
