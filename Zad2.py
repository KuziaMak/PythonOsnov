from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def height(self):
        pass


class Palto(Clothes):
    def __init__(self, size):
        self._sizeuse = size

    @property
    def sizeuse(self):
        return self._sizeuse

    def size(self):
        return (self.sizeuse / 6.5 + 0.5)

    def height(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.heightuse = height

    def size(self):
        pass

    def height(self):
        return (2 * self.heightuse + 0.3)


palto = Palto(24)
suit = Suit(10)
print(palto.size(),palto.sizeuse)
print(suit.height())
