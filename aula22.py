#aula 22 dia 07/10/2025

1.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

#dados devem ser enviados no corpo da requisição
novo_post = {
    "title": "meu primeiro post via python",
    "body": "estou aprendendo sobre http!",
    "userID": 1
}

resposta = requests.post(url, json=novo_post)

print("status code:", resposta.status_code)
print("corpo da resposta", resposta.json())


2.
#use o endpoint https://httpbin.org/post 
#envie um json com seus dados (nome, cidade, curso).
#imprima: o metodo, o status code, o conteudo retornado em formado em json, a url para a qual a requisição foi feita
#dica:o site httpbin.org devolve exatamente oque voce enviou - ideal para teste


import requests

# URL do endpoint
url = "https://httpbin.org"


# Dados em formato JSON

meus_dados = {
    "nome": "João da Silva",
    "cidade": "São Paulo",
    "curso": "Engenharia de Software"
}

# Enviando
resposta = requests.post(url, json=meus_dados)

# Imprimindo 
print("Método HTTP:", resposta.request.method)
print("Status Code:", resposta.status_code)
print("Conteúdo retornado (JSON):", resposta.json())
print("URL da requisição:", resposta.url)


3.

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
#dados atualizados
dados_atualizados ={
    "id": 1,
    "title": "titulo atualizado",
    "body": "conteudo substituido com sucesso!",
    "userID": 1
}

resposta = requests.post(url, json=dados_atualizados)
print("status code:", resposta.status_code)
print("corpo da resposta", resposta.json())


4.
#use o endpoint https://httpbin.org/put 
#envie um json com os seguintes campos: id:numero inteiro, nome:seu nome, curso:especifique um curso
#imprima: o método deve aparecer PUT, status code, o JSON retornado pelo o servidor


import requests

# Dados a serem enviados
payload = {
    "id": 1,
    "nome": "seu nome",
    "curso": "Ciência da Computação"
}

# Enviando a requisição PUT
response = requests.put("https://httpbin.org/put", json=payload)

# Exibindo as informações
print("Método:", response.request.method)
print("Status Code:", response.status_code)
print("JSON retornado:")
print(response.json())


5.
#modo delete

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

resposta = requests.delete(url)

print("status code:", resposta.status_code)
print("corpo da resposta", resposta.text)


6.
# use o endpoint https://httpbin.org/delete envie uma requisição DELETE simulando a exclusão de um registro
#imprima: o metodo, o status code, o conteudo do corpo da resposta


import requests

# URL do endpoint
url = "https://httpbin.org/delete"

# Dados simulando o registro a ser excluído
data = {
    "id": 123,
    "nome": "Registro de exemplo"
}

# Envia a requisição DELETE
responta = requests.delete(url, json=data)

# Imprime os resultados
print("Método:", response.request.method)
print("Status Code:", response.status_code)
print("Corpo da Resposta:", response.text)


7.

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
#apenas o campo que sera alterado

dados_parcerias = {
    "title": "titulo  parcialmente atualizado"
}

responta = requests.patch(url, json=dados_parcerias)
print("status code:", resposta.status_code)
print("corpo da resposta", resposta.json())


8.
import requests

url = "https://httpbin.org/patch"

meus_dados = {
    "nome": "João da Silva",
    "cidade": "São Paulo",
    "curso": "backend avançado"
}

# Enviando
resposta = requests.patch(url, json=meus_dados)

# Imprimindo 
print("Status Code:", resposta.status_code)
print("Conteúdo retornado (JSON):", resposta.json())


9.
import requests

url = "https://httpbin.org/anything"

resposta = requests.options(url)

print("Status Code:", resposta.status_code)
print("metodos permitidos:", resposta.headers.get("allow"))
print("todos os headers:", resposta.headers)


10.
import requests
import json

# Função para imprimir informações da resposta
def exibir_resposta(response):
    print("\n--- Resultado da Requisição ---")
    print(f"Método HTTP: {response.request.method}")
    print(f"URL de destino: {response.url}")
    print(f"Status code: {response.status_code}")
    print("Conteúdo JSON da resposta:")
    print(json.dumps(response.json(), indent=4))
    print("--------------------------------")

# 1 Requisição GET com dois parâmetros
def requisicao_get():
    url = "https://httpbin.org/get"
    parametros = {"nome": "Annah", "curso": "Desenvolvimento Backend"}
    response = requests.get(url, params=parametros)
    exibir_resposta(response)

# 2 Requisição POST com JSON no corpo
def requisicao_post():
    url = "https://httpbin.org/post"
    dados = {"nome": "Annah", "idade": 22, "cidade": "São Paulo"}
    response = requests.post(url, json=dados)
    exibir_resposta(response)

# 3 Requisição PUT com JSON atualizado
def requisicao_put():
    url = "https://httpbin.org/put"
    dados_atualizados = {"nome": "Annah", "idade": 23, "cidade": "Campinas"}
    response = requests.put(url, json=dados_atualizados)
    exibir_resposta(response)

# 4 Requisição DELETE com identificador no corpo
def requisicao_delete():
    url = "https://httpbin.org/delete"
    dados = {"user_id": 101}
    response = requests.delete(url, json=dados)
    exibir_resposta(response)

# Executando todas as funções
if __name__ == "__main__":
    print("Iniciando o desafio de métodos HTTP...\n")
    requisicao_get()
    requisicao_post()
    requisicao_put()
    requisicao_delete()