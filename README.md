# Aplicação de Teste Prático - Consumo de API, Autenticação de usuário e cadastro.

## Descrição
 Essa aplicação consome a APIs.guru (2.2.0) e apresenta as informações de APIs em uma interface web. Além disso, implementa um sistema de login com controle de sessão, registro de usuário, paginação e banco de dados para os usuários.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação.
- **Flask-SQLAlchemy**: Extensão para Flask que simplifica o uso do SQLAlchemy.
- **Flask**: Framework web para o back-end.
- **requests**: Biblioteca para o consumo da API.
- **psycopg2-binary**: Adaptador para PostgreSQL que permite a conexão entre Python e um banco de dados PostgreSQL.
- **Werkzeug**: Biblioteca que fornece utilitários para construir e manter aplicativos web em Python, responsável pela criação da hash de senha. 
- **HTML e Bootstrap**: Para o front-end.
- **Docker**: Para containerização da aplicação e do banco de dados.


## Instruções para Execução ##

### 1. Clone o repositório:
    ```sh
    git clone <SEM LINK AINDA, PROJETO SECRETO KK>
    cd my_app
    ```

### 2. Instale o Docker e o Docker Compose
Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina. Você pode seguir as instruções na [documentação oficial do Docker](https://docs.docker.com/get-docker/) e [documentação do Docker Compose](https://docs.docker.com/compose/install/).

### 3. Crie e inicie os contêineres Docker:
    ```sh
    docker-compose up --build
    ```

### 4. Acesse a aplicação:
   - Abra um navegador e acesse `http://localhost` para visualizar a aplicação rodando na porta 80.

## Funcionalidades
- **Consumo da APIs.guru (2.2.0)**: Os dados das APIs são apresentados na tabela, tendo também o link para redirecionamento de cada uma.
- **Sistema de Login**: Redireciona para a rota /login se o usuário não estiver autenticado ou se terminar o tempo da sessão (padrão de 10 minutos).
- **Sistema de registro**: Redireciona para a rota /register se o usuário já existir, caso não exista, cria um novo usuário com senha criptografada no banco de dados.
- **Banco de dados PostgreSQL**: Responsável por armazenar o cadastro dos usuários.

## Melhorias Futuras
- Implementação de testes automatizados.
- Melhorar a interface com mais funcionalidades interativas.

## Customizações Extras
- O sistema de autenticação foi implementado com Flask sessions.
- O sistema de autenticação possui criptografia da biblioteca werkzeug.security.
- Banco de dados independente.
- Sistema de registro para novos usuários.
- Implementação do docker. 
