# Nota: no deberia de importar todo lo que contiene el archivo al que estoy invocando usando * es una mala practica y de hacerlo que no deberia habria que llamar los métodos y propiedades arriba antes de defenir cualquier función o método que se llame igual

# una forma de importar es esta
from usuarios.impuestos.utilidades import pagar_impuestos
# otra opcion es
# from usuarios.metodos import acciones

# dir nos permite ver los método magicos y paquetes disponibles
# import usuarios
# print(usuarios.__name__)
# print(usuarios.__package__)
# print(usuarios.__path__)
# print(usuarios.__file__)

pagar_impuestos()


# investigar acerca del dinamismo del nombre de los paquetes en python y su función
