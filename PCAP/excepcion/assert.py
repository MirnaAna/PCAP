import math

x = float(input("Ingresa un número: "))

try:
    assert x >= 0.0
except AssertionError:
    print("El valor ingresado debe ser >=0. ")
    exit(1)
x = math.sqrt(x)
    
print(x)