import csv
from Facultad import Facultad
from Carrera import Carrera
import re
class ManejaFacultades:
    __lista = None

    def __init__(self):
        self.__lista = []
    
    def agregarFacultad(self, unaFacultad):
        self.__lista.append(unaFacultad)

    def Carga(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if len(fila) == 5:
                codigo=int(fila[0])
                nombre=fila[1]
                direccion=fila[2]
                localidad=fila[3]
                telefono=fila[4]
                facultad=Facultad(codigo,nombre,direccion,localidad,telefono)
                self.agregarFacultad(facultad)
            if len(fila) == 6:
                codigoc=int(fila[0])
                nombrec=fila[1]
                fecha_inicio=fila[2]
                duracion=fila[3]
                titulo=fila[4]
                facultad.agregarCarrera(codigoc,nombrec,fecha_inicio,duracion,titulo)
        archivo.close()
    
    def mostrarLista(self):
        for facultad in self.__lista:
            print("----------------------")
            facultad.mostrarFacultad()

    def buscarFacultad(self):
        codigo = int(input("Ingrese el codigo de la facultad: "))
        i=0
        band=False
        while ((i<(len(self.__lista))) and band==False):
            if (codigo==self.__lista[i].getCodigoFacultad()):
                band=True
                print("\nNombre de la facultad: {}".format(self.__lista[i].getNombreFacultad()))
                for carrera in self.__lista[i].getCarreras():
                    print("Carrera: {}".format(carrera.getNombreCarrera()))
                    print("Duracion: {}".format(carrera.getDuracion()))
                    # carrera.mostrarCarrera()
            i+=1
    
    