import sqlite3

# de esta forma no necesito ni comprometer mi consulta commit() ni cerrar mi conexion close() porque ahora mi objecto con contiene el método __exit__ y dicho objecto sino hay ningun error en la consulta tambien llama a close()
with sqlite3.connect("sqlite/app.db") as con:

    cursor = con.cursor()  # siempre debo crear un cursor para poder ejecutar la consulta sql
    cursor.execute(
        """
        create table if not exists usuarios
        (id int primary key, name varchar(50));
        """
    )
