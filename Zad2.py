class Road:
    def __init__(self, legthuse, widthuse):
        self._length = legthuse
        self._width = widthuse
    def roadmass(self,kg,sm):
        return self._width*self._length*kg*sm

while True:
    try:
       use1 = int(input("Введите длинну дороги (м) "))
       use2 = int(input("Введите ширину дороги (м) "))
       break
    except ValueError:
        print("Желательно цифрами")
        continue
road = Road(use1,use2)
print(road.roadmass(25,5),"т. на 5 см толщены и 25 кг весса")
