try:
    y = 1 / 0
    #excepcion mas concreta 
except (ZeroDivisionError, ArithmeticError):
    print("Hubo un problema la hacer la operacion")
except: #excepcion sin nombre
    print("Algo ha cascao aquí...")

print("FIN.")