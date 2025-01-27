class Empleado:
    plantilla = []
    num_pleado = 0

    def __init__(self, nombre: str, cargo: str, salario=25000.50):
        if salario < 0:
            raise ValueError("El salario no puede ser cero")

        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        Empleado.plantilla.append(self)
        Empleado.num_pleado += 1

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def get_salario(self):
        return self.__salario

    def __str__(self):
        return f"{self.nombre} es un {self.cargo} y gana {self.get_salario()}"

empleado1 = Empleado("Juanma", "Director", 75000.0)
empleado2 = Empleado("Teresa", "Presidente", 80000.0)
empleado3 = Empleado("Ana", "Administrativo", 20000.0)

print(Empleado.plantilla)

num1 = 7
num2 = 7.0
num3 = 7.5

if Empleado.is_integer(num1):
    print(f"El numero {num1} es un entero")
else:
    print(f"El numero {num1} no es un entero")

if Empleado.is_integer(num2):
    print(f"El numero {num2} es un entero")
else:
    print(f"El numero {num2} no es un entero")

if Empleado.is_integer(num3):
    print(f"El numero {num3} es un entero")
else:
    print(f"El numero {num3} no es un entero")