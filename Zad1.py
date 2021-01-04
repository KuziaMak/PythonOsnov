import sys

try:
    a, b, c = sys.argv[1:]
    a, b, c = int(a), int(b), int(c)
    print((a * b) + c)
except ValueError:
    print("Введите три переменных в кансоль python Zad1.py a b c \n"
          "Где a-выработка в часах\n"
          "b-ставка в час\n"
          "c-премия\n"
          "переменные функция расчета заработной платы сотрудника (a*b)+c ")
