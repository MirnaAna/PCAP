class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque

    def atacar(self, otro_pokemon):
        if otro_pokemon.vida <= 0:
            raise ValueError("El Pokémon objetivo ya ha sido derrotado")
        ventajas = {
            "agua": "fuego",
            "fuego": "planta",
            "planta": "agua"
        }

        if ventajas[self.tipo] == otro_pokemon.tipo:
            dano = self.ataque * 1.5
        else:
            dano = self.ataque

        otro_pokemon.vida -= dano
        print(f"{self.nombre} ataca a {otro_pokemon.nombre} con {dano} de daño")

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Vida: {self.vida}, Ataque: {self.ataque}"
    
pokemon1 = Pokemon("Pikachu", "fuego", 100, 20)
pokemon2 = Pokemon("Dragonair", "agua", 100, 25)

pokemon1.atacar(pokemon2)
print(pokemon2)
pokemon2.atacar(pokemon1)
print(pokemon1)
pokemon1.atacar(pokemon2)
print(pokemon2)
