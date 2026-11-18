# Ввод 4-значного числа
number = int(input("Введите положительное четырёхзначное число: "))

# Извлечение цифр
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
units_digit = number % 10

# Выводы
print(f"Цифра в позиции тысяч равна {thousands_digit}")
print(f"Цифра в позиции сотен равна {hundreds_digit}")
print(f"Цифра в позиции десятков равна {tens_digit}")
print(f"Цифра в позиции единиц равна {units_digit}")
