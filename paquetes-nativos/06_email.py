# https://myaccount.google.com/u/1/lesssecureapps


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


path = Path("paquetes-nativos/img.html")
mine_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Sam Minyety"
mensaje["to"] = "sam0101dev@gmail.com"
mensaje["subject"] = "Probando los mensajes smtp en python"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mine_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("correo_origen", "contraseña")
    smtp.send_message(mensaje)
    # opcional para verificar que todo el codigo fue ejecutado
    print("Mensaje enviado")
