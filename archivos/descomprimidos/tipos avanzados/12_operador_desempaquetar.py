# El operador para desempaquetar es el * nos permite pasar cada valor de una lista como un valor individual, tambien nos permite unir listas asignando el operador delante de cada lista

lista1 = [1, 2, 3, 4]
print(lista1)
print(*lista1)

lista2 = [5, 6, 7]

combinar = [*lista1, *lista2]
print(combinar)


punto1 = {"x": 45}
punto2 = {"y": 90}

nuevoPunto = {**punto1, **punto2, "z": 60}
print(nuevoPunto)
