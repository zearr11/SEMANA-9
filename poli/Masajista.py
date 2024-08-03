from poli.SeleccionFutbol import SeleccionFutbol

class Masajista(SeleccionFutbol):
    
    def __init__(self, iD, nombre, apellidos, edad, titulacion, aniosExperiencia):
        super().__init__(iD, nombre, apellidos, edad)
        self.__titulacion = titulacion
        self.__aniosExperiencia = aniosExperiencia
        
    #METODO
    def darMasaje(self):
        return f"{self.__nombre} da un masaje"

    #CAMBIO
    def set_titulacion(self, titulacion):
        self.__titulacion = titulacion
        
    def set_aniosExp(self, aniosExp):
        self.__aniosExperiencia = aniosExp
       
    def MostrarDataMasajista(self):
        super().MostrarData()
        print(f"Titulacion : {self.__titulacion}")
        print(f"Años de experiencia : {self.__aniosExperiencia}")