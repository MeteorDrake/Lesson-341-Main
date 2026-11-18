# Ввод минут
total_minutes = int(input("Введите количество минут: "))

# Основные вычисления 
full_hours = total_minutes // 60
remaining_minutes = total_minutes % 60

#Вывод
print(f"{total_minutes} минуты это {full_hours} час {remaining_minutes} минут.")
