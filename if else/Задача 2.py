# Ввод сторон треугольника
side_a = float(input("Введите длину первой стороны: "))
side_b = float(input("Введите длину второй стороны: "))
side_c = float(input("Введите длину третьей стороны: "))

# Существует ли треугльник
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    
    # Тип существующего треугольника
    if side_a == side_b == side_c:
        print("Равносторонний")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
        
else:
    print("Треугольник с такими сторонами не существует")
