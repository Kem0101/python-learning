# Investigar acerca de inyeccion de dependencias

# en este ejemplo a continuacion lo que queremos hacer es importar todas las carpetas(paquetes) que estan dentro de rutas

# Generando una estructura de inyeccion de dependencias

from pathlib import Path
# import db
# import api
# import graphql

dependencias = {
    # "db": db,
    # "api": api,
    # "graphql": graphqls
}

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]


def load(p):
    paquete = __import__(str(p).replace("/", ".")) # es un método que nos permite importar paquetes de forma dinamica
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene función init")

list(map(load, paths))