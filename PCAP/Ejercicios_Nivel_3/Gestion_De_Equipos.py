class Item:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.rareza})"


class InventarioLlenoError(Exception):
    pass

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_item(self, item):
        if len(self.inventario) >= 5:
            raise InventarioLlenoError("El inventario está lleno")
        self.inventario.append(item)

    def eliminar_item(self, item):
        if item not in self.inventario:
            raise ValueError("El objeto no está en el inventario")
        self.inventario.remove(item)

    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre}:")
        for item in self.inventario:
            print(item)



personaje = Personaje("Ana")

 
espada = Item("Espada", "Arma", "Épica")
armadura = Item("Armadura", "Armadura", "Legendaria")
poción = Item("Poción", "Poción", "Común")


personaje.agregar_item(espada)
personaje.agregar_item(armadura)
personaje.agregar_item(poción)


 
personaje.mostrar_inventario()


try:
    personaje.agregar_item(poción)
except InventarioLlenoError as e:
    print(e)

personaje.eliminar_item(espada)

personaje.mostrar_inventario()
