def dell(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "нельзя делить на ноль"

while True:
    try:
        nuber1 = int(input("Введите числитель: "))
        nuber2 = int(input("Введите знаменатель: "))
    except ValueError:
        print("Цифру надо Цифру")
        continue

    print(dell(nuber1,nuber2))
    break
