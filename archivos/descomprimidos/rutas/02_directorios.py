from pathlib import Path


path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir() # para eliminar un directorio debe estar vacio
# path.rename("new_name")


# print(path.iterdir())  # este método iterdir() genera un objeto iterable a partir de un directorio
# for p in path.iterdir():
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
# recorrer y mostrar todos los archivos con dicha extensión
archivos = [p for p in path.glob("*.py")]
# recorrer y mostrar un archivo en concreto
archivos = [p for p in path.glob("01_*.py")]
# reccorer y mostrar todos los archivos en cualquier directorio dentro del directorio  padre que estemos trabajando y con dicha externsion
archivos = [p for p in path.glob("**/*.py")]
archivos = [p for p in path.rglob("*.py")]

print(archivos)
