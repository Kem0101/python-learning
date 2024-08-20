# Nota: si vamos a usar la herencia multiple entonces tenemos que acudir a la practica de tener clases pequeñas donde ninguna clase tenga métodos repetidos

class Caminar:
    def camina(self):
        print("Esta cominando")


class Volar:
    def vuela(self):
        print("Esta valando")


class Nadar:
    def nada(self):
        print("Esta nadando")


class Pato(Caminar, Volar, Nadar):
    def movilidad(self):
        print("Se esta trasladando")


pato = Pato()
pato.camina()
