
while True:
    text1 = str("Introduce la 1ª palabra: ")
    if not text1.isalpha():
        print("Error: '"+text1+"', solo se permiten letras")
        break
    else:
        text2 = input("Introduce la 2ª palabra: ").upper()
        if not text1.isalpha():
            print("Error: '"+text2+"', solo se permiten letras")
            break

    if sorted(text1) == sorted(text2):
        print("Las palabras son anagramas")
    else:
        print("Las palabras no son anagramas")

    input

        
    
    