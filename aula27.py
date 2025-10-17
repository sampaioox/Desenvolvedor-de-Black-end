#aula 27 dia 16/10/2025
#desafio
1.
from pathlib import Path
from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

@app.route("/")
def home():
    tarefas = [
        {"titulo": "Estudar Flask", "descricao": "Configurar projeto e entender rotas.", "concluida": True},
        {"titulo": "Criar API", "descricao": "Definir endpoints REST para tarefas.", "concluida": False},
        {"titulo": "Conectar DB", "descricao": "Integrar SQLAlchemy e migrar modelos.", "concluida": False},
    ]
    return render_template("index.html", tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)