# Создание карты
maps = [[" "] * 3 for i in range(3)]
def position():
    print()
    print('   | 0 | 1 | 2 | ')
    print(' --------------- ')
    for i, row in enumerate(maps):
        row_str = f' {i} | {' | '.join(row)} | '
        print(row_str)
        print(' --------------- ')
    print()
# Проверка координат
def step():
    while True:
        coord = input('    Ваш ход: ').split()
        if len(coord) != 2: # Проверка на кол-во координат
            print('Введите две координаты!')
            continue
        x, y = coord
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2: # проверка координат
            print('Мимо, введите координаты в диапозоне от 0 до 2!')
            continue
        if maps[x][y] != " ": # Проверка на занятость клетки
            print("Мы не в морской бой играем, клетка занята!")
            continue
        return x,y
# проверка на победу
def _check():
    # победные комбинации
    win = (((0,0), (0,1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), # строки
         ((0, 0), (1, 0), (2, 0)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), # столбцы
         ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))                           # диагональ
    for cord in win:
        symbol = []
        for c in cord:
            symbol.append(maps[c[0]][c[1]])
        if symbol == ['X', 'X', 'X']:
            print("Победа первого игрока")
            return True
        if symbol == ['0', '0', '0']:
            print("Победа второго игрока")
            return True
        return False
count = 0
while True:
    count += 1
    position()
    if count % 2 == 1:
        print("Ходит первый игрок (X)")
    else:
        print("Ходит второй игрок (0)")  
# запись на карту
    x, y = step()
    if count % 2 == 1:
        maps[x][y] = "X"
    else:
        maps[x][y] = "0"
    if _check():
        break
    if count == 9:
        print('Ничья')
        break