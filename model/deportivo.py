from model.vehiculo import Vehiculo

class Deportivo (Vehiculo):
    
    def __init__(self, marca, modelo, anio, velocidadMAX):
        super().__init__(marca, modelo, anio)
        self.velocidadMax = velocidadMAX
        
    def description(self):
        return f"{super().description()}, Velocidad Max: {self.velocidadMax}"