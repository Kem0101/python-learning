# Nota: puedo crear una clase e instancias del mismo y luego pasarlos como parametros al instanciar el objeto de otra clase (a esto se le llama contenedores)

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre: str, productos: list) -> None:
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto: str):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


zapatilla = Producto("Huarache Elite", 7000)
casco = Producto("Rauling", 2000)
guante = Producto("Rauling", 12000)

deportes = Categoria("Deporte", [zapatilla, casco])
deportes.agregar(guante)
deportes.imprimir()
