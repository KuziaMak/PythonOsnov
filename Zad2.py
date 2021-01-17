massa = [1, 2, 12, 44, 1, 3, 4, 10, 7, 1, 78, 123, 55]

maximus = [x for x in massa[1:] if x > massa[massa.index(x) - 1]]
print(maximus)
