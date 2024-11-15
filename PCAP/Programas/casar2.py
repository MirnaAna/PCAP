# Cifrado César2 que tenga dos entradas de teclado , shift.
text = input("Ingresa tu mensaje: ")
shift2 = 0
while shift == 0:
    try:
        shift = int(input("Ingresa el valor de cambio del cifrado: "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        print("El valor de cambio debe ser un número entero entre 1 y 26")
        shift=0
text= text.upper()
cipher= ''
for char in text:
    #cambia de codigo
    code= ord(char) + shift
    #si el caracter es una letra
    primero= ord('A')
    shift2 += (code - primero) %26
    cipher += chr(primero + shift2 )
print(cipher)