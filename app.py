from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Configuración para enviar el correo
        send_email(name, email, message)

        # Puedes mostrar un mensaje de éxito o redirigir al usuario
        return "Gracias por tu mensaje. Te contactaremos pronto."

    return render_template('contact.html')

def send_email(name, sender_email, message):
    # Configura tu correo y servidor SMTP
    sender_password = 'Cobo.password'
    receiver_email = 'cobomaster56@gmail.com'

    # Establecer el servidor de correo
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f'Nuevo mensaje de {name}'

    body = f'Nombre: {name}\nCorreo: {sender_email}\n\nMensaje:\n{message}'
    msg.attach(MIMEText(body, 'plain'))

    # Enviar el correo
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Establecer conexión segura
        server.login(sender_email, sender_password)  # Iniciar sesión
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Enviar el correo
        server.quit()  # Cerrar la conexión
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

if __name__ == '__main__':
    app.run(debug=True)
