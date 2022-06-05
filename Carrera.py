class Carrera:
    __codigoc = 0
    __nombrec = ""
    __fecha_inicio = ""
    __duracion = 0
    __titulo = ""

    def __init__(self, codigo, nombre, fecha_inicio, duracion, titulo):
        self.__codigoc = codigo
        self.__nombrec = nombre
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__titulo = titulo
    
    def mostrarCarrera(self):
        return "Codigo: {}\nNombre: {}\nFecha de inicio: {}\nDuracion: {}\nTitulo: {}\n".format(self.__codigoc, self.__nombrec, self.__fecha_inicio, self.__duracion, self.__titulo)
    
    def getCodigoCarrera(self):
        return self.__codigoc
    
    def getNombreCarrera(self):
        return self.__nombrec
    
    def getDuracion(self): 
        return self.__duracion

