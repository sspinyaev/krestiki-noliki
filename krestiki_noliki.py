def greetings():
    print()
    print("----------------------------------------")
    print("Приветствую Вас в игре 'Крестики-Нолики'")
    print("----------------------------------------")
    print("формат ввода: x y")
    print("x - номер строки")
    print("y - номер столбца")

def game():
    print()
    print("    | 0 | 1 | 2 |")
    print("-----------------")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def turn():
    while True:
        cordinates = input("          Ваш ход:").split()
        if len(cordinates) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = cordinates
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
def win():
    win_cordinates = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cordinates in win_cordinates:
        symbols = []
        for c in cordinates:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
        return False

greetings()
field = [[" "] * 3 for i in range(3)]
move = 0
while True:
    move += 1
    game()
    if move % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = turn()

    if move % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if move == 9:
        print(" Ничья!")
        break
