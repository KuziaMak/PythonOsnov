def my_func(x, y):
    if y >= 0:
        return x ** y
    elif y < 0:
        return 1 / (x ** (-y))


def my_func2(x, y):
    c = x
    if y > 0:
        for i in range(1, y):
            x *= c
        return x

    elif y < 0:
        for i in range(1, -y):
            x *= c
        print(x)
        return 1/x
    elif y == 0:
        x = 1
        return x

while True:
    try:
        number1 = int(input("Введите число: "))
        number2 = int(input("Введите степень: "))
    except ValueError:
        print("Вы потеряли карму введя не число")
        continue
    break
while True:
    vibor = input("Какой вариант подсчета? Введите либо - a либо b: ")
    if vibor == "a":
        print(my_func(number1, number2))
        break
    elif vibor == "b":
        print(my_func2(number1, number2))
        break
    else:
        continue
