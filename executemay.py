import sqlite3 as sql

dados = [('João','98901-0109'),
         ('André','98902-8900'),
         ('Maria','97891-3321'),
         ('Robert','9781-5523')]

conexao = sql.connect('agenda.db')
cursor = conexao.cursor()
cursor.executemany('''
                   INSERT INTO agenda (nome,telefone) 
                   VALUES(?,?)
                   ''',dados)
conexao.commit()
cursor.close()
conexao.close

#executemay aceita uma lista de tuplas como parâmetro.