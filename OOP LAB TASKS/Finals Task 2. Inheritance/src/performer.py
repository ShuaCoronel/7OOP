
class Performer:
    def __init__(self, name:str = None ,age:int = None):
        self.__name = name
        self.__age = age
#initial "None" null value for parameter to accept userinput

    @property #getter for dunder attr
    def name(self):
        return self.__name
    @name.setter #setter for  dunder attr
    def name(self, name:str):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age:int):
        self.__age = age

    def info(self):
        print(f"Name: {self.name} \n"
              f"Age: {self.age} years old")

#testing
if __name__ == '__main__':
    basePerson = Performer('John',25)
    print(basePerson.name)
    print(basePerson.age)

