import random

nested_list = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]

print("Исходный вложенный список:")
for row in nested_list:
    print(row)

filtered_list = []
for i in range(len(nested_list)):
    positive_row = []
    for j in range(len(nested_list[i])):
        if nested_list[i][j] > 0:
            positive_row.append(nested_list[i][j])

    if positive_row:
        filtered_list.append(positive_row)

print("\nОтфильтрованный список (только положительные элементы):")
for row in filtered_list:
    print(row)