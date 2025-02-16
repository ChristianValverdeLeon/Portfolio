from flask import Flask, render_template, request
from flask_mail import Mail, Message  # Importar Flask-Mail

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cobomaster56@gmail.com'  # Reemplazar con tu correo
app.config['MAIL_PASSWORD'] = 'mxpw soko nevz kmzh'  # Reemplazar con tu contraseña
app.config['MAIL_DEFAULT_SENDER'] = 'cobomaster56@gmail.com'  # Reemplazar con tu correo

mail = Mail(app)  # Crear una instancia de Flask-Mail

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario de contacto
@app.route('/contact', methods=['POST'])
def contact():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    # Llamar a la función que enviará el correo
    send_email(nombre, email, mensaje)

    # Retornar una respuesta al usuario
    return "¡Gracias por ponerte en contacto! Tu mensaje ha sido enviado."

# Función para enviar el correo con Flask-Mail
def send_email(nombre, email, mensaje):
    receiver_email = 'christianvaleon@gmail.com'  # Correo receptor

    # Crear el mensaje
    msg = Message(f'Mensaje de {nombre}', recipients=[receiver_email])
    msg.body = f'Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}'

    # Enviar el correo
    try:
        mail.send(msg)  # Usar Flask-Mail para enviar el correo
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

if __name__ == '__main__':
    app.run(debug=True)
