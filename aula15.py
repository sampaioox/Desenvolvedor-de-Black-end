#aula 15
#continuação da aula anterior

# cria o arquivo alunos.txt com 5 nomes
with open("alunos.txt", "w") as arq:
    arq.write("Ana\n")
    arq.write("Bruno\n")
    arq.write("Carlos\n")
    arq.write("Mariana\n")
    arq.write("João\n")

# lendo e mostrando os nomes do arquivo
with open("alunos.txt", "r") as arq:
    for linha in arq:
        print(linha.strip())


        linhas = ["ana\n", "bruno\n", "carlos\n"]
with open("participantes.txt", "w") as arq:
    arq.writelines(linhas)
