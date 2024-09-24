# Usando uma imagem oficial do Python como base
FROM python:3.10-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o arquivo requirements.txt e instalando as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código da aplicação para o diretório de trabalho
COPY . .

# Expondo a porta que o Flask irá rodar
EXPOSE 80

# Comando para rodar a aplicação
CMD ["python", "app.py"]
