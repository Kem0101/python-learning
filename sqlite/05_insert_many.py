import sqlite3


with sqlite3.connect("sqlite/app.db") as con:

    cursor = con.cursor()  # siempre debo crear un cursor para poder ejecutar la consulta sql
    usuarios = [
        (2, "Jesus Cristo señor nuestro"),
        (3, "Espiritu santo de Dios")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )

# para insertar un conjunto de datos debemos crear una lista de tuplas y luego pasarla como segundo parametro en la consulta
