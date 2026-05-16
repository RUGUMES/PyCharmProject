print('Строго возрастающая последовательность')

while True:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    if number1 >= number2:
        print('Ошибка. Второе число меньше или равно первому.')
        continue
    else:
        while True:
            number3 = int(input('Введите третье число: '))
            if number2 >= number3:
                print('Ошибка. Третье число меньше или равно второму.')
                continue
            else:
                break
    break
print('Последовательность принята.')