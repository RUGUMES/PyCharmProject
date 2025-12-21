print("Меню:")
print("1. Кофе☕       — 120₽")
print("2. Чай 🍵      — 180₽")
print("3. Сок 🧃        — 200₽")
print("4. Вода 💧      — 150₽")
print("5. Лимонад 🥤 — 220₽\n")

Coffe = 120
Tea = 180
Juice = 200
Water = 150
Lemonade = 220

drink = input("Введите номер или название напитка: ").strip().lower()

match drink:
    case "1" | "Кофе☕":
        name, price = "Кофе☕", Coffe
    case "2" | "Чай 🍵":
        name, price = "Чай 🍵", Tea
    case "3" | "Сок 🧃":
        name, price = "Сок 🧃", Juice
    case "4" | "Вода 💧":
        name, price = "Вода 💧", Water
    case "5" | "Лимонад 🥤":
        name, price = "Лимонад 🥤", Lemonade
    case _:
        print("\n❗️ Ошибка: напиток не найден. Перезапустите программу и попробуйте снова.")

portions = int(input("Введите кол-во порций: "))
def portions_word(n):
    if n % 10 == 1 and n % 100 != 11:
        return "Порция"
    elif 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return "Порции"
    else:
        return "Порций"

total = price * portions
discount_code = input("Введите код скидки (FREEDRINK/STUDENT): ").strip().upper()
discount = 0

match discount_code:
    case "FREEDRINK":
        discount = 0.30
    case "STUDENT":
        discount = 0.20
    case _:
        discount = 0

final_price = total * (1 - discount)
print("\n" + "═" * 44)
print("               🧾 ЧЕК КАФЕ")
print("═" * 44)
print(f"Напиток:           {name}")
print(f"Цена за порцию:    {price}₽")
print(f"Количество:        {portions} {portions_word(portions)}")
print(f"Сумма:             {total}₽")

if discount > 0:
    print(f"Скидка:            {int(discount * 100)}%")
    print(f"ИТОГО К ОПЛАТЕ:    {final_price:.2f}₽")
else:
    print("Скидка:            нет")
    print(f"Итого к оплате:    {final_price:.2f}₽")

print("═" * 47)
print("Спасибо за заказ! (❁´◡`❁) Возвращайтесь снова!")
print("═" * 47)