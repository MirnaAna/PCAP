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

if suma < 10:
   digito = suma
else:# si no, repetimos la operación
  for c in str(suma):
     digito += int(c)
print("El digito verificador es:",digito)


