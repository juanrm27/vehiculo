class Vehiculo():
    color = 'blanco'

    def __init__(self, nombre = "", velocidad_maxima = 0, kilometraje = 0) -> None:
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Velocidad Max: {self.velocidad_maxima},Kilometraje:{self.kilometraje}'

class Bus(Vehiculo):
    
    def set_capacidad(self, new_capacidad=50):
        self.capacidad = new_capacidad
