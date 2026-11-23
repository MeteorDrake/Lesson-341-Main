#Ввод
pocket_input = input("Введите номер кармана от 0 до 36: ")

if not pocket_input.replace("-", "", 1).isdigit():
    print("ошибка ввода")
else:
    pocket_number = int(pocket_input)

    if not 0 <= pocket_number <= 36:
        print("ошибка ввода")
    elif pocket_number == 0:
        print("зелёный")
    else:
        #Диапазоны
        odd_is_red = 1 <= pocket_number <= 10 or 19 <= pocket_number <= 28
        is_odd = pocket_number % 2 != 0
        is_red = is_odd == odd_is_red

        print("красный" if is_red else "чёрный")