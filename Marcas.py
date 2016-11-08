import sqlite3
from EntidadesGenerica import *

class Marca:
    def __init__(self,nombre, idMarca):
        self.nombre = nombre
        self.idMarca = idMarca


class Marcas(EntidadesGenerica):

    def add(self, marca):
        return self.__ejecutarSQL__('''INSERT INTO Marcas (nombre,idMarca)
        Values(:nombre,:idMarca)''', {"nombre":marca.nombre,"idMarca":marca.idMarca})

    def rm(self, nombre):
        return self.__ejecutarSQL__('''DELETE From Marcas where nombre=:nombre''', {"nombre":nombre})

    def rmAll(self):
        return self.__ejecutarSQL__('''DELETE From Marcas''')

    def get(self, nombre):
        cursor = self.conexion.cursor()
        cursor.execute(
            '''SELECT nombre,idMarca From Marcas where nombre=:nombre''', {"nombre":nombre})
        registro = cursor.fetchone()
        if (registro):
            self.status = 1
            marca = Marca(registro['nombre'], registro['idMarca'])
            return marca
        else:
            self.status = 0
            return None
