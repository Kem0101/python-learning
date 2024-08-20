# Investigar un poco mas acerca de la anulación de métodos

class Ave:
    def __init__(self) -> None:
        self.volador = "volador"

    def vuelva(self):
        print("vuella ave")


class Pato(Ave):
    def __init__(self) -> None:
        super().__init__()
        self.nada = "nadador"

    def vuelva(self):
        print("vuela pato")


pato = Pato()
pato.vuelva()
print(pato.volador, pato.nada)
