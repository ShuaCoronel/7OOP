from performer import Performer
from singer import Singer
from dancer import Dancer

#object for case 1, base class
human0 =  Performer()
human0.name = input("Enter your name: ")
human0.age = int(input("Enter your age: "))
human0.info()  #base class Performer method prints performer "info()"

#object for case 2, singer: subclass inherits base class attr.
human1 = Singer()
print()
human1.name = input("Enter your name: ")
human1.age = int(input("Enter your age: "))
human1.vocal_range = input("Enter your vocal range: ")

#singer sub class method sing
human1.info()
human1.sing()

#object for case 3, dancer: subclass inherits base class attr.
human2 = Dancer()
print()
human2.name = input("Enter your name: ")
human2.age = int(input("Enter your age: "))
human2.dance_style = input("Enter your dance style: ")

human2.info()
human2.dance_move()








