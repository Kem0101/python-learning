from abc import ABC, abstractstaticmethod


class Model(ABC):
    # En esta implementación no necesito crear un constructor
    # Tambien podriamos hacer que un método de esta clase sea abstracto
    @property
    @abstractstaticmethod
    def tabla(self):
        pass

    def guardar(self):
        print(f"Guardar {self.tabla} en BD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscar por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.buscar_por_id(7)
