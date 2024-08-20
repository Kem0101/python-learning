mascotas = ["Purrungo", "Wilo", "Flopi", "Chocolo",
            "Bartolito", "Wilo", "Parcheron", "Chacho"]

mascotas.insert(1, "Tiri")
mascotas.append("Vaca lola")
print(mascotas)

mascotas.remove("Wilo")
mascotas.pop()  # el metodo pop() elimina por default el ultimo elemento y en su defecto el indice que le pasemos
del mascotas[1]
mascotas.clear()
print(mascotas)
