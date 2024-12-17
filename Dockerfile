# Usar la imagen oficial de Python 3.10
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo Python dentro del contenedor
COPY christian_algorithm.py .

# Ejecutar el script Python cuando el contenedor se ejecute
CMD ["python", "christian_algorithm.py"]
