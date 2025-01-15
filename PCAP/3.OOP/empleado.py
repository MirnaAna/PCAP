class Empleado:
    def __init__(self, nombre, cargo, salario=100):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario 

    def get_salario(self):
        return self.__salario 
    def __str__(self):
        return f"{self.nombre} es un {self.cargo} y gana {self.__salario}"

ListaEmpleados=[
    Empleado("Juanma", "Director", 75000.0),
    Empleado("Teresa", "Presidente", 80000.0),
    Empleado("Ana", "Administrativo", 20000.0)
]
empleados_vip= [empleado for empleado in ListaEmpleados if empleado.get_salario() > 50000]

for e in empleados_vip:
    print(e)

empleado1 = Empleado("Juan", "Gerente", 5000)
print(empleado1.get_salario())