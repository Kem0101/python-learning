import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lista)  # cambiar el orden aleatoriamente a una lista

print(
    # random.random(),  # genera una cadena de numeros desde cero a uno
    # # genera una cadena de numeros desde hasta segun los valores que le pasemos
    # random.randint(1, 10),
    # lista,
    random.choice(lista),  # elegir un numero aleatorio de un listado
    random.choices(lista, k=3),
    "".join(random.choices("abcdefghi,123", k=3))
)

# crear secuencia de caracteres aleatorios que podrian ser usados como contraseñas
chars = string.ascii_letters
digitos = string.digits

seleccion = random.choices(chars + digitos, k=16)
# print(seleccion)
password = "".join(seleccion)
print(password)
