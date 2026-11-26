month_number = int(input("Введите номер месяца (от 1 до 12): "))

#Основные вычисления
match month_number:
    case 12 | 1 | 2:
        season_name = "Зима"
        month_emoji = "🥶"
    case 3 | 4 | 5:
        season_name = "Весна"
        month_emoji = "😊"
    case 6 | 7 | 8:
        season_name = "Лето"
        month_emoji = "😎"
    case 9 | 10 | 11:
        season_name = "Осень"
        month_emoji = "🤧"
    case _:
        season_name = "ошибка"
        month_emoji = "💀"

#Вывод
if season_name:
    print(f"Месяц под номером {month_number} это {season_name} {month_emoji}")
else:
    print("Ошибка: введен некоректный месяц. Пожалуйста введите число от 1 до 12.")