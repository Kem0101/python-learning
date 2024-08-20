try:
    n1 = int(input("Ingrese el primer numero: "))

except Exception as e:
    print("Ingrese un valor que corresponda")

# existen dos bloques mas que podemos tener en cuando a excepciones
else:
    print("Solo se ejecuta si no hay ningun error")

finally:
    print("Este bloque se ejecutara siempre haya o no errores")
