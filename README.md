# Mi Portfolio

Este es un proyecto de portfolio personal creado con Flask y Docker.

## Tecnologías utilizadas

- Python 3.10
- Flask
- Docker
- HTML
- CSS

## Cómo correr el proyecto

1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `python app.py`.
4. Abre tu navegador y ve a `http://127.0.0.1:5000/`.

## Docker

Este proyecto también está configurado para ejecutarse dentro de un contenedor Docker.

1. Construye la imagen Docker: `docker build -t flask-portfolio .`
2. Ejecuta el contenedor: `docker run -p 5000:5000 flask-portfolio`

