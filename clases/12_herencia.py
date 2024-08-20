class Animal:
    def comer(self):
        print("Esta comiendo")


class Perro(Animal):
    def caminar(self):
        print("Esta caminando")


class Paloma(Animal):
    def volar(self):
        print("Esta volando")


perro = Perro()
perro.comer()

paloma = Paloma()
paloma.volar()
