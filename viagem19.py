from viagem_class import viagem_class

viagem_0 = viagem_class("florida")
viagem_1 = viagem_class("havaí")
viagem_2 = viagem_class("tóquio")
viagem_3 = viagem_class("egito")
viagem_4 = viagem_class("londres")

print("==================================="
        '''
        ''')
print("Bem-vindo! senai viagens tem algumas ofertas para voce:"
        '''
        ''')
viajante = input("digite seu nome para começarmos: ")

print(f"{viajante} temos 5 destinos que combina com voce:"
'''
[0] flórida
[1] havaí
[2] tóquio
[3] egito
[4] londres

''')

seleção = int(input("selecione o numero da viajem desejada: "))  #solicitação ao usuario
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4]  #lista dos indices
opção_selecionada = int(seleção)
for opção in lista_viagem:
    if opção_selecionada >= 5:  #caso o usuario não digite a opção correta
        print("esta opção não esta encluida em nossos destinos.")
        break
    if opção_selecionada <= 4:  #verifica a seleção
        print(f"{viajante} sua viagem para {lista_viagem[opção_selecionada].destino} esta marcada. ")
        print("volte sempre!")
        break