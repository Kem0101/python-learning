# Es importante tener en cuenta que la hora de realizar loops anidados en bases de datos grande esta deberia ser la ultima alternativa ya que consumira muchos recursos e se tomara bastante tiempo realizar esta operacion en miles o millones de datos

for j in range(3):  # outer for loop
    for k in range(2):  # inner for loop
        print(f"{j}, {k}")
