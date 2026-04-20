from itertools import count

print('Лабиринт')

print(f'Символы в лабиринте:\n 0 — проход (можно идти)\n 1 — стена (нельзя пройти) \n л — ловушка (-10 HP) \n м — монета (+1 монета) \n ф — выход (нужно дойти до него и не погибнуть) \n з — враг (-50 HP) \n н — начальная точка (вход) ')

#1.1
maze_symbols = input('Введите 25 символов: ')

print(maze_symbols[5:10])
print(maze_symbols[10:15])
print(maze_symbols[15:20])
print(maze_symbols[20:25])

#1.2
maze_start = maze_symbols.find('н')
row1 = maze_start//5
column1 = maze_start%5
print(f'Местоположение входа в лабиринт: {row1, column1}')

#1.3
maze_finish = maze_symbols.find('ф')
row = maze_finish//5
column = maze_finish%5
print(f'Местоположение выхода из лабиринта: {row, column}')

#1.4
maze_distance = abs(row1 - row)+abs(column1 - column)
print(f'Дистанция лабиринта: {maze_distance}')

#1.5
count = 0
for i in maze_symbols:
        if 'м' in i:
            count += 1
print(f'{"🟡"*count}')

#1.6
start_player_hp = 100
player_hp = 0
count_trap = 0
count_enemy = 0
for i in maze_symbols:
    if "л" in i:
        count_trap += 10
    if "з" in i:
        count_enemy += 50
    player_hp = start_player_hp - count_trap - count_enemy
    if player_hp <= 0:
        print('Смерть')

    number_of_hearts = player_hp//10
    number_of_empty_hearts = 10 - player_hp//10
    print(f'Здоровье игрока: {'♥'*number_of_empty_hearts}{'♡'*number_of_hearts}')

#1.7
emoji_replace = {
    '0': '⬜',   # проход - белый квадрат
    '1': '⬛',   # стена - черный квадрат
    'л': '🔷',   # ловушка - синий ромб
    'м': '🟡',   # монета - желтый круг
    'ф': '🟫',   # выход - коричневый квадрат
    'з': '🐷',   # враг - свинья
    'н': '⭐'    # начало - звезда
}

for i in range(0, 25, 5):
    row = maze_symbols[i:i+5]
    emoji_row = ''.join(emoji_replace.get(ch, ch) for ch in row)
    print(emoji_row)

