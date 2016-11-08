import sqlite3
from EntidadesGenerica import *

class Rubro:
    def __init__(self,nombreRubro, idRubro):
        '''
        :param nombreRubro: nombre del rubro
        :param idRubro: este id representa el id de la base de datos. Si se intenta guardar un rubro nuevo. Este campo
        puede tener un volor o no. El id se calcula al momento de insertar.
        '''
        self.nombreRubro = nombreRubro
        self.idRubro = idRubro


class Rubros(EntidadesGenerica):

    def add(self, rubro):
        return self.__ejecutarSQL__('''INSERT INTO Rubros (nombreRubro)
            Values(:nombreRubro)''', {"nombreRubro":rubro.nombreRubro})
    def rm(self, nombreRubro):
        return self.__ejecutarSQL__('''DELETE From Rubros where nombreRubro=:nombreRubro''', {"nombreRubro":nombreRubro})

    def rmAll(self):
        return self.__ejecutarSQL__('''DELETE From Rubros''')

    def get(self, nombreRubro):
        cursor = self.conexion.cursor()
        cursor.execute(
            '''SELECT nombreRubro,idRubro From Rubros where nombreRubro=:nombreRubro''', {"nombreRubro":nombreRubro})
        registro = cursor.fetchone()
        if (registro):
            self.status = 1
            rubro = Rubro(registro['nombreRubro'], registro['idRubro'])
            return rubro
        else:
            self.status = 0
            return None
