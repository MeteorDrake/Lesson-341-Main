boxer_weight = int(input("Введите вес боксера (кг): "))

# Определение категории
if boxer_weight < 60:
    print("Легкий вес")
elif boxer_weight < 64:
    print("Первый полусредний вес")
elif boxer_weight < 69:
    print("Полусредний вес")
else:
    print("Вес не подходит ни под одну из трех категорий")
