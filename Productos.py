import sqlite3
from EntidadesGenerica import *

class Producto:
    def __init__(self, nombreProducto, idProducto):
        self.nombreProducto = nombreProducto
        self.idProducto = idProducto


class Productos(EntidadesGenerica):

    def add(self, producto):
        return self.__ejecutarSQL__('''INSERT INTO Productos (nombreProducto,idProducto,idMarca,IdRubro)
Values(:nombreProducto,:idProducto,:idMarca,:IdRubro)''', {"nombreProducto": producto.nombreProducto,
                                                           "idProducto": producto.idProducto,
                                                           "idMarca":producto.idMarca,
                                                           "IdRubro": producto.IdRubro})
    def rm(self, nombreProducto):
        return self.__ejecutarSQL__('''DELETE From Productos where nombreProducto=:nombreProducto''',
                              {"nombreProducto": nombreProducto})

    def rmAll(self):
        return self.__ejecutarSQL__('''DELETE From Productos''')

    def get(self, nombreProducto):
        cursor = self.conexion.cursor()
        cursor.execute(
            '''SELECT nombreProducto,idProducto,idMarca,IdRubro From Productos where nombreProducto=:nombreProducto''', {"nombreProducto": nombreProducto})
        registro = cursor.fetchone()
        if (registro):
            self.status = 1
            producto = Producto(registro['nombreProducto'], registro['idProducto'], registro['idProducto'], )
            return Producto
        else:
            self.status = 0
            return None
