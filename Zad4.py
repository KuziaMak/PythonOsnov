massa = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

norepe = [x for x in massa if massa.count(x) == 1]
print(norepe)
