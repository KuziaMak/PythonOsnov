class Stationery:
    def __init__(self,titleuse):
        self.title = titleuse
    def draw(self):
        return f"Запуск отрисовки {self.title}"
class Pen(Stationery):
    def draw(self):
        return f"Запуск росписи {self.title}"
class Pencil(Stationery):
    def draw(self):
        return f"Запуск рисовки {self.title}"
class Handle(Stationery):
    def draw(self):
        return f"Запуск лени {self.title}"

stat = Stationery("Картины")
print(stat.draw())
pen = Pen("Текста")
print(pen.draw())
penc = Pencil("Рисунка")
print(penc.draw())
hand = Handle("Моей")
print(hand.draw())