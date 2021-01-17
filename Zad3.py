class Worker:
    def __init__(self,nameuse,surnameuse,positionuse,incomeuse):
        self.name = nameuse
        self.surname = surnameuse
        self.position = positionuse
        self._income = incomeuse
class Position(Worker):
    def get_full_name(self):
        return f"Ваше полное имя и должность {self.name} {self.surname} {self.position}"
    def get_total_income(self):
        return f"Ваш оклад:{self._income['wage']+self._income['bonus']}"
name = "Максим"
surname = "Максимычь"
position = "Должность"
income = {"wage": 20000, "bonus": 500}
info = Position(name,surname,position,income)
print(f"{info.get_full_name()}\n{info.get_total_income()}")