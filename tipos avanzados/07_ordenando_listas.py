numeros = [3, 7, 12, 24, 10, 32, 90]

# numeros.sort()
numeros.sort(reverse=True)
# La diferencia entre sort y sorted es que sorted crea una nueva lista
numOrdenado = sorted(numeros, reverse=True)
print(numOrdenado)


# Ordenar matrices

# Si la lista contiene como primer valor un ordenable como en este caso entonces sort de la forma normal puede ordenar correctamente
usuarios = [
    [3, "Sam"],
    [1, "Kemuel"],
    [7, "Ari"]
]

usuarios = [
    ["Sam", 3],
    ["Kemuel", 1],
    ["Ari", 7]
]


# def ordenar(elemento):
# return elemento[1]

# usuarios.sort(key=ordenar)  # Esta no es la mejor forma de hacer este proceso

# vamos hacer los mismo que la función anterior pero con una función lambda
# la función lambda en python sobre entiende que va actuar sobre la lista a la que se le aplica el metodo sort() en este caso, recibiendo esta los parametros:valorDeRetorno
usuarios.sort(key=lambda el: el[1])
print(usuarios)
