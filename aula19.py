#aula 19 dia 01/10/2025

1.
from abc import ABC, abstractmethod

# Classe abstrata
class Funcionario(ABC):
    @abstractmethod
    def calcular_pagamento(self):
        pass

# Subclasse

class Assalariado(Funcionario):
    def __init__(self, nome, salario_fixo):
        self.nome = nome
        self.salario_fixo = salario_fixo

    def calcular_pagamento(self):
        return self.salario_fixo

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.valor_hora * self.horas_trabalhadas


#Testando 

funcionarios = [
    Assalariado("Ana", 3000),
    Horista("João", 50, 120), 
    Horista("Maria", 40, 100) 
]

for f in funcionarios:
    print(f"{f.nome} vai receber: R$ {f.calcular_pagamento():.2f}")


2.
from abc import ABC, abstractmethod
import math

# Classe abstrata
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

# Testando
ret = Retangulo(5, 3)
circ = Circulo(4)

print(f"Área do retângulo: {ret.area():.2f}")
print(f"Área do círculo: {circ.area():.2f}")


3.
from abc import ABC, abstractmethod

# Classe abstrata
class Veiculo(ABC):
    @abstractmethod
    def abastecer(self):
        pass


# Classe Carro
class Carro(Veiculo):
    def abastecer(self):
        print("Carro abastecido com gasolina.")


# Classe Caminhão
class Caminhao(Veiculo):
    def abastecer(self):
        print("Caminhão abastecido com diesel.")


# Programa principal
if __name__ == "__main__":
    veiculos = [Carro(), Caminhao()]

    for v in veiculos:
        v.abastecer()


4.
# Definindo as classes

class Carro:
    def mover(self):
        print("O carro está se movendo pela estrada.")

class Aviao:
    def mover(self):
        print("O avião está voando pelos céus.")

class Barco:
    def mover(self):
        print("O barco está navegando pelo mar.")

# Função que executa o movimento
def executar_movimento(objeto):
    if hasattr(objeto, 'mover') and callable(getattr(objeto, 'mover')):
        objeto.mover()
    else:
        print("O objeto não tem o método 'mover'.")

# Testando
carro = Carro()
aviao = Aviao()
barco = Barco()

executar_movimento(carro)   
executar_movimento(aviao)  
executar_movimento(barco)   

#viagem_class faz parte dessa aula!