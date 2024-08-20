import sqlite3


with sqlite3.connect("sqlite/app.db") as con:

    cursor = con.cursor()  # siempre debo crear un cursor para poder ejecutar la consulta sql
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Jehova Dios eterno"),
    )

# porque pasamos la consulta como dos argumentos y no como un string formateados?
# esto es para evitar un ataque de SQL Injection que seria posible si creamos un insert creando la consulta como un string formateado, en values las propiedades las pasamos como signos de interrogación y los valores como otro algumento que sera una tupla
