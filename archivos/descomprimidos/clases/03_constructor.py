class Perro():
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    def habla(self):
        print(f"{self.name} labra: Jau jau jau!")


mi_perro = Perro("Flopi", 1)
mi_perro.habla()
