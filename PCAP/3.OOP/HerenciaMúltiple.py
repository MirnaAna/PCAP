class saiyan:
    origen="saldana"
    def __init__(self, nombre):
     self.nombre = nombre

class Humano:
    planeta= "Tierra"
    def __init__(self,nombre):
        self.nombre = nombre

class Mestizo(saiyan, Humano):
   def __init__(self, nombre,a, b):
      self.nombre= nombre
      self.padre = a.nombre
      self.madre = b.nombre

def verAncestro(self):
        for x in Mestizo.__bases__:
            print(x.__name__, end=' ')
        print()
    

goku = saiyan("Son Goku")
vegeta = saiyan("vegeta")
bulba = Humano("Bulba")
trunks = Mestizo("Trunks", vegeta, bulba)

print(type(goku).__name__)
print(type(bulba).__name__)
print(type(trunks).__name__)

print(goku)
print(trunks.__dict__)
print(f"El padre de {trunks.nombre} es {trunks.__dict__["padre"]} y de la madre es {trunks.__dict__["madre"]}")
print(trunks.origen)
saiyan.origen="Tierra"
print(trunks.origen)

if type(trunks).__name__ == "Mestizo":
    if issubclass(Mestizo, saiyan):
        print(f"{trunks.nombre} puede convertir en super saiyan. ")
        if issubclass(Mestizo, Humano):
            print(f"{trunks.nombre} es un ser humano.")
    else:
        print(f"{trunks.nombre} no puede convertir en super saiyan.")






   
