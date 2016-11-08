from Importaciones import Importaciones,Importacion


Importaciones("imperdiel.db").rmAll()
f = open("BaseDatos\\B-52")
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
        Importaciones("imperdiel.db").add(importacion)
        indice = -1
    indice += 1

f.close()