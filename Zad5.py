import functools

massa = [x for x in range(100, 1001, 2)]
final = functools.reduce(lambda x, y: x + y, massa)
print(final)
