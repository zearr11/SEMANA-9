
class SeleccionFutbol:
    
    def __init__(self, iD, nombre, apellidos, edad):
        self.__id = iD
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
    
    #CAMBIOS
    def set_iD(self, iD):
        self.__id = iD
    
    def set_nombres(self, nombre):
        self.__nombre = nombre
        
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def set_edad(self, edad):
        self.__edad = edad
    
    #ACCIONES  
    def viajar(self):
        return f"{self.__nombre} viaja."

    def concentrarse(self):
        return f"{self.__nombre} se concentra."
    
    def entrenamiento(self):
        return f"{self.__nombre} entrena."
    
    def partidoFutbol(self):
        return f"{self.__nombre} juega el partido de futbol."
    
    #MuestraDatos
    def MostrarData(self):
        print(f"ID : {self.__id}")
        print(f"Nombre : {self.__nombre}")
        print(f"Apellidos : {self.__apellidos}")
        print(f"Edad : {self.__edad}")