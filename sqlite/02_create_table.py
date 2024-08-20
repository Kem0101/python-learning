import sqlite3


con = sqlite3.connect("sqlite/app.db")

cursor = con.cursor()  # siempre debo crear un cursor para poder ejecutar la consulta sql
cursor.execute(
    """
    create table if not exists usuarios
    (id int primary key, name varchar(50));
    """
)
con.commit()  # siempre debo comprometer la consulta a traves del objecto de la conexion

con.close()
