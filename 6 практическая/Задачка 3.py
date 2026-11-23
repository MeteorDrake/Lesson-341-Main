#Вводы
col1_input=input("Введите координату(в формате целого числа) 1-й клетки по горизонтали (столбец): ")
row1_input=input("Введите координату(в формате целого числа) 1-й клетки по вертикали (строка): ")
col2_input=input("Введите координату(в формате целого числа) 2-й клетки по горизонтали (столбец): ")
row2_input=input("Введите координату(в формате целого числа) 2-й клетки по вертикали (строка): ")

#Проверка
try:
    col1 = int(col1_input)
    row1 = int(row1_input)
    col2 = int(col2_input)
    row2 = int(row2_input)

    if not (1 <= col1 <= 8 and 1 <= row1 <= 8 and 1 <= col2 <= 8 and 1 <= row2 <= 8):
        print("ошибка ввода")
    else:
        # Сравнение цветов клеток
        is_first_even = (col1 + row1) % 2 == 0
        is_second_even = (col2 + row2) % 2 == 0
        is_same_color = is_first_even == is_second_even

        #Результаты
        print("YES" if is_same_color else "NO")

except ValueError:
    print("ошибка ввода, введите число")
