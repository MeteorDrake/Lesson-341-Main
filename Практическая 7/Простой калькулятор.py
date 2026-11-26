first_number = float(input("Введите первое число (целое или дробное, например 10 или 5.5): "))
operation_symbol = input("Введите символ операции (+, -, * или /): ")
second_number = float(input("Введите второе число (целое или дробное): "))

#Математические операторы
match operation_symbol:
    case "+":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
    case "-":
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")
    case "*":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
    case "/":
        if second_number == 0:
            print("Ошибка: деление на ноль.")
        else:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}")
    case _:
        print("Неизвестная операция.")