if __name__ != "__main_":
    from usuarios.metodos.crud import guardar  # importacion absoluta
    from ..metodos.crud import guardar  # importacion relativa

    print(__name__)

    def pagar_impuestos():
        print("Pagando Impuestos")
        guardar()


if __name__ == "__main__":
    print("Ejecutar tarea de mantenimiento")
