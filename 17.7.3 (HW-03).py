per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
while True:
    number = input("Пожалуйста введите сумму вклада: ")
    try:
        dep = int(number)
        if dep < 0:
            print("Сумма вклада не может быть отрицательной")
            continue
        break
    except ValueError:
        print("Сумма вклада должна быть целым числом")
print("Сумма вклада:", dep)
c = list(per_cent.values())
b = [round((x*dep/100),4)for x in c]
print("Годовой процент:", b)
maxx = max(b)
print("Самый выгодный годовой процент", maxx)