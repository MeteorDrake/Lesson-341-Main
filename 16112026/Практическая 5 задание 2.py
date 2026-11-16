def calculate_bmi():
    ##Счет ИМТ по весу и росту
    weight, height = map(float, input("Введтте ваш вес в килограммах и рост в метрах через пробел: ").split())
    return weight / (height * height)

bmi = calculate_bmi()

print(f"Ваш ИМТ: {bmi:.1f}")