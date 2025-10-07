#aula 21 dia 06/10/2025

1.
#fazendo uma requisição GET para um site

import requests

resposta = requests.get("https://httpbin.org/get")

print("status code:", resposta.status_code)
print("\nCabaçalhos:", resposta.headers)
print("\ncorpo:", resposta.text)


2.
import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/users/3")

print("status code:", resposta.status_code)
print("\nCabaçalhos:", resposta.headers)
print("\ncorpo:", resposta.text)

print("\ncorpo:", resposta.json())
print("content type:", resposta.content)

company = resposta.json()
empresa = company["company"]["name"]
print("\ncompany and name", empresa)


2.
import requests

url = "https://httpbin.org/post"
dados = {"usuario": "marcelo", "curso": "blackend python"}

resposta = requests.post(url, json=dados)

print("método:", resposta.request.method)
print("codigo de status:", resposta.status_code)
print("corpo da resposta:", resposta.json())