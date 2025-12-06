
from birdClass import Bird

class Sparrow(Bird):
    def __init__(self, name=None):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name}: Chirp Chirp!")


class Parrot(Bird):
    def __init__(self, name = None):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name}: Tweet Tweet!")

