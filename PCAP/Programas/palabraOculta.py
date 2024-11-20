# entrada de la palabra
"""
tenemos dos cadenas: una palabra perro (p.ej. "perro")
"""
palabra = input("Introduce la palabra a buscar:").upper
grupo = input("introduce grupo de caracteres: ").upper
print(palabra)
contiene = True 
inicio= 0

for c in palabra:

    pos = grupo.find(c, inicio)    #devuelve -1 si no está
    if pos < 0:        #si el carácter no está, terminamos
        contiene = False
        break
    inicio= pos + 1
if contiene:
    print("La palabra contiene todos los caracteres del grupo")
else:
    print("La palabra no contiene todos los caracteres del grupo")
    