# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha(): # Si el caracter no es una letra, no lo cifra.
        continue
    char = char.upper()   #m --> M
    code = ord(char) + 1  # punto de codigo siguiente
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)