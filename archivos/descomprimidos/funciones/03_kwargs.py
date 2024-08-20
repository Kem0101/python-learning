def get_product(**datos):  # la sintaxis ** mas el parametro le dice a python que estamos pasando un keyword argument y que este es iterable
    print(datos["id"], datos["name"])


get_product(id="id", name="Iphone", marca="apple")
