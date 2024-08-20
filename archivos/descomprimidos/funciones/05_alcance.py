# Utilizar variables globales se considera malas practicas, una de las principales razones es que pueden ocurrir cambio en el tipo de variable a lo largo del codigo.
# De ser necesario usar las variables globales por alguna razon se puede usar la palabra reservada global dentro de la funcion requerida

saludo = 20


def saludar():
    global saludo
    saludo = "Hola mundo"
    print(saludo)


def saludarTambien():
    saludo = "Hi bro"
    print(saludo)


saludar()
saludarTambien()
print(saludo)
