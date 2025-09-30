#aula 17 dia 29/09/2025

1.
class contabancaria:
    def __init__(self, titular,saldo):
        self.__titular = titular  #atributo privado
        self.__saldo = saldo   #atributo privado

    #getter
    def get_saldo(self):
        return self.__saldo
    
    #setter
    def depositar(self, valor):
        self.__saldo += valor

conta = contabancaria ("Ana", 1000)
print(conta.get_saldo())   #acessa saldo
conta.depositar(500)    #alterar saldo
print(conta.get_saldo())


2.
class animal:
    def __init__(self,nome):
        self.nome = nome

    def emitir_som(self):
        print("som generico...")

class cachorro(animal):   
    def emitir_som(self):   #sobrescrevendo método
        print("Au au!")

class gato(animal):
    def emitir_som(self):
        print("miau!")

dog = cachorro("Rex")
cat = gato("mimi")

dog.emitir_som()  #au au!
cat.emitir_som()  #miau


3.
class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome # privado
        self.__salario = salario # privado

    # Getter do nome
    def get_nome(self):
        return self.__nome

    # Setter do nome
    def set_nome(self, nome):
        self.__nome = nome

    # Getter do salário
    def get_salario(self):
        return self.__salario

    # Setter do salário
    def set_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            print("Salário inválido!")

# Classe Gerente que herda de Funcionário
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario) # chama o construtor da classe mãe
        self.departamento = departamento

    def mostrar_departamento(self):
        print(f"O gerente {self.get_nome()} é do departamento: {self.departamento}")


# Testando
f1 = Funcionario("Ana", 3000)
print(f"Funcionário: {f1.get_nome()} - Salário: {f1.get_salario()}")

g1 = Gerente("Carlos", 8000, "TI")
print(f"Gerente: {g1.get_nome()} - Salário: {g1.get_salario()}")
g1.mostrar_departamento()


4.
 #Classe base
class Veiculo:
    def __init__(self, marca, ano):
        self._marca = marca # atributo encapsulado (com underline)
        self._ano = ano

    def get_marca(self):
        return self._marca

    def get_ano(self):
        return self._ano


# Subclasse Carro
class Carro(Veiculo):
    def __init__(self, marca, ano):
        super().__init__(marca, ano)

    def mostrar_tipo(self):
        print(f"Sou um Carro. Marca: {self.get_marca()}, Ano: {self.get_ano()}")


# Subclasse Moto
class Moto(Veiculo):
    def __init__(self, marca, ano):
        super().__init__(marca, ano)

    def mostrar_tipo(self):
        print(f"Sou uma Moto. Marca: {self.get_marca()}, Ano: {self.get_ano()}")


# Criando objetos e chamando métodos
carro1 = Carro("Toyota", 2022)
moto1 = Moto("Honda", 2021)

carro1.mostrar_tipo()
moto1.mostrar_tipo()


5.
# Classe base
class Funcionario:
    def trabalhar(self):
        print("O funcionário está trabalhando normalmente.")

# Subclasse herdando de Funcionario
class Estagiario(Funcionario):
    # Sobrescrevendo o método trabalhar()
    def trabalhar(self):
        print("O estagiário está aprendendo e ajudando no trabalho.")

# Criando objetos de cada tipo
f1 = Funcionario()
e1 = Estagiario()

# Chamando os métodos
f1.trabalhar()
e1.trabalhar()
