count = 0
for i in range(10):
 i = int(input('Введите число: '))
 if i % 2 != 0:
    count+= 1
if count == 0:
    print('Yes')
else:
    print('No')