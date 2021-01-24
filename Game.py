import random


class Cart:
    def __init__(self, name=None):
        self.name = name

    @property
    def loto(self):
        self.massa = []

        for i in range(0, 3):
            j = 0
            mass = []
            while j != 5:
                paftor = 0
                a = random.randint(1, 90)
                if a in mass:
                    paftor = 1
                for r in self.massa:
                    if a in r:
                        paftor = 1
                if paftor == 1:
                    continue
                mass.append(a)
                j += 1
            mass = sorted(mass)
            for e in range(4):
                mass.insert(len(mass) - random.randint(1, 5), "")

            self.massa.append(mass)
        return list(map(lambda x: list(map(lambda y: str(y), x)), self.massa))


class Lotogame:
    def __init__(self, playera, playerb):
        self.playera = playera
        self.playerb = playerb

    def start(self):
        self.all1 = self.playera.loto
        self.all2 = self.playerb.loto
        self.musor = []
        for q in range(90, 0, -1):
            dumb = False
            right = 0

            print(f"{self.playera.name}:\n", "-" * 25, "\n",
                  f"{' '.join(self.all1[0])}\n {' '.join(self.all1[1])}\n {' '.join(self.all1[2])}\n", "-" * 25)
            print(f"{self.playerb.name}:\n", "-" * 25, "\n",
                  f"{' '.join(self.all2[0])}\n {' '.join(self.all2[1])}\n {' '.join(self.all2[2])}\n", "-" * 25)
            rand = random.randint(1, 90)
            while rand in self.musor:
                rand = random.randint(1, 90)
                continue
            self.musor.append(rand)
            for w in self.all1:
                if str(rand) in w:
                    w[w.index(str(rand))] = "-"
                    right = 1
            for u in self.all2:
                if str(rand) in u:
                    u[u.index(str(rand))] = "-"
            print(f"Новая цифра: {rand} ходов осталось: {q}")
            usereply = input(f"Зачеркнуть цифру? (y/n):\n")
            if (usereply == "y" and right == 0) or (usereply == "n" and right == 1):
                dumb = True
            elif (usereply == "y" and right == 1) or (usereply == "n" and right == 0):
                pass
            else:
                print("Нет ответ должен быть y или n ")
                break
            if self.all1[0].count("-") == 5 and self.all1[1].count("-") == 5 and self.all1[2].count("-") == 5:
                print(f"Победил: {self.playera.name}")
                break
            if (self.all2[0].count("-") == 5 and self.all2[1].count("-") == 5 and self.all2[2].count(
                    "-") == 5) or dumb == True:
                print(f"Победил: {self.playerb.name}")
                break


player = Cart("Игрок")
nps = Cart("Компьютер")
game = Lotogame(player, nps)
game.start()
