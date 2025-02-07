class Carta:
    def __init__(self, nombre, ataque, defensa, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Ataque: {self.ataque}, Defensa: {self.defensa}"

class CartaNoEncontradaError(Exception):
    pass

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mazo = []

    def agregar_carta(self, carta):
        self.mazo.append(carta)

    def invocar_carta(self, nombre):
        for carta in self.mazo:
            if carta.nombre == nombre:
                return carta
        raise CartaNoEncontradaError(f"La carta {nombre} no está en el mazo")

    def __str__(self):
        return f"Jugador {self.nombre} - {len(self.mazo)} cartas en el mazo"


class Batalla:
    def __init__(self, carta1, carta2):
        self.carta1 = carta1
        self.carta2 = carta2

    def luchar(self):
        if self.carta1.ataque > self.carta2.defensa:
            return f"{self.carta1.nombre} gana el juego"
        elif self.carta2.ataque > self.carta1.defensa:
            return f"{self.carta2.nombre} gana el juego"
        else:
            return "Empate"


# Ejemplo de uso
jugador1 = Jugador("Jugador 1")
carta1 = Carta("Dragón Blanco", 2000, 1500, "Monstruo")
carta2 = Carta("Dragón Negro", 2500, 1200, "Monstruo")

jugador1.agregar_carta(carta1)
jugador1.agregar_carta(carta2)

try:
    carta_invocada1 = jugador1.invocar_carta("Dragón Blanco")
    carta_invocada2 = jugador1.invocar_carta("Dragón Negro")
except CartaNoEncontradaError as e:
    print(e)
else:
    batalla = Batalla(carta_invocada1, carta_invocada2)
    print(batalla.luchar())  