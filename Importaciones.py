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
    __lista = []
    def add(self, importacion):
        return self.__ejecutarSQL__('''INSERT INTO Importaciones (marca, productoNombre, codigo, codigoOrigen,
        precioSinIva, rubro) Values(:marca, :productoNombre, :codigo, :codigoOrigen,  :precioSinIva, :rubro)''',
                                    {"marca":importacion.marca, "productoNombre":importacion.productoNombre,
                                     "codigo":importacion.codigo,"codigoOrigen":importacion.codigoOrigen,
                                     "precioSinIva":importacion.precioSinIva, "rubro":importacion.rubro})
    def addl(self,importacion):
        self.__lista.append(importacion)


    def comit(self):
        self.autocomit=False
        for importacion in self.__lista:
            self.add(importacion)
        self.conexion.commit()
        self.__lista.clear()

    def rmAll(self):
        return self.__ejecutarSQL__('''DELETE From Importaciones''',None)

