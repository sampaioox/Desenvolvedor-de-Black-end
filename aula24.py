#aula 23 dia 09/10/2025

1.
import json

#json com python
texto = '{"curso": "backend", "modulo": "HTTP"}'
dados = json.loads(texto)
print(dados["curso"])    #blackend

novo_json = json.dumps(dados, indent=2)
print(novo_json)


2.
import requests

url = "https://httpbin.org/bearer"

# Token fictício
token = "abc123xyz987"

# Cabeçalho com 'Bearer' correto
headers = {"Authorization": f"Bearer {token}"}

# Enviando requisição
resposta = requests.get(url, headers=headers)

# Exibindo resultados
print("Status Code:", resposta.status_code)
print("Corpo da resposta:")
print(resposta.json())


3.
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Operadores Aritméticos
    soma = 30 + 57
    multiplicacao = 15 * 7
    divisao = 25 / 4
    resto = 37 % 5
    potencia = 6 ** 4

    # Montar resposta como string (HTML simples ou texto)
    resposta = f"""
    <h1>Operadores Aritméticos</h1>
    <ul>
        <li>1. Calcule a soma de 30 + 57: {soma}</li>
        <li>2. Multiplique 15 por 7: {multiplicacao}</li>
        <li>3. Divida 25 por 4 e veja o resultado: {divisao}</li>
        <li>4. Descubra o resto da divisão de 37 por 5: {resto}</li>
        <li>5. Eleve 6 à potência de 4: {potencia}</li>
    </ul>
    """
    return resposta

if __name__ == "__main__":
    app.run(debug=True)


4. #DESAFIO = COLOCAR A CALCULADORA DE IMC DENTRO DO FLASK PARA QUE OS DADOS SEJAM EXIBIDOS EM UMA JANELA NO NAVEGADOR

