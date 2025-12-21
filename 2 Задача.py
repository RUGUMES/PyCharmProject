print("ростой калькуляттор")

first = float(input('Введите первое число: '))
seconde = float(input('Введите второе число: '))
simwol = input('Введите символ для арифметического действия (+, -, *, /): ')

match simwol:
    case '+':
        print(f'Сложение {first + seconde}')
    case '-':
        print(f'Вычитание {first - seconde}')
    case '*':
        print(f'Умножение {first * seconde}')
    case '/':
        print(f'Деление {first / seconde}')
    case _:
        print('Некорректный ввод данных')
