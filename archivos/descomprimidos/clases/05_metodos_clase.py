class Perro():
    patas: int = 4

    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    # de esta forma convertimos este método en un metodo de la clase
    @classmethod
    def habla(cls):
        print("Jau jau jau!")

    # factory method
    @classmethod
    def factory(cls):
        return cls("Purrunguito", 1)


mi_perro = Perro.habla()
mi_perro2 = Perro.factory()
print(mi_perro2.name, mi_perro2.age)
