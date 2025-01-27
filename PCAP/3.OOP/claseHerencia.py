# Crear una clase reptil que reciba un nombre como argumento
class Reptil:
    def __init__(self, nombre):
        self.nombre = nombre

class Serpiente(Reptil):
    pass

class Culebra(Serpiente):
    pass

print(f"\t\t{Reptil.__name__}\t{Serpiente.__name__}\t{Culebra.__name__}")

#comprobar si los objetos son de cierta clase
reptil1= Reptil("Rana")
reptil2= Reptil("Víbora")
reptil3= Reptil("Cocodrilo")

for obj in[reptil1,reptil2,reptil3 ]:
    print(obj.nombre, end=" \t")
    for clase in[Reptil,Serpiente,Culebra]:
        print(isinstance(obj,clase), end=" \t")

print()

reptil1= reptil2
reptil2 = reptil3

print(reptil1 == reptil2, reptil2 is reptil1)
print(reptil2 == reptil3, reptil2 is reptil2)
print(Reptil == reptil3, reptil1 is reptil3)


for clas1 in [Reptil, Serpiente, Culebra]:
    print(clas1.__name__, end=' \t')
    for clas2 in [Reptil, Serpiente, Culebra]:
        print(issubclass(clas1, clas2), end='\t')
    print()
print()

reptil1 = Reptil("lagarto")
print(reptil1.nombre)

reptil2 = Serpiente("Manba_negra")
print(type(Serpiente).__name__)

reptil3= Culebra("culebra_ibérica")
print(type(Culebra).__name__)

print("Verificar si Culebra es subclase de Serpiente:")
print(issubclass(Culebra, Serpiente))

print("Verificar el tipo de reptil2:")
print(type(reptil2).__name__)