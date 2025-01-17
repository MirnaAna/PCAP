class Empleado:
    plantilla = []
    num_pleado=0


    def __init__(self, nombre: str, cargo:str, salario=25000.50):

        if salario < 0:
            raise ValueError("El salario no puede ser cero")
        
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario 
        Empleado.plantilla.append(self)
        Empleado.num_pleado+=1
    
    def get_salario(self):
        return self.__salario 
    
    def __str__(self):
        return f"{self.nombre} es un {self.cargo} y gana {self.__salario}"
  
empleado1= Empleado("Juanma", "Director", 75000.0),
empleado2= Empleado("Teresa", "Presidente", 80000.0),
empleado3= Empleado("Ana", "Administrativo", 20000.0),

for e in Empleado.plantilla:
    print(e)
