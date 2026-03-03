import sqlite3 as sql
from contextlib import closing

with sql.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM agenda')

        while True:
            resultado = cursor.fetchone()

            if resultado is None:
                break
            print(f'Nome: {resultado[0]}\nTelefone: {resultado[1]}')