import os
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)


#Configuração de sessão. 
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=10)  # Expirar sessão após 30 minutos de inatividade
)

#Configurando o banco de dados.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

db = SQLAlchemy(app)

# Criando o model usuário --- Modelagem do banco de dados.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Rota para criar o banco de dados
def init_db():
   with app.app_context():
        db.create_all()

#Realiza a requisição da api e devolve em json.
def get_api_data():
    response = requests.get('https://api.apis.guru/v2/list.json')
    data = response.json()
    return data

#Home com paginação
@app.route('/', methods=['GET'])
def home():
    if 'logged_in' in session and session['logged_in']:
        page = request.args.get('page', 1, type=int)
        per_page = 10
        
        api_data = get_api_data()
        items = []
        
        for api_name, api_info in api_data.items():
            for version, details in api_info.get('versions', {}).items():
                items.append({
                    'title': details.get('info', {}).get('title', api_name),
                    'version': version,
                    'email': details.get('info', {}).get('contact', {}).get('email', 'N/A'),
                    'url': details.get('info', {}).get('contact', {}).get('url', None)
                })

        total_items = len(items)
        total_pages = (total_items + per_page - 1) // per_page
        
        start = (page - 1) * per_page
        end = start + per_page
        api_data_paginated = items[start:end]
        
        # Configuração do intervalo de páginas a ser exibido
        visible_pages = 5
        start_page = max(1, page - visible_pages // 2)
        end_page = min(total_pages, start_page + visible_pages - 1)
        
        if end_page - start_page < visible_pages - 1:
            start_page = max(1, end_page - visible_pages + 1)
        
        return render_template('index.html', api_data=api_data_paginated, page=page, total_pages=total_pages, start_page=start_page, end_page=end_page)
    else:
        return render_template('login.html')



#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Login ou senha inválidos, tente novamente!', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

#Registrar
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        
        #Checa se já existe um usuário no banco de dados, caso não exista, ele irá criar a conta.
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Usuário já existe. Por favor, escolha outro nome de usuário.', 'danger')
            return redirect(url_for('register'))
        else:
            #Utilizando criptografia na senha ao enviar para o banco de dados.
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuário registrado com sucesso!', 'sucess')
            return redirect(url_for('login'))
    return render_template('register.html')


#Logout para terminar a sessão
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80, debug=True) #Como é uma aplicação teste, vou deixar o debug no True. 