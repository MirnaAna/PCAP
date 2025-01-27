class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: ¡Guau!"
 
 
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, Corderito!"
 
 
class GuardDog(SheepDog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, Señor Intruso!"
    
class LowLandDog(SheepDog):
    def __str__(self):
        return super().__str__() + " ¡ Guau! ¡no me gustan las montañas!"
 
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
toby = GuardDog("Chihauuu")

print(rocky)
print(luna)
print(toby)

