#aula 28 dia 20/10/2025

#1. exemplo 
from dataclasses import dataclass

@dataclass
class produto:
    nome: str
    preço: float
    estoque: int = 0 #valor padrão

p1 = produto("caneta", 2.50, 10)
p2 = produto("caneta", 2.50, 10)

print(p1)  #produto
print(p1 == p2)  #true


#2. exemplo pratico - banco de dados
import sqlite3

#crie uma conexão
conexao = sqlite3.connect('meubanco.db')

#cria um Curso
cursor = conexao.cursor()

# cria tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

#insere um registro
cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ('João', 'joao@email.com'))

#salva
conexao.commit()
conexao.close()

print("banco criado e usuario inserido com sucesso!")


#3. desafio
import sqlite3

# banco de dados
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()

#tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
''')

# Inserindo produtos
cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES ('Mouse Gamer', 99.90, 15)")
cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES ('Teclado Mecânico', 199.90, 10)")
cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES ('Headset', 149.90, 8)")

# Salvando 
conexao.commit()

#listando
cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

print("=== Lista de Produtos ===")
for p in produtos:
    print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R${p[2]:.2f} | Estoque: {p[3]}")


#print("=== lista de produtos ===")
#print(produtos)

# Fechando a conexão
conexao.close()


#4.
