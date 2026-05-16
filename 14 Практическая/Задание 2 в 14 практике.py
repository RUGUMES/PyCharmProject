import random

nested_list = [[random.randint(0, 20) for _ in range(5)] for _ in range(5)]

print("Исходный список:")
for row in nested_list:
    print(row)

sums_of_rows = []
total_sum = 0
max_sum = -1
max_sum_row_index = 0

for i in range(len(nested_list)):
    row_sum = sum(nested_list[i])
    sums_of_rows.append(row_sum)
    total_sum += row_sum

    if row_sum > max_sum:
        max_sum = row_sum
        max_sum_row_index = i

print(f"\nСумма элементов каждого подсписка (строки): {sums_of_rows}")
print(f"Общая сумма всех элементов: {total_sum}")
print(f"Строка с максимальной суммой (индекс {max_sum_row_index}): {nested_list[max_sum_row_index]}, сумма = {max_sum}")