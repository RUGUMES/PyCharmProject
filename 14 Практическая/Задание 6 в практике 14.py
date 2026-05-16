prices = list(map(int, input("Цены предметов (через пробел): ").split()))

ascending = sorted(prices)

descending = sorted(prices, reverse=True)

original = prices.copy()

reversed_order = prices[::-1]

print(f"Сортировка по возрастанию: {ascending}")
print(f"Сортировка по убыванию: {descending}")
print(f"Оригинальный порядок (от старых к новым): {original}")
print(f"Обратный порядок (от новых к старым): {reversed_order}")