def mal_uso(n):
    raise ZeroDivisionError


try:
    mal_uso(0)
except ArithmeticError:
    print("¿Qué pasó? ¿Un error?")

print("FIN.")
    
