#aula 23 dia 08/10/2025 

1.
import requests

payload = {
    "id": 1,
    "nome": "preto-2",
    "raridade": 5
}

resposta = requests.put("https://httpbin.org/put", json=payload)

print("Método:", resposta.request.method)
print("Status Code:", resposta.status_code)
print("JSON retornado:")
print(resposta.json())

2.
import requests

url = "https://httpbin.org/headers"

#cabeçalho com user-agent
headers = {
    "user-agent": "cursobackendpython/1.0 (aluno marcelo; +https://meuportfolio.dev)"
}

#enviando
resposta = requests.get(url, headers=headers)

print("Status Code:", resposta.status_code)
print("\ncabeçalhos recebidos pelo o servidor:")
print(resposta.json()["headers"])