# Nota: ejemplo de tipos de rustas en python

from pathlib import Path
# Asi seria una ruta en windows
Path(r"C:\Archivos de programa\minecraft")
# Ruta en Mac o Linux
# Path("/usr/bin")  # ruta absoluta
# Path()
# Path.home()
# Path("one/__init__.py")  # ruta relativa

path = Path("hola_mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.absolute()
)

# cambiar nombre de archivo y extension si se quiere
p = path.with_name("testing.py")
print(p)
p = path.with_suffix(".exe")  # cambiar extension
print(p)
p = path.with_stem("otro_nombre")  # cambiar nombre de archivo
print(p)
