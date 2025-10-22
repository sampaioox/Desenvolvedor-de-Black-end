#aula 29 dia 29/10/2025

#1.criando banco de dados no pgADMIN 4
import psycopg2

conexao = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="senaisp",
    host="localhost",
    port="5432"
)
conexao.autocommit = True #necessario para criar o banco

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE loja_virtual")
cursor.close()
conexao.close()

print("loja virtual 'loja_virtual' criado com sucesso!")


#2.conectando 
import psycopg2
from psycopg2 import OperationalError

def conectar():
    try:
        #dados da conexão
        conexao = psycopg2.connect(
            dbname="loja_virtual",
            user="postgres",
            password="senaisp",
            host="localhost",
            port="5432"
        )
        
        print("✅ conexão com a loja virtual bem-sucedida!")
        conexao.close()

    except OperationalError as e:
        print("❌ erro ao conectar a loja virtual:")
        print(e)

conectar()


#3. criando a tabela 
import psycopg2

conexao = psycopg2.connect(
    dbname="meubanco",
    user="postgres",
    password="senaisp",
    host="localhost",
    port="5432"
)


cursor = conexao.cursor()
cursor.execute("""
            INSERT INTO clientes (nome, email, telefone) VALUES
            ('marcelo Breitenbach', 'marcelo.breitenbach@sp.senai.br', '(19)9.8111-8959'),
            ('junio da silva', 'junio@uol.com.br', '(19)9.8888-1234'),
            ('ana julia', 'anaju@terra.com.br', '(19)9.1488-9595')
            ON CONFLICT (email) DO NOTHING;
                """)

conexao.commit()
cursor.close()
conexao.close()
print("tabela 'clientes' criada com sucesso!")
