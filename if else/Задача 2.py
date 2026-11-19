print("Введите длинну всех сторон треугольника (через строку)")
side_a, side_b, side_c = float(input()), float(input()), float(input())

if side_a == side_b == side_c:
    print("Треугольник - равносторонний")
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print("Треугольник - равнобедренный")
else:
    print("Треугольник - разносторонний")
