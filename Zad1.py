import time
class TrafficLight:
    def __init__(self):
        self.__color = ["красный","желтый","зеленый"]
    def running(self):
        print(self.__color[0])
        time.sleep(7)
        print(self.__color[1])
        time.sleep(2)
        print(self.__color[2])
        time.sleep(10)
        return "" # Как без пропуска сделать не могу понять

while True:
    print(TrafficLight().running())