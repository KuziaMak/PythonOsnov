with open("Text6.txt","r",encoding="utf-8-sig") as f:
    massa = {}
    for i in f.readlines():
        summa = [0]
        i = i.split()
        for j in i[1:]:
            j = j.split("(")
            try:
                summa.append(int(j[0]))
            except ValueError:
                pass
        massa[f"{i[0]}"] = sum(summa)
print("Файл закрыт")
print(massa)