import os
from ManejaFacultades import ManejaFacultades
from Facultad import Facultad
from Carrera import Carrera

class Menu:
    __manejador = ManejaFacultades()
    __op = 0

    def __init__(self, op= 0):
        self.__op = op

    def opciones(self):
            self.__manejador.Carga()
            os.system("cls")
            continuar = True


            while continuar:
                print("[1] Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.")
                print("[2] Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.")
                print("[0] Para salir del menu")
                self.__op = int(input("INGRESE OPCION\n"))
                os.system("cls")

                if(self.__op == 1):
                    self.__manejador.buscarFacultad()

                # elif(self.__op ==2):

                elif(self.__op == 0):
                    continuar = not continuar
                    print("PROGRAMA FINALIZADO")
                else: 
                    print("Opcion incorrecta, ingrese nuevamente")