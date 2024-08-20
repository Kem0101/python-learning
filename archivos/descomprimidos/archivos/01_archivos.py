from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# con este método podemos ver algunas estadisticas relacionada al archivo
# print(archivo.stat())


# con este método podemos usar el otro método ctime para darle mayor legibilidad
print("Acceso", ctime(archivo.stat().st_atime))
print("Creacion", ctime(archivo.stat().st_ctime))
print("Modificacion", ctime(archivo.stat().st_mtime))
