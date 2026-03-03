import sqlite3 as sql

conexao = sql.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM agenda')
resultado = cursor.fetchall() #1 retorna uma lista de tuplas com os resultados da consulta

for nome, telefone in resultado: #2 Pega as variáveis para exibir os dados.
    print(f'Nome: {nome}')
    print(f'Telefone: {telefone}')
    print('-' * 20)

cursor.close()
conexao.close()

