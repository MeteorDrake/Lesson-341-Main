# Номер места в вагоне
seat_number = int(input("Введите номер места в вагоне: "))

# Вычисления
coupe_number = (seat_number - 1) // 4 + 1

#Вывод
print(coupe_number)
