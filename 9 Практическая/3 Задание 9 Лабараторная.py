print('Ведьмаку заплатите чеканной монетой')

price = int(input("Введите стоимость услуги ведьмака: "))

coins = [25, 10, 5, 1]

total_coins = 0
coin_index = 0

remaining = price

print(f"Оплата суммы {price} монетами:")

while remaining > 0:

    current_coin = coins[coin_index]

    if remaining >= current_coin:

        coin_count = remaining // current_coin

        total_coins += coin_count

        remaining %= current_coin
        print(f"  Монет номиналом {current_coin}: {coin_count}")

    coin_index += 1

print(f"Минимальное количество монет: {total_coins}")