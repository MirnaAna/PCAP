class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

'''
la funcion toma un objeto cualquiera, busca en su interior atributos enteros con nombre 
que comiencen con 'i' y los suma, si no encuentra ninguno devuelve
0. Si encuentra mas de un atributo con el nombre que comienza con 'i' y
es entero, devuelve la suma de todos los atributos enteros con nombre que comienc
en 'i'.
'''
def incIntsI(obj):
    for clave in obj.__dict__.keys():
        if clave.startswith('i'):
            val = getattr(obj, clave)
            if isinstance(val, int):
                setattr(obj, clave, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)