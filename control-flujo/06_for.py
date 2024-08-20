"""for loop"""

id = 12
for numero in range(7):
    if numero == id:
        print("Este es el id", id)
        break

else:
    print("Este usuario no existe")


# iterables: range(), list, strings
# ejemplo con string
for char in "Jehova es mi pastor":
    print(char)
