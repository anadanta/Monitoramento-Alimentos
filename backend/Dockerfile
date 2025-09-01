# Use uma imagem oficial do Python como imagem base
FROM python:3.11

# Define o diretório de trabalho no container
WORKDIR /usr/src/app

# Define variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instale as dependências do sistema (necessário para o mysqlclient)
RUN apt-get update && apt-get install -y --no-install-recommends gcc default-libmysqlclient-dev

# Copie o arquivo de dependências e instale-as
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o código do projeto para o diretório de trabalho
COPY . .