#importación de librerías
from flask import Flask

from flask_mail import Mail

import asyncio

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cebem2021@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ad1234Ad1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def send_message():

    msg = mail.send_message(
        'Hola Angel',
        sender='cebem2021@gmail.com',
        recipients=['gonzalezm.angel@gmail.com'],
        body="Si ves este correo, es porque la API de Flask-Mail funciona"
    )

    mail.send(msg)

    return 'Message sent'

with app.app_context():
    send_message()

if __name__ == '__main__':
    app.run(debug=True)


