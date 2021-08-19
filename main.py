def get_deposit(percent):
    return money * percent / 100


per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада = "))
deposit = list(map(get_deposit, per_cent.values()))

print("Максимальная сумма, которую вы можете заработать —", round(max(deposit), 2))
