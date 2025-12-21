print('Калькулятор ИМТ')

weight, height = map(float, input('Введите вес в килограммах и рост в метрах:').split())

IMT= weight/(height*height)

print(f'ИМТ: {IMT}')