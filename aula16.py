#aula 16 dia 25/09/2025

1.
# registro.py
# Solicita nome e idade do usuário e grava no arquivo usuario.txt

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# abre o arquivo em modo de adição (append)
with open("usuario.txt", "a", encoding="utf-8") as arq:
    arq.write(f"{nome};{idade}\n")

print("Dados salvos com sucesso em usuario.txt!")

2.

with open("nomes.txt", "r") as arq:
    for linha in arq:
        print(linha.strip()) #.strip()remove\n

3.
#ler o arquivo
with open("nomes.txt", "r") as arq:
    nomes = arq.readlines()

#modifica
nomes_formatos = []
for n in nomes:
    n = n.strip().upper() + "\n"
    nomes_formatos.append(n)

#escreve de volta
with open("nomes.txt", "w") as arq:
    arq.writelines(nomes_formatos)

4.
#criar um arquivo com esse comando

with open("novo.txt", "x") as arq:
    arq.write("arquivo novo criado!\n")

5.

with open("usuario.txt", "r") as arq:
    linhas = arq.readlines()

linhas_formadas =[]
for linha in linhas:
    nome, idade = linha.strip().split(";")
    linhas_formadas.append(f"{nome.upper()};{idade}\n")

with open("usuario.txt", "w") as arq:
    arq.writelines(linhas_formadas)