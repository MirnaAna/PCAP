def imprime_pares(lista):
    for num in lista:
        if int(num)% 2 ==0:
            print(num, end =' , ') #para separarlo con una coma end=''
        else:
            continue
