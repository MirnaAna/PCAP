tablero=[]
sudoku_ok= False
for i in range(9):
    fila= input("introduce fila" +str(i)+":")
#verificar que el sodoku es valido
    if not fila.isnumeric():
        print("La fila contiene caracteres no numéricos.")
        break
    elif sorted(fila) != list("123456789"):
        print(sorted(fila))
        print("la fila debe contener todos los digitos del intervalo [1-9]")
        break
    else:
      sudoku_ok=True
      tablero.append(fila)
    
if sudoku_ok:
     print("el sudoku si es valido")
else:
    print("el sudoku no es valido")