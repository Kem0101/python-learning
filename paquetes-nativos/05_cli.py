import os
import sys
from pathlib import Path

# print(sys.argv)


def cli(args):
    if len(args) == 1:
        print("No se le pasaron argumentos")
        return
    if len(args) != 3:
        print("Se requieren 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("Ya hay un archivo con este nombre")
        return

    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito")


cli(sys.argv)
