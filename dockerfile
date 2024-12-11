# Base image
FROM python:3.12-alpine

# Instalar pacotes necessários
RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    libffi-dev \
    python3-dev \
    build-base \
    bash

# Definir diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt e instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o container
COPY . /app/

# Expor a porta 8000
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
