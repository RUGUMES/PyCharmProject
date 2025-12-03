# Задание 2
print("Цвета колеса рулетки")

carman = int(input("Введите номер кармана: "))

if carman == 0:
    print("Цвет зелёный")
elif (1 <= carman <= 10) or (19 <= carman <= 28):
    if carman % 2 == 0:
        print("Цвет черный")
    else:
        print("Цвет красный")
elif (11 <= carman <= 18) or (29 <= carman <= 36):
    if carman % 2 == 0:
        print("Цвет красный")
    else:
        print("Цвет черный")
else:
    print("Ошибка ввода")