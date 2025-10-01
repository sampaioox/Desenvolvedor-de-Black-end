#aula18 dia 30/09/2025

#encapsulamento e herança

1.
class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = 0  
        self.set_nota(nota) 

    def get_nota(self):
        """Retorna a nota do aluno."""
        return self.__nota

    def set_nota(self, nova_nota):
        """Define a nota do aluno, validando se está entre 0 e 10."""
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Erro: A nota deve estar entre 0 e 10.")

    def get_nome(self):
        """Retorna o nome do aluno."""
        return self.__nome

# Exemplo de uso:
aluno1 = Aluno("Maria", 7.5)
print(f"Nome: {aluno1.get_nome()}, Nota: {aluno1.get_nota()}")

# Tentando definir uma nota inválida
aluno1.set_nota(12)
print(f"Nota após tentativa inválida: {aluno1.get_nota()}")

# Definindo uma nota válida
aluno1.set_nota(9.0)
print(f"Nota após tentativa válida: {aluno1.get_nota()}")


2.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


class Professor(Pessoa):
    def __init__(self, nome, idade, materia):
        # Chama o construtor da classe pai (Pessoa) para inicializar nome e idade
        super().__init__(nome, idade)
        self.materia = materia 

    def ensinar(self):
        return f"Eu sou o(a) professor(a) {self.nome} e ensino {self.materia}."

# Exemplo:

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Maria", 30)
print(pessoa1.apresentar())  

# Criando uma instância da classe Professor
professor1 = Professor("Carlos", 45, "Matemática")
print(professor1.apresentar())  
print(professor1.ensinar())    


3.
# Classe base
class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")

# Subclasse Carro
class Carro(Veiculo):
    def mover(self):
        print("O carro está acelerando pela estrada.")

# Subclasse Bicicleta
class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está pedalando pela ciclovia.")

veiculo1 = Carro()
veiculo1.mover()  

veiculo2 = Bicicleta()
veiculo2.mover() 


4.
class Usuario:
    def __init__(self, senha):
        self.__senha = senha # atributo privado

    def alterar_senha(self, antiga, nova):
        """Troca a senha apenas se a antiga estiver correta."""
        if self.__senha == antiga:
            self.__senha = nova
            print("Senha alterada com sucesso!")
        else:
            print("Senha antiga incorreta. Não foi possível alterar.")

    def login(self, senha):
        """Valida o acesso verificando se a senha está correta."""
        if self.__senha == senha:
            print("Login realizado com sucesso!")
            return True
        else:
            print("Senha incorreta. Acesso negado.")
            return False


# Exemplo de uso
usuario1 = Usuario("1234")

usuario1.login("1234") 
usuario1.alterar_senha("1234", "abcd") 
usuario1.login("abcd") 
usuario1.login("1234") 

5.
# Classe base
class Animal:
    def __init__(self, nome):
        self._nome = nome 

    def mover(self):
        print(f"{self._nome} está se movendo.")

# Subclasse de Animal
class Mamifero(Animal):
    def amamentar(self):
        print(f"{self._nome} está amamentando.")

# Subclasse de Mamífero
class Cachorro(Mamifero):
    def latir(self):
        print(f"{self._nome} está latindo: Au Au!")

# ---- Teste ----
dog = Cachorro("Rex")

# Chamando métodos de cada nível
dog.mover()
dog.amamentar() 
dog.latir() 

#.........
#abstração e polimorfismo exemplo:

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class cachorro(animal):
    def faze_som(self):
        return "au au!"
    
class gato(animal):
    def faze_som(self):
        return "miau!"
    

1.
from abc import ABC, abstractmethod

# Classe abstrata
class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass

# Subclasses concretas
class Violao(Instrumento):
    def tocar(self):
        return "O violão está tocando acordes 🎸"

class Piano(Instrumento):
    def tocar(self):
        return "O piano está tocando notas clássicas 🎹"

class Bateria(Instrumento):
    def tocar(self):
        return "A bateria está fazendo a batida 🥁"

# Lista de instrumentos
instrumentos = [Violao(), Piano(), Bateria()]

# Executando
for i in instrumentos:
    print(i.tocar())
