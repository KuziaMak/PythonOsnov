with open("Text5.txt","w+",encoding="utf-8-sig") as f:
    usernumb = input("Введите числа через пробел: ").split()
    for i in usernumb:
        f.write(f"{i}\n")
    try:
        massa = []
        f.seek(0)
        for i in f.readlines():
            i = float(i)
            massa.append(i)
        print(sum(massa))
    except ValueError:
        print("ЧИСЛА")
        f.close()





print("Файл закрыт")