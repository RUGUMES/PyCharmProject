print('Кассовый аппарат.')

total_price = 0

while True:
    product_price = int(input('Введите цену товара:'))
    if product_price < 0:
        print('Ошибка')
        continue
    else:
        total_price += product_price
        if product_price == 0:
            break
if total_price > 1000:
 print(f'{total_price * 0.9}')
else:
 print(f'{total_price}')