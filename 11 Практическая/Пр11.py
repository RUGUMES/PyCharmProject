#Задание 1

print('12 месяцев')

print("n k m")
for n in range(1, 13):
    for k in range(1, 13):
        for m in range(1, 13):
            if 28*n + 30*k + 31*m == 365 and n + k + m == 12:
                print(n, k, m)

#Задание 2

print("Быки, коровы и телята")

for bulls in range(0, 11):
    for cows in range(0, 21):
        for calves in range(0, 201):
            if 10*bulls + 5*cows + 0.5*calves == 100:
                print(bulls, cows, calves)


#Задание 3
powers = {i: i**5 for i in range(1, 151)}

print("Поиск a, b, c, d, e...")
found = False

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum_pow = powers[a] + powers[b] + powers[c] + powers[d]
                # Проверяем, является ли sum_pow пятой степенью какого-то числа <=150
                e = int(sum_pow ** (1/5) + 0.5)  # +0.5 для округления
                if e <= 150 and powers[e] == sum_pow:
                    print(f"Найдено: {a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5")
                    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")
                    print(f"a+b+c+d+e = {a+b+c+d+e}")
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break

#Задание 4

n = input('Введите число: ')

count_3 = 0
count_last_digit = 0
count_even = 0
sum_greater_than_five = 0
product_greater_than_seven = 1
count_0_and_5 = 0

last_digit = n[-1]

for digit in n:

    if digit == '3':
        count_3 += 1

    if digit == last_digit:
        count_last_digit += 1

    if int(digit) % 2 == 0:
        count_even += 1

    if int(digit) > 5:
        sum_greater_than_five += int(digit)

    if int(digit) > 7:
        product_greater_than_seven *= int(digit)

    if digit in ('0', '5'):
        count_0_and_5 += 1

print(f'Количество цифр 3 в нём {count_3}')
print(f'Сколько раз в нём встречается последняя цифра {count_last_digit}')
print(f'Количество чётных цифр {count_even}')
print(f'Сумму его цифр, больших пяти {sum_greater_than_five}')
print(f'Произведение цифр, больших семи {product_greater_than_seven}')
print(f'Сколько раз в нём встречаются цифры 0 и 5 {count_0_and_5}')

#Задание 5

import random

answers = {
    "positive": [
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо да",
        "Можешь быть уверен в этом"
    ],
    "hesitantly_positive": [
        "Мне кажется - да",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят - да",
        "Да"
    ],
    "neutral": [
        "Пока неясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять"
    ],
    "negative": [
        "Даже не думай",
        "Мой ответ - нет",
        "По моим данным - нет",
        "Перспективы не очень хорошие",
        "Весьма сомнительно"
    ]
}

all_answers = []
for category in answers.values():
    all_answers.extend(category)

print("Привет! Я магический шар 8. Я знаю ответ на любой твой вопрос.")
print("Чтобы выйти, введи 'выход' или 'exit'.")

while True:
    question = input("\nЗадай свой вопрос: ").strip()

    if question.lower() in ('выход', 'exit', 'quit', 'стоп'):
        print("До свидания! Возвращайся, если возникнут вопросы.")
        break

    if not question:
        print("Кажется, ты ничего не спросил. Попробуй ещё раз!")
        continue

    if not question.endswith('?'):
        print("Это был вопрос? Попробуй добавить вопросительный знак в конце.")
        continue

    # Генерируем случайный ответ
    answer = random.choice(all_answers)

    print("\nМагический шар думает...")
    import time

    time.sleep(random.uniform(0.5, 2.0))

    print(f"\n📢 Ответ: {answer}\n")

    again = input("Хочешь задать еще один вопрос? (да/нет): ").strip().lower()
    if again not in ('да', 'yes', 'y', 'д', 'lf'):
        print("До свидания! Буду ждать твоих вопросов.")
        break