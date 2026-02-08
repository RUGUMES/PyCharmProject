n = int(input('Введите с начало кол-во чисел,а потом сами числа: '))

max1 = -1
max2 = -1

for _ in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)