import random

secret_num = random.randint(1, 10)

for attempt in range(3):
    user_num = int(input())

    if user_num == secret_num:
        print("Вы угадали загаданное число")
        break
    else:
        if user_num < secret_num:
            print("Неверно. Загаданное число больше")
        else:
            print("Неверно. Загаданное число меньше")
else:
    print("Загаданное число:", secret_num)
