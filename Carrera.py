class Carrera:
    __codigoc = 0
    __nombrec = ""
    __duracion = 0
    __titulo = ""

    def __init__(self, codigo, nombre, duracion, titulo):
        self.__codigoc = codigo
        self.__nombrec = nombre
        self.__titulo = titulo
        self.__duracion = duracion

    
    def mostrarCarrera(self):
        return "Codigo: {}\nNombre: {}\nDuracion: {}\nTitulo: {}\n".format(self.__codigoc, self.__nombrec, self.__duracion, self.__titulo)
    
    def getCodigoCarrera(self):
        return self.__codigoc
    
    def getNombreCarrera(self):
        return self.__nombrec
    
    def getDuracion(self): 
        return self.__duracion

