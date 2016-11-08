from Importaciones import Importaciones,Importacion
from pathlib import Path,PureWindowsPath

p = Path("BaseDatos")
importaciones = Importaciones("imperdiel.db")
importaciones.rmAll()

for x in p.iterdir():
    if x.is_file():
        # and x.name<"ACAU":
        print("BaseDatos\\"+x.name)
        f = open("BaseDatos\\"+x.name)
        indice = 0
        for line in f.readlines():
            if indice == 0:
                 importacion = Importacion()
                 importacion.marca = f.name[10:]
                 importacion.codigo = line[:-1]

            if indice == 1:
                importacion.productoNombre = line[:-1]

            if indice == 2:
                importacion.codigoOrigen= line[:-1]

            if indice == 3:
                importacion.precioSinIva= line[:-1]

            if indice == 4:
                importacion.rubro = line[:-1]
                importaciones.addl(importacion)
                indice = -1
            indice += 1
        f.close()
        importaciones.comit()

