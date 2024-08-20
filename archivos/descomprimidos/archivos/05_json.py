import json
from pathlib import Path

# json (javascript object notation)
# escribir json
# productos = [
#     {"id": 1, "name": "Guante Rawling"},
#     {"id": 2, "name": "Zapatillas Guarache Elite"},
#     {"id": 3, "name": "Bate Easton"}
# ]

# data = json.dumps(productos)  # convertir un listado de diccionario en json
# Path("archivos/productos.json").write_text(data)


data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar el json
productos[0]["name"] = "Guante Mizuno"
Path("archivos/productos.json").write_text(json.dumps(productos), encoding="utf-8")
