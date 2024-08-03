from poli.SeleccionFutbol import SeleccionFutbol

class Entrenador(SeleccionFutbol):
    
    def __init__(self, iD, nombre, apellidos, edad, idFederacion):
        super().__init__(iD, nombre, apellidos, edad)
        self.__idFederacion = idFederacion
    
    #METODO
    def planificar(self):
        return f"{self.__nombre} planifica."
    
    #CAMBIO
    def set_idFeracion(self, idFederacion):
        self.__idFederacion = idFederacion
        
    def MostrarDataEntrenador(self):
        print(f"idFederacion : {self.__idFederacion}")
        super().MostrarData()
        