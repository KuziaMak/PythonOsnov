usnumb = int(input("Введите целое положительное число: "))
maxim = usnumb % 10
while usnumb > 0:
    if usnumb % 10 > maxim:
        maxim = usnumb % 10
    usnumb //= 10
print(f"Самое большое число: {maxim} ")
