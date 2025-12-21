def atm_withdrawal(amount):
    denominations = [5000, 2000, 1000, 500, 200, 100]
    ostatok = amount

    print(f"Сумма: {amount} руб.")
    for denom in denominations:
        count = ostatok // denom
        if count > 0:
            print(f"{denom} руб: {count} шт.")
            ostatok -= count * denom

    if ostatok == 0:
        print("Выдача завершена.")
    else:
        print(f"Остаток: {ostatok} руб. (невозможно выдать)")


amount = int(input("Введите сумму: "))
atm_withdrawal(amount)