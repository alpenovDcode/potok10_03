
month = int(input("Введите номер месяца: "))


if month < 1 or month > 12:
    print("Неверный номер месяца")
else:

    if 3 <= month <= 5:
        print("Весна")
    elif 6 <= month <= 8:
        print("Лето")
    elif 9 <= month <= 11:
        print("Осень")
    else:
        print("Зима")
