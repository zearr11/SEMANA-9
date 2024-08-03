from poli.SeleccionFutbol import SeleccionFutbol

class Futbolista(SeleccionFutbol):
    
    def __init__(self, iD, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(iD, nombre, apellidos, edad)
        self.__dorsal = dorsal
        self.__demarcacion = demarcacion
    
    #METODO
    def entrevista(self):
        return f"A {self.__nombre} se le entrevista."
    
    def partidoFutbol(self):
        return f"Estadio Monumental"

    #CAMBIOS
    def set_dorsal(self, dorsal):
        self.__dorsal = dorsal
        
    def set_demarcacion(self, demarcacion):
        self.__demarcacion = demarcacion
        
    def MostrarDataFutbolista(self):
        super().MostrarData()
        print(f"Dorsal : {self.__dorsal}")
        print(f"Demarcacion : {self.__demarcacion}")
        