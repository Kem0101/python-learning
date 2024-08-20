class Perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Este es un método magico de python
    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: jau jau jau!")


perro = Perro("Purrungo", 2)
print(perro)
