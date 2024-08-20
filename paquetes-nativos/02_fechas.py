# import time

# # utc
# print(time.time())

from datetime import datetime

fecha = datetime(2023, 7, 13)

fecha_ahora = datetime.now()

# es segundo argumento se le llama directives
fechaStr = datetime.strptime("2023-07-13", "%Y-%m-%d")

print(fecha.strftime("%Y.%m.%d"))

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.day,
    fecha.minute
)

# SIGUIENTES TEMAS DE ESTE MODULO, VIDEO SOLO VISTOS Y ANOTADOS(LUEGO INVESTIGARLOS)
# => timedelta
