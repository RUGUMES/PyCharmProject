#Список нечётных чисел
num = int(input('Введите число: '))

odd_num = list(range(1, num + 1, 2))

print(odd_num)

#Анализ цен
print('Анализ цен')

prices = [1500, 500, 2000, 3500, 1000, 4500]

print('Цены:', *prices)

print(f'Самый дорогой товар: {max(prices)}')
print(f'Самый дешевый товар: {min(prices)}')
print(f'Общую стоимость всех товаров: {sum(prices)}')
print(f'Средняя цена товара: {sum(prices) // len(prices)}')

#Изменение списка
users = ['Admin', 'Guest', 'User', 'Bot']

users[2] = 'Moderator'
users[3] = 'SuperAdmin'
users.append('Newbie')
print(*users, sep = ', ')

#Ручной подсчёт
marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
count_5 = 0
count_2 = 0

for score in marks:
    if score == 5:
        count_5 += 1
    elif score == 2:
        count_2 += 1

print('Все оценки:', *marks, sep = ', ')
print(f'Количество пятерок: {count_5}')
print(f'Количество двоек: {count_2}')

#Магия срезов
print('Магия срезов')
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first = data[:3]
last = data[7:10]
reserved = data[::-3]
odd = data[1::2]
print(*data, sep = ', ')
print()
print('Первая тройка чисел:', *first)
print('Последняя тройка чисел:', *last)
print('Список в обратном порядке:', *reserved)
print('Числа с нечетными индексами:', *odd)

#Палиндром
word = input('Введите слово: ')
word_list = list(word)
reserved_word = word_list[::-1]
if word_list == reserved_word:
    print(f'{word} является палиндромом')
else:
    print(f'{word} не является палиндромом')


#Ручной поиск индекса
numbers = [10, 20, 30, 40, 50]
num = int(input('Введите число: '))
found = False
for i in range(len(numbers)):
    if numbers[i] == num:
        print(f'{numbers[i]} имеется')
        found = True
        break
if not found:
    print('Нет такого числа')

import random
#Обмен значений
A = [random.randint(1, 100) for i in range(5)]
print('Список чисел: ', *A)

min_A = A.index(min(A))

A[0], A[min_A] = A[min_A], A[0]

print('Измененная версия списка: ', *A)