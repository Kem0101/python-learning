import csv
import os

# escribir
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow(["10", "1", "Aprendiendo a trabajar archivos csv"])
#     writer.writerow(["11", "2", "Python es genial"])


# leer
# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     # de esta forma me imprime la lista pero el puntero va al final de la lista osea no podria volverlo a leer desde la primera linea
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)


# actualizar CSV
# with open("archivos/archivo.csv",) as r, open("archivos/archivo_temp.csv", "w") as w:
#     reader = csv.reader(r)
#     writer = csv.writer(w)
#     for linea in reader:
#         if linea[0] == "10":
#             writer.writerow([10, 1, "Texto actualizado 2"])
#         else:
#             writer.writerow(linea)
#     os.remove("archivos/archivo.csv")
#     os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
