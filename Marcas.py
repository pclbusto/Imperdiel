import sqlite3

class Marca:
    def __init__(self,nombre, idMarca):
        self.nombre = nombre
        self.idMarca = idMarca


class Marcas:
    def __init__(self):
        self.conexion = sqlite3.connect('imperdiel.db')
        self.conexion.row_factory = sqlite3.Row
        self.status = 1

        def add(self, marca):
            c = self.conexion.cursor()
            c.execute('''INSERT INTO Marcas (nombre,idMarca)
    Values(:nombre,:idMarca)''', {"nombre":marca.nombre,"idMarca":marca.idMarca})
            self.conexion.commit()

        def rm(self, nombre):
            cursor = self.conexion.cursor()
            cursor.execute('''DELETE From Marcas where nombre=:nombre''', {"nombre":nombre})
            self.conexion.commit()

        def rmAll(self):
            cursor = self.conexion.cursor()
            cursor.execute('''DELETE From Marcas''')
            self.conexion.commit()

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
