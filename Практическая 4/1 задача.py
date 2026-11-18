import math

number = float(input("Введите вещественное число: "))

# округление
result = math.floor(number) + math.ceil(number)

print(result)
