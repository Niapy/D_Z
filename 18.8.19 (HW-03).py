while True:
    number = input("Введите количество необходимых билетов: ")
    try:
        amount_of_tickets = int(number)
        if amount_of_tickets < 0:
            print("Количество может быть отрицательным")
            continue
        break
    except ValueError:
        print("Количество билетов должно быть целым числом")
print("Количество билетов:", amount_of_tickets)
s = 0
cost = (0, 990, 1390)
list_of_age = list(map(int, input("\nВозраст посетителей : ").strip().split()))[:amount_of_tickets]
for x in list_of_age:
    if x < 18:
        s = s + cost[0]
    elif 18 < x < 25:
        s = s + cost[1]
    elif x > 25:
        s = s + cost[2]
if amount_of_tickets > 3:
    s = s-(s*0.1)
print("Стоимость билетов составляет: ", s)