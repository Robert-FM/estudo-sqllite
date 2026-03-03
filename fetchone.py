import sqlite3 as sql

conexao = sql.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM agenda')

while True:
    resultado = cursor.fetchone()
    
    if resultado is None:
        break

    for resultado in cursor:
        print(f'Nome: {resultado[0]}')
        print(f'Telefone: {resultado[1]}')
        print('-' * 20)
        
cursor.close()
conexao.close()

#Devido o fetchone(), tem que colocar os índices