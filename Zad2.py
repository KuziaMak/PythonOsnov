while True:
    try:
        kol = int(input("Сколько элементов в списке? "))
    except ValueError:
        print("Введи ЦИФРУ!!!!! ")
        continue
    list1 = []
    for i in range(0, kol):
        element = input("введите этлемент: ")
        try:
            element = int(element)
        except ValueError:
            element = element
        finally:

            list1.append(element)
    print(list1)
    for j in range(0, len(list1[0:]) - 1, 2):
        rek = list1[j]
        list1[j] = list1[j + 1]
        list1[j + 1] = rek
    print(list1)
    break
