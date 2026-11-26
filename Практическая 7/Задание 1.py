product_rating = input("Введите рейтинг продукта (целое число от 1 до 10): ").strip()

# Определение оценки
match product_rating:
    case "9" | "10":
        description = "Отличный продукт!"
        rating_emoji = "🌟"
        recommendation = "Настоятельно рекомендую!"
    case "7" | "8":
        description = "Хороший продукт"
        rating_emoji = "👍"
        recommendation = "Рекомендую"
    case "4" | "5" | "6":
        description = "Средний продукт"
        rating_emoji = "😐"
        recommendation = "Можно попробовать"
    case "1" | "2" | "3":
        description = "Плохой продукт"
        rating_emoji = "❌"
        recommendation = "Не рекомендую"
    case _:
        description = None

# Вывод
if description:
    print(f'\nРейтинг {product_rating} → "{description} {rating_emoji} {recommendation}"')
else:
    print("\nОшибка: введите корректное целое число от 1 до 10 💀💀💀.")