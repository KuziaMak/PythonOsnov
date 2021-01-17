import itertools, sys

try:
    v, y = sys.argv[1], sys.argv[2]
    if v == "a":
        x = sys.argv[3]
        y, x = int(y), int(x)
        for i in itertools.count(y):
            if i > x:
                break
            print(i)

    elif v == "b":
        y = int(y)
        j = 1
        for i in itertools.cycle("BatMan"):
            if j > y:
                break
            print(i)
            j += 1

    else:
        raise ValueError
except ValueError:
    print("Введите а для первого скрипта и два значение через пробел начало и конец цикла(включительно конец)\n"
          "Введите b для первого скрипта и одно значение через пробел конец цикла(включительно конец)")
except IndexError:
    print("Недостаточно или слишком много параметров")
