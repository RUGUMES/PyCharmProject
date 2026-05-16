n = int(input("Сколько предметов может унести игрок? "))
items = list(map(int, input("Ценности предметов (через пробел): ").split()))

items.sort(reverse=True)

taken_items = items[:n]

max_value = sum(taken_items)

print(f"\nМаксимально возможная суммарная ценность: {max_value}")