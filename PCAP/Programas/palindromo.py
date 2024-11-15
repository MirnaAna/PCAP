# comprueba que una frase es un palindromo

# Ejemplos de palíndromo: Arriba la birra, sé verla al reves, Borrow or rob , so many dynamos

frase = input("introduce una frase: ")
frase2 = (frase.lower()).replace(' ','')

if frase2 == frase2[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")