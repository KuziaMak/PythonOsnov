natural = [9, 8, 8, 5, 5, 5, 5, 4, 3, 3, 3, 3, 3, 3, 1, 1, 1]
while True:
    try:
        number = int(input("Введите число добавляйся в рейтинг: "))

    except ValueError:
        print("ЧИСЛО нужно ЧИСЛО")
        continue

    if number in natural:
        rek = natural.index(number)
        natural.insert(rek, number)
    else:
        if number < natural[len(natural) - 1]:
            natural.append(number)
        elif number > natural[len(natural) - 1] and number < natural[0]:
            ceslo = len(natural) - 1
            while number > natural[ceslo] and ceslo != 0:
                ceslo -= 1
            natural.insert(ceslo + 1, number)
        elif number > natural[0]:
            natural.insert(0, number)

    print(natural)
