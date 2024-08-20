class Model():
    tabla = False

    def __init__(self) -> None:
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardar {self.tabla} en BD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscar por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(7)
