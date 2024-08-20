# Nota: Importante! no se deberia lanzar excepciones muy seguidos porque son costosa en rendimientos
# Tambien podemos personalizar las excepciones

def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5 / 0


try:
    division()
except ZeroDivisionError as e:
    print(e)
