FROM python:3.10

# Crear un directorio de trabajo
WORKDIR /servidor

COPY servidor1.py .

EXPOSE 5000

# Instala las dependencias
RUN pip install flask

# Ejecutar la aplicacion
CMD ["python", "servidor1.py"]