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
                       ''',('café','19.99'))
        cursor.execute('''INSERT INTO preços (nome, preços)
                       VALUES(?,?)
                       ''',('pão','10.99'))
        cursor.execute('''INSERT INTO preços (nome, preços)
                       VALUES(?,?)
                       ''',('areia','5.50'))