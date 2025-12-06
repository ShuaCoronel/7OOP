from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass





