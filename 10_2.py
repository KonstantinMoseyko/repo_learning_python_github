from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, user_num):
        self.user_num = user_num

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return self.user_num / 6.5 + 0.5


class Costume(Clothes):
    @property
    def tissue_consumption(self):
        return 2 * self.user_num + 0.3


finished_coat = Coat(5)
finished_costume = Costume(5)
print(finished_coat + finished_costume)
