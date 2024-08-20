usuarios = [
    ["Sam", 3],
    ["Kemuel", 1],
    ["Ari", 7]
]

# forma común
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# haremos esto mismo de una forma eficientizada
# nombres = [expression for item in item] => usando esta forma del codigo
# esto se llama transformar = map
nombres = [usuario[0] for usuario in usuarios]

# esto es filtrar = filter
nombres = [usuario for usuario in usuarios if usuario[1] > 3]

# esto es transformar y filtrar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 1]

# VAMOS HACER LOS MISMOS PROCESOS DE LA COMPRESION DE LISTAS PERO CON LAS FUNCIONES CORRESPONDIENTE
nombres = list(map(lambda usuario: usuario[0], usuarios))  # map()

menosUsuarios = list(
    filter(lambda usuario: usuario[1] > 2, usuarios))  # filter

print(menosUsuarios)
