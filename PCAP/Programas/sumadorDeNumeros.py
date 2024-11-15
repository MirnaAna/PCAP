#sumador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split() # list(line) seria otra forma 
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print("error: '"+substr+"'no es un numero.")