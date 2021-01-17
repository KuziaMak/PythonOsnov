class Car:
    def __init__(self,speeduse,coloruse=None,nameuse=None,is_policeuse=None):
        self.speed = speeduse
        self.color = coloruse
        self.name = nameuse
        self.is_police = is_policeuse
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self,direction):
            return f"Повернула в {direction}"
    def show_speed(self):
        return f"{self.speed} кл/ч"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Вы привысили скорость на {self.speed-60} кл/ч"
        else:
            return f"{self.speed} кл/ч"
class SportCar(Car):
    def show_speed(self):
        return f"Быстрее Быстрее скорость {self.speed} кл/ч"
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Вы привысили скорость на {self.speed-40} кл/ч"
        else:
            return f"{self.speed} кл/ч"
class PoliceCar(Car):
    def show_speed(self):
        if self.speed:
            return f"Вы не можите привысить скорость {self.speed} кл/ч"


while True:
    try:
       use1 = int(input("Введите скорость "))
       use2 = input("Введите какая у вас машина - лем; раб; спорт или мусор ")
       if use2 == "лем":
           carr = 0
           pol = False
       elif use2 == "раб":
           carr = 1
           pol = False

       elif use2 == "спорт":
           carr = 2
           pol = False

       elif use2 == "мусор":
           carr = 3
           pol = True


       else:
           print(use2,"это не машина сначало")
           continue

       break
    except ValueError:
        print("Желательно цифрами")
        continue
car = Car(use1,"цветная","кто то называет машин по имени?",pol)
print(f"Данные о машине: скорость - {car.speed}, имя - {car.name}, цвет - {car.color}, из полиции {car.is_police}")
print(car.stop(),car.go(),car.turn("налево"),car.go(),car.turn("направо"))
choice = [TownCar,WorkCar,SportCar,PoliceCar]
print(choice[carr](use1).show_speed())
