#Задача 1
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))

print(numbers[-1])

print(numbers[::-1])

has_5_and_17 = (5 in numbers) and (17 in numbers)
print("YES" if has_5_and_17 else "NO")

print(numbers[1:-1])

#Задача 2
n = int(input("Введите количество строк: "))
all_chars = []
for _ in range(n):
    line = input()

    all_chars.extend(line)

print(all_chars)

#Задача 3
path = input("Введите путь к файлу: ")

parts = path.split('\\')
for part in parts:
    print(part)

#Задача 4
ip_str = input("Введите IP-адрес: ")
octets = ip_str.split('.')
is_valid = True

if len(octets) != 4:
    is_valid = False
else:
    for octet in octets:

        if not octet.isdigit():
            is_valid = False
            break
        num = int(octet)
        if num < 0 or num > 255:
            is_valid = False
            break

print("Да" if is_valid else "Нет")

#Задача 5
numbers_str = input("Введите целые числа через пробел: ")
num_list = [int(x) for x in numbers_str.split()]

pair_count = 0

temp_list = num_list.copy()

for i in range(len(temp_list)):
    for j in range(i + 1, len(temp_list)):
        if temp_list[i] == temp_list[j]:
            pair_count += 1

print(pair_count)

#Задача 6
numbers = [8, 9, 10, 11]

numbers[1] = 17

numbers.extend([4, 5, 6])

del numbers[0]

numbers.extend(numbers.copy())

numbers.insert(3, 25)

print(numbers)