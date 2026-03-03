import sqlite3 as sql

conexao = sql.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM agenda') #1 realiza a consulta no db.
resultado = cursor.fetchall() #2 Acesso aos resultados. Retorna uma tupla ou None.
print(f'Nome: {resultado[0][0]}\nTelefone: {resultado[0][1]}')#3
cursor.close()
conexao.close()

#a) Índice do registro (linha): resultado[0]
#b) Índice da coluna dentro do registro: resultado[0][0]