while True:
    number = input("Введите месяц: ")
    try:
        number = int(number)
        if number < 1 or number > 12:
            print("Сколько в году месяцов?")
            continue
    except ValueError:
        print("Цифру надо писать")
        continue
    mesic = {1: 'Зима', 2: 'Зима', 3: "Весна",
             4: "Весна", 5: "Весна", 6: "Лето",
             7: "Лето", 8: "Лето", 9: 'Осень',
             10: 'Осень', 11: 'Осень', 12: 'Зима'}  # Идей как сделать лудшее нет
    print(mesic[number])
    break
