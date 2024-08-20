from pathlib import Path

# si no queremos remplazar todo el texto en el archivo debemos tener pendiente de trabajarlo por saltos de lineas como un array como hacemos a continuacion
archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "Hola Mundo!")

archivo.write_text("\n".join(texto), "utf-8")
