import os
from twilio.rest import Client


sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_N")


cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Probando el envio de sms con python y twilio",
    from_=numero,
    to="+15512473829"
)
print(mensaje)