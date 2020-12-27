summa = 0
qui = ''

while True:
    uzervod = input("Введите числа через пробел или q для выхода: ")
    uzervod = uzervod.split()
    for i in uzervod:
        try:
            i = int(i)
        except ValueError:
            i = i
        if type(i) == int:
           summa+= int(i)
        elif type(i) == str:
            if i == 'q':
                qui = "q"
    if qui == "q":
        break
    print(summa)
print(summa)