month_number = int(input("Введите номер месяца (от 1 до 12): "))

#Разделение на группы
thirty_days_months = (4, 6, 9, 11)
thirty_one_days_months = (1, 3, 5, 7, 8, 10, 12)

if month_number in thirty_days_months:
    print(30)
elif month_number in thirty_one_days_months:
    print(31)
elif month_number == 2:
    print(28)
else:
    print("Некорректный номер месяца")
