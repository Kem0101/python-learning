def suma(*numeros):  # esta sintaxis de * y el nombre de parametros convierte nuestros paramatros en iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 3, 4)
suma(2, 3, 7, 1)
suma(5, 3, 7, 5)
