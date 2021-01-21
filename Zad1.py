class Matrix:
    def __init__(self, matr, matr2):
        self.matr = matr
        self.matr2 = matr2
        self.summ = []

    def __add__(self, other):
        try:
            for i in range(0, len(other)):
                self.summ[i] = [x + y for x, y in zip(self.summ[i], other[i])]
        except IndexError:
            self.summ = other[:]

        return self

    def __str__(self):
        return f"Матрици: \n{self.matr[0]} ; {self.matr2[0]}\n{self.matr[1]} ; { self.matr2[1]} \n " \
               f"Сумма: \n{self.summ[0]}\n{self.summ[1]} "


matr1 = [[5, 6, 2], [1, 8, 2]]
matr2 = [[8, 5, 4], [3, 7, 9]]
mat = Matrix(matr1, matr2)
mat + matr1 + matr2
print(mat)
