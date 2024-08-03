from model.vehiculo import Vehiculo


class Minivan(Vehiculo):
    def __init__(self, marca, modelo, anio, n_pasajeros):
        super().__init__(marca, modelo, anio)
        self.n_pasajeros = n_pasajeros
        
    def description(self):
        return f"{super().description()}, Numero Pasajeros = {self.n_pasajeros}"