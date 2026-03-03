import sqlite3 as sql #1

conexao = sql.connect("agenda.db") #2 criação do db
cursor = conexao.cursor() #3 criação do cursor. Cursor são objetos utilizados para enviar comandos e receber resultados do db.
cursor.execute('''
               create table agenda(
               nome text, telefone text)
               ''') 
#4 É o método 'execute' do cursor para enviar o comando ao db.
cursor.execute('''
               INSERT INTO agenda (nome,telefone) 
               VALUES(?,?)
               ''',('Nilo','7788-1432')) #5 É o método 'execute' para executar o comando 'insert', passamos os dados logo após o comando.
conexao.commit() #6 É a parte das operações necessárias para modificar o banco de dados.
cursor.close() #7 Fechamento do cursor
conexao.close() #8 Fechamento da conexão