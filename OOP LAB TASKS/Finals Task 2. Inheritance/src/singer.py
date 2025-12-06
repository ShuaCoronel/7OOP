from performer import Performer

class Singer(Performer):
    def __init__(self, name = None, age = None, vocal_range:str=None):
        super().__init__(name,age) #inherits constructor name,age from Perfomer class
        self.__vocal_range = vocal_range #extra attr for child class

    @property
    def vocal_range(self):
            return self.__vocal_range

    @vocal_range.setter
    def vocal_range(self, vocal_range):
        self.__vocal_range = vocal_range


    def  sing(self):
        print(f"{self.name} is singing with a vocal range of {self.__vocal_range}")

