mascotas = ["Wilo", "Purungo", "Flopi", "Chocolo"]
print(mascotas[0])  # acceder por su índice
mascotas[2] = "Bipli"  # reasignar valor por su índice
print(mascotas)
print(mascotas[2:])  # acceder desde el índice indicado a toda la longitud
# acceder desde el inicio hasta la cantidad de posiciones indicadas
print(mascotas[:2])
print(mascotas[-1])  # acceder al ultimo elemento de la lista
# acceder desde la posición 1 y saltando una posición (o sea de dos en dos)
print(mascotas[1::2])
# podemos asignar un valor dentro de los dos puntos para decir hasta cuantos elementos queremos asignar
print(mascotas[1:2:2])


numeros = list(range(21))
print(numeros[::2])  # acceder a los numeros pares
print(numeros[1::2])  # acceder a los numeros impares
