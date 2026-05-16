print("Сколько ждать?")

# Флаг для отслеживания встречи с Александрой
found_alexandra = False
# Счетчик людей между Александрой и Левоном
people_between = 0

print("Введите имена участников (для завершения введите пустую строку):")

while True:
    name = input()


    if name == "":
        break

    if name == "Александра":
        found_alexandra = True

    elif name == "Левон" and found_alexandra:
        break
    elif found_alexandra:
        people_between += 1

print(people_between)