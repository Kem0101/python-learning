# la palabra reservada return nos permite almacenar y devolver el valor de una operacion en una variable y reutilizar dicho valor en otras funciones o en si misma
def suma(a, b):
    resultado = a + b
    return resultado


c = suma(3, 7)
d = suma(c, 12)
print(d)
