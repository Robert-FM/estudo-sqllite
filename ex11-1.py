import sqlite3 as sql
from contextlib import closing

with sql.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                       CREATE TABLE preços(
                       nome TEXT,
                       preços NUMERIC)
                       ''')
        cursor.execute('''INSERT INTO preços (nome, preços)
                       VALUES(?,?)
                       ''',('Arroz','25.90'))
        cursor.execute('''INSERT INTO preços (nome, preços)
                       VALUES(?,?)
                       ''',('Feijão','8.50'))
        cursor.execute('''INSERT INTO preços (nome, preços)
                       VALUES(?,?)
                       ''',('Macarrão','4.75'))