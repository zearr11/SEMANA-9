
class Vehiculo:
    
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def description(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio}"
    
    def abastecerGAS(self):
        return "Carga minima 3 galones"
    