with open("Text3.txt", "r", encoding="utf-8-sig") as f:
    strok = f.readlines()
    massa, name = [], []

    for i in strok:
        i = i.split()
        massa.append({"name": i[0], "money": float(i[1])})
        if float(i[1]) < 20000:
            name.append(i[0].split(":")[0])

    sred = sum(mass["money"] for mass in massa) / len(massa)

    print(f"Те у кого зарплата меньше 20000: {name}\nСреднее значение всех окладов сотрудников: {sred} ")
print("Файл закрыт")
