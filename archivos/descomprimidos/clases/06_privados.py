class Perro():
    def __init__(self, name, age):
        # con la doble guion bajo convierto la propiedad a privada
        self.__name: str = name
        self.age: int = age

    def get_nombre(self):
        return self.__name

    def set_nombre(self, name):
        self.__name = name

    def habla(self):
        print(f"{self.__name} con edad {self.age} año y dice: Jau jau jau!")

    # factory method
    @classmethod
    def factory(cls):
        return cls("Purrunguito", 1)


perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
# con este comando obtenemos todos los metodos de una instancia
# print(perro1.__dict__)
# de esta forma accedemos a los metodos privido de una clase(no deberiamos hacer esta practica)
# print(perro1._Perro__name)
