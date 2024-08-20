# Nota: las razones por las que querria agregar una excepcion personalizada, puede ser para agregarle logica o valores que podrian sernos util despues

class MiError(Exception):
    "Esta es mi clase de error personalizada"

    def __init__(self, mensaje: str, codigo: int) -> None:
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self) -> str:
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por cero", 805)
    return 5 / 0


try:
    division()
except MiError as e:
    print(e)
