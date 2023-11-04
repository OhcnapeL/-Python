money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитаем количество  месяцев, которое можно протянуть без долгов

month = 1
money_capital = money_capital + salary - spend  # Подушка безопасности по истечению первого месяца
while True:
    money_capital = money_capital + salary - spend * (1 + increase)  # Подушка безопасности в каждый последующий месяц
    spend *= (1 + increase)  # Траты за последующий месяц
    month += 1
    if money_capital < 0:  # Цикл завершится когда расходы превзойдут размер подушки, поэтому последний месяц исключаем
        break
print("Количество месяцев, которое можно протянуть без долгов:", month - 1)  # Исключаем последнюю итерацию

# TODO Посчитаем другим способом через условие разницы между тратами и остатком 1 вариант

money_capital_1 = 20000
salary_1 = 5000
spend_1 = 6000
increase_1 = 0.05

month_1 = 0

while True:
    money_capital_1 = money_capital_1 + salary_1 - spend_1
    spend_1 *= (1 + increase_1)
    month_1 += 1
    if money_capital_1 + salary_1 - spend_1 < 0:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month_1)

# TODO Посчитаем другим способом через условие разницы между тратами и остатком 2 вариант

money_capital_2 = 20000
salary_2 = 5000
spend_2 = 6000
increase_2 = 0.05

month_2 = 0

while True:
    delta = spend_2 - salary_2  # Чистые траты в месяц
    if delta > money_capital_2:  # Когда чистые траты превзойдут остаток подушки прекратить цикл
        break
    money_capital_2 -= delta  # Остаток подушки
    month_2 += 1
    spend_2 *= (1 + increase_2)  # Траты с учётом роста цен

print("Количество месяцев, которое можно протянуть без долгов:", month_2)
