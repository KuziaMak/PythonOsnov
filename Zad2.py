def info(name, famali, yeas, email, tell):
    return f"{name} {famali} {yeas} лет. Имеет почту: {email} и телефон: {tell}"


while True:
    data1 = input("Введите имя: ")
    data2 = input("Введите Фамилию: ")
    data3 = input("Почту: ")
    try:
        data4 = int(input("Введите сколько вам лет(цифру): "))
        data5 = int(input("теллефон(цифрами жилательно): "))
    except ValueError:
        print("Давай сначало умник\nи чтоб без букв ")
        continue
    print(info(tell=data5, yeas=data4, famali=data2, name=data1, email=data3))
    break
