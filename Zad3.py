class Cell:
    def __init__(self,cyslo):
        self.cyslo = cyslo

    def __add__(self, other):
        try:
            self.cyslo += other.cyslo
            return self
        except AttributeError:
            self.cyslo += other
            return self
    def __sub__(self, other):
        try:
            self.cyslo -= other.cyslo
            return self
        except AttributeError:
            self.cyslo -= other
            return self
    def __mul__(self, other):
        try:
            self.cyslo *= other.cyslo
            return self
        except AttributeError:
            self.cyslo *= other
            return self
    def __truediv__(self, other):
        try:
            self.cyslo //= other.cyslo
            return self
        except AttributeError:
            self.cyslo //= other
            return self
    def __str__(self):
        return f"{self.cyslo}"
    def make_order(self):
        for i in range(1,self.cyslo+1):
            if i %5 == 0:
                print(f"*\n", end="")
            else:
                print("*",end="")
        print("\nend")


cell1 = Cell(20)
cell2 = Cell(50)
print(cell1,cell2)
a = 2
b = 3
cell1 * b
cell1 / a
cell2 / b
cell1 + cell2
print(cell1,cell2)
cell1.make_order()
