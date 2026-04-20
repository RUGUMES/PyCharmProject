import random

nested_list = [[random.randint(1, 10) for _ in range(5)] for _ in range(3)]

print("Исходный вложенный список:")
for row in nested_list:
    print(row)

search_value = random.randint(1, 10)
print(f"\nИщем элемент: {search_value}")

positions = []

for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        if nested_list[i][j] == search_value:
            positions.append((i, j))

if positions:
    print(f"Элемент {search_value} найден на позициях:")
    for pos in positions:
        print(f"  строка {pos[0]}, индекс в строке {pos[1]}")
else:
    print(f"Элемент {search_value} не найден в списке.")