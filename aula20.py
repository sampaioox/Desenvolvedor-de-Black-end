#aula 20 dia 02/10/2025

#desafio do prof luiz fernando

2.   #sistema de biblioteca
from livro_class import livro_class

livro_0 = livro_class("O Pequeno Príncipe ")
livro_1 = livro_class("A menina feita de espinhos")
livro_2 = livro_class("Diario de Anne Frenk")
livro_3 = livro_class("Os tres mosqueteiros")
livro_4 = livro_class("Como eu era antes de voce")
livro_5 = livro_class("A Biblioteca da Meia-Noite")
livro_6 = livro_class("Dom Quixote de La Mancha")
livro_7 = livro_class("O jurado")
livro_8 = livro_class("1984")
livro_9 = livro_class("O Alquimista")
livro_10 = livro_class("Os Miseráveis")

print("==================================="
        '''
        ''')
print("Bem-vindo! nossa loja tem algumas ofertas de livros para voce:"
        '''
        ''')
cliente = input("digite seu nome para começarmos: ")

print(f"{cliente} temos 5 destinos que combina com voce:"
'''
[0] O Pequeno Príncipe
[1] A menina feita de espinhos
[2] Diario de Anne Frenk
[3] Os tres mosqueteiros
[4] Como eu era antes de voce
[5] A Biblioteca da Meia-Noite
[6] Dom Quixote de La Mancha
[7] o jurado
[8] 1984
[9] O Alquimista
[10] Os Miseráveis
''')

seleção = int(input("selecione o numero do livro desejado: "))  #solicitação ao usuario
lista_livro = [ livro_0, livro_1, livro_2, livro_3, livro_4]  #lista dos indices
opção_selecionada = int(seleção)
for opção in lista_livro:
    if opção_selecionada >= 5:  #caso o usuario não digite a opção correta
        print("esta opção não esta encluida em nossa biblioteca.")
        break
    if opção_selecionada <= 4:  #verifica a seleção
        print(f"{cliente} seu livro {lista_livro[opção_selecionada].destino} foi comprada com sucesso. ")
        print("volte sempre!")
        break



#exercicio 1, 2 tiveram as pasta livro_class, e feira_class abertas exemplo
#class feira_class:
    #def __init__(self, feira):
        #self.destino = feira



3.  #sistema de feira livre

from feira_class import feira_class

fruta_0 = feira_class("banana")
fruta_1 = feira_class("maça")
fruta_2 = feira_class("goiaba")
fruta_3 = feira_class("abacate")
fruta_4 = feira_class("melão")

print("==================================="
        '''
        ''')
print("Bem-vindo! ao hortifrute da ana temos algumas ofertas para voce:"
        '''
        ''')
cliente = input("digite seu nome para começarmos: ")

print(f"{cliente} temos 5 frutas que talvez combine com voce:"
'''
[0] banana
[1] maça 
[2] goiaba
[3] abacate
[4] melão

''')

seleção = int(input("selecione o numero da fruta desejada: "))  #solicitação ao usuario
feira_class = [fruta_0, fruta_1, fruta_2, fruta_3, fruta_4]  #lista dos indices
opção_selecionada = int(seleção)
for opção in feira_class:
    if opção_selecionada >= 5:  #caso o usuario não digite a opção correta
        print("esta opção não esta encluida em nossos menu.")
        break
    if opção_selecionada <= 4:  #verifica a seleção
        print(f"{cliente} sua fruta esta {feira_class[opção_selecionada].destino} ja eata na sacola!. ")
        print("volte sempre!")
        break


4.  #agenda POO
 # Classe Contato
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


# Classe Agenda
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato '{contato.nome}' adicionado com sucesso.")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            print("Contatos na agenda:")
            for contato in self.contatos:
                print(contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")


# Exemplo
if __name__ == "__main__":
    agenda = Agenda()

    # Criar contatos
    contato1 = Contato("Alice", "1234-5678", "alice@email.com")
    contato2 = Contato("Bob", "9876-5432", "bob@email.com")

    # Adicionar contatos
    agenda.adicionar_contato(contato1)
    agenda.adicionar_contato(contato2)

    # Listar contatos
    agenda.listar_contatos()

    # Buscar contato
    nome_busca = "Alice"
    encontrado = agenda.buscar_contato(nome_busca)
    if encontrado:
        print(f"\nContato encontrado: {encontrado}")
    else:
        print(f"\nContato '{nome_busca}' não encontrado.")

    # Remover contato
    agenda.remover_contato("Bob")
    agenda.listar_contatos()


5. #Sistema de Cadastro com Conjuntos e POO
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    pass

class Professor(Pessoa):
    pass

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()
        self.professores = set()

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)

    def adicionar_professor(self, professor):
        self.professores.add(professor)

    def mostrar_dados(self):
        print(f"\nCurso: {self.nome}")
        print("Professores:")
        for prof in self.professores:
            print(f"- {prof.nome}")
        print("Alunos:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}")

# Exemplo de uso
curso1 = Curso("Programação em Python")

a1 = Aluno("João")
a2 = Aluno("Maria")
p1 = Professor("Prof. Carla")

curso1.adicionar_aluno(a1)
curso1.adicionar_aluno(a2)
curso1.adicionar_professor(p1)

curso1.mostrar_dados()




