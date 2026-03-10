import sqlite3 as sql
from contextlib import closing

with sql.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM preços')
        '''
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f'Nome: {resultado[0]}\nPreço: {resultado[1]}')
            print('-'*20)
        '''
        for resultado in cursor.fetchall():
            print(f'Nome: {resultado[0]}\nPreço: {resultado[1]}')
            print('-'*20)