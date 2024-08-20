persona = "  Kemuel Martinez  "

print(persona.upper())
print(persona.lower())
print(persona.strip().capitalize())
print(persona.title())
print(persona.strip())  # elimina los espacios en blanco a ambos lados
print(persona.lstrip())  # elimina los espacios en blanco a la izquierda
print(persona.rstrip())  # elimina los espacios en blanco a la derecha
# hace una busqueda entro del string y nos devuelve el indice donde se encuentra la cadena de texto especificada
print(persona.find("el"))
print(persona.replace("uel", ""))
# en estos dos próximos métodos hacemos una busqueda de los caracteres especificados dentro del string y devuelve un boolean
print("el" in persona)
print("el" not in persona)
