import mysql.connector


cardapio = ['Carne: Carne Moida com temperos',
            'Queijo: Mussarela',
            'Pizza: Carne e Queijo Tomate e oregano'
            ]
cardapio1 = {'Carne: Carne Moida com temperos',
             'Queijo: Mussarela',
             'Pizza: Carne e Queijo Tomate e oregano'
             }

dados = {}
pedidos = []
pedido = 'queijo'


nome = str(input('Bot Esfiha Show: Qual seu Nome: '))
telefone = int(input('Qual o número do seu celular: '))

#criei banco de dados para receber nome, telefone e pedido do cliente


#criando sistema pra conferir se já tem o cliente no banco de dados


banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='clientes_esfiharia'
)

cursor = banco.cursor()

comando_SQL = 'INSERT INTO clientes (nome, telefone, pedido) VALUES (%s,%s,%s)'
dado = (nome, telefone, pedidos[:])

cursor.execute(comando_SQL, dado)
banco.commit()

# printe de resposta a primeira mensagem do cliente

print(f'Boa Noite {nome} seja bem vindo!')
print('<' * 28)
print('Segue a baixo nosso cardápio.')
print('>' * 28)
print()
print()

#printar o cardápio pro cliente

for k, v in enumerate(cardapio1):
    print(f'{k + 1} : {v}')

print()
print()

while True:

    escolha = int(input('Boa noite, qual o seu pedido pra hoje?: '))
    if escolha == 1:
        pedidos.append(cardapio[escolha - 1])
        print(f'A sua escolha é {cardapio[escolha - 1]}')
    elif escolha == 2:
        pedidos.append(cardapio[escolha - 1])
        print(f' A sua escolha é {cardapio[escolha - 1]}')
    elif escolha == 3:
        pedidos.append(cardapio[escolha - 1])
        print(f'A sua escolha é {cardapio[escolha - 1]}')
    continuar = str(input('Vamos acrescentar mais algum item?: [SIM] ou [NÃO]')).strip().upper()
    if continuar not in 'Ss':
        break

print()
print('O seu pedido ficou assim:')
print()
for p in pedidos:
    print(p)

print()

if banco.is_connected():
    cursor.close()
    banco.close()
    print('Conexão com MySQL encerrada')