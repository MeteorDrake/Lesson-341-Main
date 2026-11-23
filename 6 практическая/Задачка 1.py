#Ввод
temperature_input = input("Введите вашу температуру тела(к примеру 36.6): ")
systolic_input = input("Теперь ваше верхнее давление(к примеру 120): ")
pulse_input = input("Теперь ваш пульс формата ударов в минуту(к примеру 72): ")

temperature = float(temperature_input.replace(",", "."))
systolic_pressure = int(systolic_input)
heart_rate = int(pulse_input)

#Константы
TEMP_NORMAL = (36.0, 37.0)
TEMP_MILD = ((35.0, 36.0), (37.0, 38.0))
PRESSURE_NORMAL = (110, 130)
PRESSURE_MILD = ((105, 110), (130, 140))
PULSE_NORMAL = (60, 100)
PULSE_MILD = ((55, 60), (100, 110))


#Проверка
def in_range(value, bounds):
  low, high = bounds
  return low <= value <= high


def in_mild(value, ranges):
  (low1, high1), (low2, high2) = ranges
  return low1 <= value < high1 or high1 < value <= high2


def is_critical(value, normal, mild):
  return not in_range(value, normal) and not in_mild(value, mild)


critical = (
    is_critical(temperature, TEMP_NORMAL, TEMP_MILD)
    or is_critical(systolic_pressure, PRESSURE_NORMAL, PRESSURE_MILD)
    or is_critical(heart_rate, PULSE_NORMAL, PULSE_MILD)
)
normal = (
    in_range(temperature, TEMP_NORMAL)
    and in_range(systolic_pressure, PRESSURE_NORMAL)
    and in_range(heart_rate, PULSE_NORMAL)
)
mild = (
    in_mild(temperature, TEMP_MILD)
    or in_mild(systolic_pressure, PRESSURE_MILD)
    or in_mild(heart_rate, PULSE_MILD)
)

#Результаты
result = (
    "Обнаружены отклонения, требуется врач."
    if critical
    else (
        "Всё в порядке, показатели в норме."
        if normal
        else (
            "Лёгкие отклонения, требуется отдых."
            if mild
            else "Показатели на границе нормы, рекомендуется легкое наблюдение."
        )
    )
)

print(f"\nИтог: {result}")