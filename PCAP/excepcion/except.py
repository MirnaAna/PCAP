try:
    y = 1 / 0
    #excepcion mas concreta 
except ZeroDivisionError:
    print("¡División entre cero!")
    #excepcion mas abstracta
except ArithmeticError:
    print("¡Problema Aritmético!")
except: #excepcion sin nombre
    print("Algo ha cascao aquí...")

print("FIN.")
    