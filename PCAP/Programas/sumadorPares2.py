#sumador de Números.
from imprimir_pares import imprime_pares as impp

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split() # list(line) seria otra forma 
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print("error: '"+substr+"'no es un numero.")

impp(strings)