import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient



email = os.environ.get("SENGRID_MAIL")

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="Correo de prueba",
    html_content="Aprendiendo como <b>crear y enviar</b> un email con sendgrid"
)

try:
    apikey = os.environ.get("SENGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body
    )
except Exception as e:
    print(e)