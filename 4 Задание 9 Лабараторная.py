print("Все вместе")

number = int(input("Введите натуральное число: "))

temp = number

count_3 = 0
count_last_digit = 0
count_even = 0
sum_greater_5 = 0
product_greater_7 = 1
count_7_plus = 0
count_0_5 = 0


last_digit = number % 10

print(f"\nАнализ цифр числа {number}:")
print("-" * 30)

while temp > 0:
    digit = temp % 10

    if digit == 3:
        count_3 += 1

    if digit == last_digit:
        count_last_digit += 1

    if digit % 2 == 0:
        count_even += 1

    if digit > 5:
        sum_greater_5 += digit

    if digit > 7:
        product_greater_7 *= digit
        count_7_plus += 1


    if digit == 0 or digit == 5:
        count_0_5 += 1


    temp //= 10


if count_7_plus == 0:
    product_greater_7 = 1
elif count_7_plus == 1:

    pass

print(f"Количество цифр - 3: {count_3}")
print(f"Количество вхождений последней цифры ({last_digit}): {count_last_digit}")
print(f"Количество четных цифр: {count_even}")
print(f"Сумма цифр, больше 5: {sum_greater_5}")
print(f"Произведение цифр, больше 7: {product_greater_7}")
print(f"Количество цифр 0 и 5 (суммарно): {count_0_5}")