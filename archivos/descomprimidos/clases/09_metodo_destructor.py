class Perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Este es un método magico de python para eliminar un objecto llamado(destructor)
    def __del__(self):
        print(f"Bye perrito: {self.nombre}")

    def habla(self):
        print(f"{self.nombre} de {self.edad} años dice: jau jau jau!")


perro = Perro("Purrungo", 2)
del perro
