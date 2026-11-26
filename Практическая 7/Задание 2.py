import random

#Запрос кода статуса
raw_status = input(
    "Введите код статуса заказа (pending, processing, shipped, delivered, cancelled): "
)
order_status = raw_status.strip().lower()

# Выбор информации по статусу
match order_status:
    case "pending":
        status_ru = "В ожидании"
        status_emoji = "⏳"
        description = "Заказ принят и ожидает подтверждения"
        wait_time = f"{random.randint(10, 30)} минут"
        advice = "Ожидайте уведомления о начале сборки"
    case "processing":
        status_ru = "В обработке"
        status_emoji = "⚙️"
        description = "Ваш заказ собирается и упаковывается на складе"
        wait_time = f"{random.randint(1, 3)} часа(ов)"
        advice = "Скоро мы передадим посылку в службу доставки"
    case "shipped":
        status_ru = "Отправлено"
        status_emoji = "✈️"
        description = "Ваш заказ находится в пути к вам"
        wait_time = f"{random.randint(2, 5)} дней"
        advice = "Следите за уведомлениями о доставке"
    case "delivered":
        status_ru = "Доставлено"
        status_emoji = "✅"
        description = "Заказ успешно вручён получателю"
        wait_time = "0 минут (завершено)"
        advice = "Спасибо за покупку! Будем рады вашему отзыву"
    case "cancelled":
        status_ru = "Отменено"
        status_emoji = "🚫"
        description = "Заказ был отменён"
        wait_time = "Не применимо"
        advice = "Если это произошло по ошибке, оформите заказ заново"
    case _:
        status_ru = "💀"

# Вывод
if status_ru:
    print("\n╔════════════════════════════════════════╗")
    print("║        📦 СТАТУС ВАШЕГО ЗАКАЗА 📦      ║")
    print("╚════════════════════════════════════════╝\n")
    print(f"Статус: {status_ru} {status_emoji}")
    print(f"Описание: {description}")
    print(f"Примерное время: {wait_time}")
    print(f"Рекомендация: {advice}")
else:
    print(f'\n❌ Ошибка: Неизвестный статус "{raw_status.strip()}"')
    print("Доступные статусы: pending, processing, shipped, delivered, cancelled")