import math

#Координаты точек
x1, y1 = map(float, input("Введите координаты первой точки (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x2 y2): ").split())

# Расчет расстояния
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distance)
