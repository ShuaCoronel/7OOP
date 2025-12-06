from performer import Performer

class Dancer(Performer):
    def __init__(self, name:str=None ,age:int= None, dance_style:str = None):
        super().__init__(name,age) #inherits the constructor from Parent class
        self.__dance_style = dance_style #extra attr of child class

    @property
    def dance_style(self):
        return self.__dance_style

    @dance_style.setter
    def dance_style(self, dance_style):
        self.__dance_style = dance_style

    def dance_move(self):
        print(f"{self.name} is dancing {self.__dance_style}")