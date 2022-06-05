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
                codigoc=int(fila[1])
                nombrec=fila[2]
                titulo=fila[3]
                duracion=fila[4]
                facultad.agregarCarrera(codigoc,nombrec,duracion,titulo)
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
    
    def buscarCarrera(self, nombreCarrera: str):
        
        band = False
        unaCarrera = None
        unaFacultad = None
        i=0
        while not band and i<len(self.__lista):
            unaFacultad: Facultad=self.__lista[i]
            carreras = unaFacultad.getCarreras()
            j=0
            while not band and j<len(carreras):
                if carreras[j].getNombreCarrera().lower()==nombreCarrera.lower():
                    band = True
                j += 1
            
            i += 1
        if band:
            unaFacultad = self.__lista[i-1]
            unaCarrera: Carrera = self.__lista[i-1].getCarreras()[j-1]
        return (unaFacultad, unaCarrera)

    def mostrarCarrera(self, nombreCarrera):
        unaFacultad, unaCarrera = self.buscarCarrera(nombreCarrera)
        if unaFacultad!=None and unaCarrera!= None:
            print("Codigo: {}-{}\nNombre: {}\nLocalidad: {}\n".format(unaFacultad.getCodigoFacultad(), unaCarrera.getCodigoCarrera(), unaFacultad.getNombreFacultad(), unaFacultad.getLocalidad()))
        else:
            print("[ERROR] No se encontró la carrera.")

