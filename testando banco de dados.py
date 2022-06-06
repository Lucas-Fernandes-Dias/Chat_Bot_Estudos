import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='clientes_esfiharia'
)
cursor = banco.cursor()


comando_SQL = 'INSERT INTO clientes (nome, telefone, pedido) VALUES (%s,%s,%s)'
dados = ('Maria', '991590675', 'Carne')

cursor.execute(comando_SQL, dados)
banco.commit()


