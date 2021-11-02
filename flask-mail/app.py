#importación de librerías
from flask import Flask

from flask_mail import Mail

from preferences import *

app = Flask(__name__)

app.config['MAIL_SERVER'] = smtpServer
app.config['MAIL_PORT'] = port
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = useTLS
app.config['MAIL_USE_SSL'] = useSSL

mail = Mail(app)

def send_message():


    msg = mail.send_message(
        subjectMsg,
        sender=senderMsg,
        recipients=[recipientMsg],
        body=bodyMsg
    )

    mail.send(msg)

    return 'Message sent'

with app.app_context():
    send_message()

if __name__ == '__main__':
    app.run(debug=True)


