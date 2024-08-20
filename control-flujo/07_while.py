# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# loop infinito
comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() != "salir":  # si tenemos un loop infinito en este caso un while, podemos usar un if para dado una condición romper el bucle
        break
