import sqlite3


class Producto:
    def __init__(self, nombreProducto, idProducto):
        self.nombreProducto = nombreProducto
        self.idProducto = idProducto


class Productos:
    def __init__(self):
        self.conexion = sqlite3.connect('imperdiel.db')
        self.conexion.row_factory = sqlite3.Row
        self.status = 1

        def add(self, producto):
            c = self.conexion.cursor()
            c.execute('''INSERT INTO Productos (nombreProducto,idProducto,idMarca,IdRubro)
    Values(:nombreProducto,:idProducto,:idMarca,:IdRubro)''', {"nombreProducto": producto.nombreProducto,
                                                               "idProducto": producto.idProducto,
                                                               "idMarca":producto.idMarca,
                                                               "IdRubro": producto.IdRubro})
            self.conexion.commit()

        def rm(self, nombreProducto):
            cursor = self.conexion.cursor()
            cursor.execute('''DELETE From Productos where nombreProducto=:nombreProducto''', {"nombreProducto": nombreProducto})
            self.conexion.commit()

        def rmAll(self):
            cursor = self.conexion.cursor()
            cursor.execute('''DELETE From Productos''')
            self.conexion.commit()

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
