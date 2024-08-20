class Perro():
    patas: int = 4

    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    def habla(self):
        print(f"{self.name} labra: Jau jau jau!")


# Dentro de la misma clase se puede redefinir el valor de una propiedad de la clase
# Perro.patas = 3

mi_perro = Perro("Flopi", 1)
# Tambien puedo cambiar el valor de una propiedad de la clase concretamente en una instancia
mi_perro.patas = 5
# mi_perro.habla()
print(mi_perro.patas)
