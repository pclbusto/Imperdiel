import sqlite3
from EntidadesGenerica import *

class Importacion:
    def __init__(self,marca, productoNombre,codigo,codigoOrigen,precioSinIva,rubro):
       
        self.marca = marca
        self.productoNombre = productoNombre
        self.codigo = codigo
        self.codigoOrigen = codigoOrigen        
        self.precioSinIva = precioSinIva
        self.rubro = rubro
    def __init__(self):
        self.marca = ""
        self.productoNombre = ""
        self.codigo = 0
        self.codigoOrigen = ""
        self.precioSinIva = 0
        self.rubro = ""

class Importaciones(EntidadesGenerica):

    def add(self, importacion):
        return self.__ejecutarSQL__('''INSERT INTO Importaciones (marca, productoNombre, codigo, codigoOrigen,
        precioSinIva, rubro) Values(:marca, :productoNombre, :codigo, :codigoOrigen,  :precioSinIva, :rubro)''',
                                    {"marca":importacion.marca, "productoNombre":importacion.productoNombre,
                                     "codigo":importacion.codigo,"codigoOrigen":importacion.codigoOrigen,
                                     "precioSinIva":importacion.precioSinIva, "rubro":importacion.rubro})
    def rmAll(self):
        return self.__ejecutarSQL__('''DELETE From Importaciones''',None)

