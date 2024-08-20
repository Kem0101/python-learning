# LAS TUPLAS SON UN TIPO DE DATOS QUE NO PUEDEN SER MODIFICADOS PERO SI PUEDES CREAR OTRA TUPLA A PARTIR DE LA ORIGINAL

numeros = (1, 2, 3) + (4, 5, 6, 7)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)


listaNumeros = list(numeros)
listaNumeros[0] = 'Jehova'
print(listaNumeros)
