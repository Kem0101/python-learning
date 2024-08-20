# Al crear una clase debemos usar la convencion upper camel case
class Perro():
    def habla(self):
        print('Jau jau jau!')


mi_perro = Perro()
mi_perro.habla()
# Verificar si un método pertenece a una clase
print(isinstance(mi_perro, Perro))
