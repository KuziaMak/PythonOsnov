with open("Text4.txt","r",encoding="utf-8-sig") as f:
    with open("Text4(2).txt","w+",encoding="utf-8-sig") as g:
        print(f.read())
        f.seek(0)
        massa = [mass.split(" ") for mass in f.readlines()]
        number = [num[0] for num in massa]
        new_number = [num.replace("One","Один").replace("Two","Два").replace("Three","Три").replace("Four","Четыре")
                      for num in number]
        t = 0
        for i in new_number:
            g.write(f"{i} {massa[t][1]} {massa[t][2]}")
            t+=1
        g.seek(0)
        print(g.read())#Возможно я слегка перемудрил, но это не точно
print("Файлы закрыты")