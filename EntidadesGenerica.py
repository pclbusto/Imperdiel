import sqlite3

class EntidadesGenerica:
    def __init__(self,nombreBD):
        self.conexion = sqlite3.connect(nombreBD)
        self.conexion.row_factory = sqlite3.Row
        self.status = 1

    def __ejecutarSQL__(self, script, parametros):
        c = self.conexion.cursor()
        status = 0
        try:
            if parametros:
                c.execute(script, parametros)
            else:
                c.execute(script)
        except sqlite3.Error as er:
            print(er)
            status = 1
        self.conexion.commit()
        return status