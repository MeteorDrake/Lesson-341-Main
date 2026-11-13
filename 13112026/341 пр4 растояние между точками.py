import math
count = 0
def solve_distance(x1, y1, x2, y2):
    distance = (math.sqrt(((x1-x2)**2) + ((y1-y2)**2)))
    return distance

while(count !=3):
    result = solve_distance(float(input("Введите координату (x) первой точки:")),float(input("Введите координату (y) первой точки:")),float(input("Введите координату (x) второй точки:")),float(input("Введите координату (y) второй точки:")))
    print(f"Длинна отрезка: {result:.2f} сантиметров")
    count +=1
