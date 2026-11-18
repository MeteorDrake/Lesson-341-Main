import math

# Ввод угла
degrees = float(input("Введите угол в градусах: "))

# Перевод градусов в радиану
radians = math.radians(degrees)

# Основные расчеты
sine_value = math.sin(radians)
cosine_value = math.cos(radians)
result = sine_value + cosine_value + (sine_value / cosine_value) ** 2

#Вывод
print(result)
