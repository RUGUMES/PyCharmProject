print("Ход ферзя")
row1 = int(input("Введите номер строки первой клетки (1-8): "))
column1 = int(input("Введите номер столбца первой клетки (1-8): "))
row2 = int(input("Введите номер строки второй клетки (1-8): "))
column2 = int(input("Введите номер столбца второй клетки (1-8): "))

if (row1==row2 or column1==column2) or (abs(row1 - row2) == abs(column1 - column2)):
    print("YES")
else:
    print("NO")