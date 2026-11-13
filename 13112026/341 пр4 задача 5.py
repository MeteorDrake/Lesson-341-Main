print("Введите кол-во детей")
kids = int(input())
print("Введите кол-во мандаринов")
orange = int(input())
if(kids>orange):
    print("Дети не получили не одного мандарина",orange//kids)
    print(orange%kids,"мандаринов осталось в корзине")
else:
    print("по",orange//kids,"Мандарина получили дети")
    print(orange%kids,"мандаринов осталось в корзине")