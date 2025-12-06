from birdClass import Bird
from birds import Sparrow
from birds import Parrot

class Birdcage():
    def __init__(self, birds:list ):
        self.birds = birds


    def make_sound(self):
        for bird in self.birds:
            bird.make_sound()
