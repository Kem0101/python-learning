import requests

# convencion de status code
# 200 listar, 201 crear, 204 actualizar o eliminar


# listar los recursos
# url = "https://jsonplaceholder.typicode.com/users"

# info = requests.get(url, timeout=10)
# print(
#     info,
#     info.status_code,
#     info.text
# )
# info = info.json()

# for user in info:
#     print(user["name"])

# buscar solo un usuario
# url = "https://jsonplaceholder.typicode.com/users/7"
# info = requests.get(url, timeout=10)
# print(info.json())


# crear un recurso
# url = "https://jsonplaceholder.typicode.com/users/"
# user = {
#     "name": "Kemuel Martinez"
# }

# info = requests.post(url, timeout=10, data=user)
# print(info.status_code)

# actualizar un recurso
# url = "https://jsonplaceholder.typicode.com/users/3"
# user = {
#     "name": "Kemuel Martinez"
# }

# info = requests.put(url, timeout=10, data=user)
# print(info.status_code)


# eliminar recurso
# esta es la forma standar de pasarle headers a las peticiones a la api
url = "https://jsonplaceholder.typicode.com/users/3"
apikey = "1234567"
headers = {
    "Autorization": f"Bearer {apikey}"
}

info = requests.delete(url, timeout=10, headers=headers)
print(info.status_code)
