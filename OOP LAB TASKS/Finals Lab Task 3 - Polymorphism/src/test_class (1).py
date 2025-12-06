
from birdClass import Bird
from birds import Sparrow,Parrot
from birdCage import Birdcage

sparrow0 = Sparrow()
sparrow0.name = "Sparrow"
parrot0 = Parrot()
parrot0.name = "Parrot"

print("Invoking object Sparrow method:")
sparrow0.make_sound()

print("\nInvoking object Parrot method:")
parrot0.make_sound()

print()
print("Invoking object Bird Cage method:")
cage0 = Birdcage([sparrow0,parrot0])
cage0.make_sound()




