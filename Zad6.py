Tovar = []
while True:
    try:
        kol = int(input("Ведите количество разных товаров: "))
    except ValueError:
        print("Нужно цифру")
        continue
    for i in range(1, kol + 1):
        name = input("Введите название товара: ")
        try:
            cena = int(input("Ведите цену товара(число): "))
            vol = int(input("Ведите количество товара(число): "))
        except ValueError:
            print("Нужно цифру")
            continue
        ed = input("Введите единицу измерения товара(шт. т. и т.д.): ")

        Tovar.append((i, {"название":name, "цена":cena,  "количество": vol, "eд":ed }))
        print(Tovar)

    break

katal = {'название': [], 'цена': [], 'количество': [], 'eд': []}
for i in Tovar:
    katal['название'].append(i[1]['название'])
    katal['цена'].append(i[1]['цена'])
    katal['количество'].append(i[1]['количество'])
    katal['eд'].append(i[1]['eд'])
print(katal)
