def mal_usunto(n):
    try:
        return n / 0
    except:
        print("¡lo hice otra vez!")
        raise #regenera la excepcion
try:
    mal_usunto(0)
except ArithmeticError:
    print("¡Ya veo!")
    exit(0)

print("EN-FIN.")