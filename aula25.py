#aula 25 dia 13/10/2025

#1.BANCO DE DADOS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
db = SQLAlchemy(app)

# Modelo (Model)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.titulo}>'

# Criando o banco de dados e a tabela
with app.app_context():
    db.create_all()


#2.ADICIONANDO UMA TAREFA NO BANCO DE DADOS

with app.app_context():
    nova_tarefa = Task(titulo="estudar Flask", descricao="aprender sobre moldagem da dados")
    db.session.add(nova_tarefa)
    db.session.commit()

    tarefas = Task.query.all()
    print(tarefas)


3.
from flask import Flask, render_template

app = Flask(__name__)

#controller
@app.route('/')
def home():
    #model (simulação de dados)
    tarefas = [
        {"titulo": "estudar Flask", "concluida": True},
        {"titulo": "criar API", "concluida": False},
    ]
    #view
    return render_template ("index.html", tarefas = tarefas)
if __name__ == '__main__':
    app.run(debug=True)