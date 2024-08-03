from model.vehiculo import Vehiculo

class Camioneta(Vehiculo):
    
    def __init__(self, marca, modelo, anio, capacidadMAX):
        super().__init__(marca, modelo, anio)
        self.capacidadMAX = capacidadMAX
        
    def description(self):
        return f"{super().description()}, CAPACIDAD MAX = {self.capacidadMAX}"