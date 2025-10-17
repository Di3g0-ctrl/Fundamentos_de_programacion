from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class Avion(Vehiculo):
    pass

# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
avion1 = Avion("Boeing", "Boeing Chinook", 2020, "Blanco")

#Otras instancias
auto2 = Auto("Honda", "Civic", 2015, "Rojo")
moto2 = Moto("Kawasaki", "Ninja", 2021, "Negra")
camion2 = Camion("Kenworth", "T200", 2019, "Rojo")
avion2 = Avion("Kenworth", "Mirage2000", 2020, "Blanco")


# Visualización
print(auto1)
print(moto1)
print(camion1)
print(avion1)