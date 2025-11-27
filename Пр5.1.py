#калькулятор_налого
tax_rate = 0.13

annual_income=float(input("Ввести годовой доход:"))

# подсчёт
amount_of_tax=annual_income*tax_rate
income_with_tax=annual_income-amount_of_tax

# вывод информации пользователю
print("Общая сумма дохода:", annual_income)
print("Сумма налога:", amount_of_tax)
print("Сумма дохода после вычета налога", income_with_tax)