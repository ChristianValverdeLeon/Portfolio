# Usa una imagen oficial de Python
FROM python:3.10

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias sin venv
RUN pip install --no-cache-dir -r requirements.txt  

# Expone el puerto 5000 para Flask
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "app.py"]
