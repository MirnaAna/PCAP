import random
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    def atacar(self, otro_personaje):
        if otro_personaje.vida <= 0:
            raise ValueError("El personaje ya está derrotado")
        if random.random() < 0.2:
            print(f"{otro_personaje.nombre} esquiva el ataque")
        else:
            otro_personaje.vida -= self.ataque
            print(f"{self.nombre} ataca a {otro_personaje.nombre} por {self.ataque} de daño")
    def esquivar(self):
        return random.random()< 0.2
    
class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, magia):
        super().__init__(nombre, vida, ataque)
        self.magia = magia
    def ataque_especial(self, otro_personaje):
        if otro_personaje.vida <= 0:
            raise Exception("No puedes atacar a un personaje derrotado")
        if random.random() < 0.2: 
            print(f"{otro_personaje.nombre} esquiva el ataque especial")
        else:
            otro_personaje.vida -= self.ataque + self.magia
            print(f"{self.nombre} ataca a {otro_personaje.nombre} por {self.ataque + self.magia} de daño")
            if random.random() < 0.5:
                self.vida += self.ataque
                print(f"{self.nombre} se cura por {self.ataque} de vida")


guerrero = Personaje("Guerrero", 100, 20)
mago = Personaje("Mago", 80, 15)

guerrero.atacar(mago)
print(f"la vida restante de {mago.nombre}:{mago.vida}")


