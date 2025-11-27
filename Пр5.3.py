# конвертер валюты
def convert_usd_to_rub(amount_usd):
  """
  Конвертация долларов в рубли

  Args:
     amount_usd (float): Сумма долларов

  Returns:
     float: Сумма в рублях
  """

# курс доллара
  usd_to_rub = 95.50
  return amount_usd * usd_to_rub

try:
    amount_dollar = float(input("Сумма долларов:"))
    amount_ruble = convert_usd_to_rub(amount_dollar)
    print("Сумма в рублях", amount_ruble)
except ValueError:
    print("")