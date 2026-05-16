
max_number = -1

while True:
    number = int(input("Введите натуральное число (0 для остановки): "))

    if number == 0:
        break

    if number > max_number:
        max_number = number

if max_number != -1:
    print(f"Самое большое число: {max_number}")
else:
    print("Вы не ввели ни одного натурального числа.")