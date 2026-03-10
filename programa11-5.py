import sqlite3 as sql
from contextlib import closing

nome = nome = input(f'Nome a Selecionar: ').strip().capitalize()

with sql.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM agenda WHERE nome = ?',(nome,))

        for resultado in cursor.fetchall():
            print(f'Nome: {resultado[0]}\nTelefone: {resultado[1]}')
            print('-'*20)