class Perro():
    def __init__(self, nombre):
        self.nombre = nombre

    # el decorador property convierte un método en una propiedad y esta solo se debe usar con los metodos que nos devuelven los valores osea los getter,
    # property va a asignar un decorador al método que le hayamos asignado y luego podremos usar dicho método como decorador del método setter
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Purrungo")
print(perro.nombre)
