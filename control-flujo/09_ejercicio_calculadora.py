# strings
# Bienvenido a la calculadora
# Para salir escriba salir
# Las operaciones son, suma, multi, div, resta
# Ingresa numero, ingresa operacion, ingresa siguiente numero

# EJERCICIO: CALCULADORA
# SOLUCION:
# verificar si ya se ha ingresado un numero antes
# sino se ha ingresado ningun numero, ingresar numero
# si el usuario ya ha ingresa un numero entonces debe ingresar una operacion
# luego que el usuario ingrese una operacion, le vamos a pedir que ingrese el siguiente numero
# luego de ingresar el segun numero le vamos a mostrar el resultado
# luego dicho resultado lo guardaremos como el primer numero y le pedimos ingrese una nueva operacion y otro numero
# a este valor se le hara la operacion ultima operacion ingresada mas el ultimo numero ingresado

print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son, suma, multi, div y resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")

    print(f"El resultado es {resultado} ")
