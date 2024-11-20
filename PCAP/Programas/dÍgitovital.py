feche=''
while True:
    fecha= input("Introduce tu fecha de nacimiento(en formato AAAAMMDD):")
    if fecha.isnumeric():
      break
    print("Debes traducir un formato AAAAMMDD")

digito = 0
suma = 0
for c in fecha:
   suma +=int(c)

if len(str(suma)) >1:
   digito = int(c)
else:
  digito = suma
print("El digito verificador es:",digito)


