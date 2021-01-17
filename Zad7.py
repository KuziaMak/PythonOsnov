import math
def fact(n):
    yield math.factorial(n)
while True:
    try:
        n = int(input("Введите факториал "))
        if n < 0:
            continue
        break
    except ValueError:
        print("В виде цифор пожалуста ")
        continue
for el in fact(n):
    print(el)