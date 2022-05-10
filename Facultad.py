from Carrera import Carrera

class Facultad: 
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carrera = None

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carrera = []
    
    def mostrarFacultad(self):
        print("Codigo: {}\nNombre: {}\nDireccion: {}\nLocalidad: {}\nTelefono: {}\n".format(self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono))
        for i in self.__carrera:
            print("----------------------")
            i.__str__()
    
    def agregarCarrera(self, codigoc, nombrec, fecha_inicio, duracion, titulo):
        self.__carrera.append(Carrera(codigoc, nombrec, fecha_inicio, duracion, titulo))

    def getCodigoFacultad(self):
        return self.__codigo
    
    def getNombreFacultad(self):
        return self.__nombre
    
    def getCarreras(self):
        return self.__carrera
    
