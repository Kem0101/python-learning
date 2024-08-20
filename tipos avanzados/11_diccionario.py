punto = {"x": 25, "y": 30}
print(punto)
print(punto["x"])
print(punto["y"])

punto["x"] = 45
print(punto)
# print(punto, punto["lala"])

if "lala" in punto:
    print("Encontre lala", punto["lala"])

print(punto.get("x"))
# si la clave no existe devuelve none pero tambien puedo pasarle un valor por default a una llave que no existe, usando el metodo get
print(punto.get("lala", 100))
del punto["x"]
del (punto["y"])
print(punto)

punto["x"] = 25
punto["y"] = 45

for valor in punto:  # esta forma devuelve cada llave con su valor
    print(valor, punto[valor])

for valor in punto.items():  # esta forma devuelve tuplas
    print(valor)

for llave, valor in punto.items():  # esta forma devuelve tuplas y podemos desempaquetarla(destructurarla)
    print(llave, valor)


# NOTA: VEREMOS UN EJEMPLO MAS REALISTA DEL USO DE DICCIONARIO
usuarios = [
    {"id": 1, "nombre": "Sam"},
    {"id": 2, "nombre": "Ari"},
    {"id": 3, "nombre": "Kemuel"},
    {"id": 4, "nombre": "Keylin"},
    {"id": 5, "nombre": "Saray"}
]

for usuario in usuarios:
    print(usuario["nombre"])
