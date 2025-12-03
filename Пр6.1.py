# Задание 1
print("Диагностика Вашего здоровья")


temperature = float(input("Введите показатель Вашей температуры (°C): "))
pressure = int(input("Введите показатели Вашего давления (верхнее): "))
pulse = int(input("Введите показатели Вашего пульса (уд/мин): "))

if (36 <= temperature <= 37) and (110 <= pressure <= 130) and (60 <= pulse <= 100):
     print('Нормальное состояние')
elif ((35 <= temperature < 36) or (37 <= temperature <= 38)) and ((105 <= pressure < 110) or (130 < pressure <= 140)) and ((55 <= pulse < 60) or (100 <= pulse <= 110)):
     print("Легкое недомогание")
else:
     print("Требуется врач")








