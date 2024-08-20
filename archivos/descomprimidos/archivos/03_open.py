from io import open


# texto = "Conociendo open"


# escritura
# archivo = open("archivos/archivo-prueba.txt", "w")
# archivo.write(texto)
# archivo.close()


# lectura
# archivo = open("archivos/archivo-prueba.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista(lee el texto por cada linea y devuelve un array cada linea es un string)
# archivo = open("archivos/archivo-prueba.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# with open("archivos/archivo-prueba.txt", "r") as archivo:
#     # esto descarga todo el archivo en memoria y lo lee
#     print(archivo.readlines())
#     # seek() para hacer que el puntero vuelva al caracter que le indiquemos
#     archivo.seek(0)
#     for linea in archivo:  # de esta manera vamos leyendo linea por linea
#         print(linea)


# agregar
# archivo = open("archivos/archivo-prueba.txt", "a+")
# archivo.write("Agregando texto nuevo")
# archivo.close()

# texto = ''
# lectura y escritura
# with open("archivos/archivo-prueba.txt", "r+") as archivo:
#     texto = archivo.readlines()
#     archivo.seek(0)
#     texto[0] = "Mi primera linea"
#     print(texto)
#     archivo.writelines(texto)
