#Ввод
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
        print("ошибка ввода, координаты выходят за пределы стандартной шахматной доски")
    elif col1 == col2 and row1 == row2:
        print("ошибка ввода, клетки должны отличаться")
    else:
        #Логика хода слона
        col_diff = abs(col1 - col2)
        row_diff = abs(row1 - row2)
        is_diagonal_move = col_diff == row_diff

        #Результат
        print("YES" if is_diagonal_move else "NO")

except ValueError:
    print("ошибка ввода, введите число")