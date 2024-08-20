# Crear una función que identifique si una palabra es un palíndromo o no
# Implementar dos funciones una para eliminar los espacios del texto y otra para dar la vuelta al texto, luego llamar ambas funciones desde la funcion principal

def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves  # Esta linea de codigo lo que hace es tomar el indece actual y concatenarle luego con que esta almacenado en la variable texto_al_reves por esta razon el texto es invertido ya que el char siempre tomara la posicón cero del string
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print("Test")
print(es_palindromo("hola mundo"))
print(es_palindromo("somos o no somos"))
print(es_palindromo("Reconocer"))
print(es_palindromo("abba"))
