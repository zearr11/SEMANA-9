from model.deportivo import Deportivo as carro
from model.camioneta import Camioneta
from model.minivan import Minivan

from poli.Entrenador import Entrenador
from poli.Futbolista import Futbolista
from poli.Masajista import Masajista
from poli.SeleccionFutbol import SeleccionFutbol

'''
objCarro = carro("Nissan","CH510","2020","100 km")

print(objCarro.description())

objCarro2 = carro("Tesla","Truck","2023","250 km")

print(objCarro2.description())
print(objCarro2.abastecerGAS())


camion = Camioneta("Chevrolet", "341SF","2026","100000")

print(camion.description())

objMinivan = Minivan("Toyota","KI122","2021","6")
print(objMinivan.description())
'''

objFutbolista = Futbolista("2503", "Cristiano", "Ronaldo", "38", 7, "Delantero")

#objFutbolista.MostrarDataFutbolista(objFutbolista)

print(objFutbolista.entrevista())