import random

nested_list = [[random.randint(-20, 50) for _ in range(4)] for _ in range(4)]

print("Исходный вложенный список:")
for row in nested_list:
    print(row)

max_value = nested_list[0][0]
max_row = 0
max_col = 0

for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        if nested_list[i][j] > max_value:
            max_value = nested_list[i][j]
            max_row = i
            max_col = j

print(f"\nМаксимальный элемент: {max_value}")
print(f"Позиция: строка {max_row}, индекс в строке {max_col}")