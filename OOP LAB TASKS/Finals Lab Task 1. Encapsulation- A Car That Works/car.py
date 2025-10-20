
class Car:
    def __init__(self,color=None,price=None, size=None):
        self.__color = color
        self.__price = price
        self.__size = size

    @property
    def car_color(self):
        print("Getter is invoked!")
        return self.__color

    @car_color.setter
    def car_color(self,newColor):
        self.__color = newColor
        print("")


    @property
    def car_price(self):
        return self.__price

    @car_price.setter
    def car_price(self,newPrice):
        self.__price = float(newPrice)


    @property
    def car_size(self):
        sizelist = {'S': 'SMALL',
                    'M': 'MEDIUM',
                    'L': 'LARGE'}
        if self.__size in sizelist:
            return sizelist[self.__size]
        return self.__size

    @car_size.setter
    def car_size(self,newSize):
        self.__size = newSize




if __name__ == "__main__":
    car1 = Car()
    car1.car_color = "White"
    car1.car_size = "M"
    car1.car_price = 17

    print(f"for a {car1.car_color} car "
          f"price at {car1.car_price} "
          f"and of {car1.car_size.upper()} size")

    print(f"{car1.car_color} - {car1.car_price} - {car1.car_size.upper()}")

