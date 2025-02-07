import random
import string

class PersonajeGacha:
    def __init__(self, nombre, rareza, elemento):
        self.nombre = nombre
        self.rareza = rareza
        self.elemento = elemento
        self.__id_secreto = self.generar_id_secreto()

    def generar_id_secreto(self):
        letras = string.ascii_uppercase
        digitos = string.digits
        return ''.join(random.choice(letras) for _ in range(2)) + ''.join(random.choice(digitos) for _ in range(3))

    def invocar(self):
        rarezas = [3, 4, 5]
        probabilidades = [0.8, 0.15, 0.05]
        rareza_invocada = random.choices(rarezas, weights=probabilidades)[0]
        return PersonajeGacha(f"Personaje {rareza_invocada} estrellas", rareza_invocada, "Elemento aleatorio")

    def __str__(self):
        return f"Nombre: {self.nombre}, Rareza: {self.rareza} estrellas, Elemento: {self.elemento}, ID secreto: {self.__id_secreto}"

personaje = PersonajeGacha("Personaje 5 estrellas", 5, "Elemento fuego")
invocacion = personaje.invocar()
print(invocacion)