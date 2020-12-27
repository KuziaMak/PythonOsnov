def my_func(a,b,c):
    d = [a,b,c]
    return sum(d)-min(a,b,c)


while True:

    try:
        nuber1 = int(input(f"Введите 1 число: "))
        nuber2 = int(input(f"Введите 2 число: "))
        nuber3 = int(input(f"Введите 3 число: "))
    except ValueError:
        print("Это не было числом\nникогда не было...")
        continue
    print(my_func(nuber1,nuber2,nuber3))
    break