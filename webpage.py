import eel
import main

eel.init("")
eel.start("index.html", size=(1020, 800))


@eel.expose()
def call_main(matrix):
    main.main(matrix)
