# Количество школьников и мандаринов
students_count = int(input("Введите количество школьников: "))
mandarins_count = int(input("Введите количество мандаринов: "))

# Основные расчеты
mandarins_per_student = mandarins_count // students_count
mandarins_left = mandarins_count % students_count

#Выводы
print(mandarins_per_student)
print(mandarins_left)
