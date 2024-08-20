from pathlib import Path
from zipfile import ZipFile

# creando un archivo comprimido
# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)


# leer un archivo comprimido
with ZipFile("archivos/comprimidos.zip") as zip:
    # este metodo namelist() nos permite ver todo el contenido del archivo zip
    # print(zip.namelist())
    info = zip.getinfo("archivos/06_comprimidos.py")
    print(info.file_size, info.compress_size)

    # de esta forma extraemos todo el archivo comprimido
    zip.extractall("archivos/descomprimidos")
