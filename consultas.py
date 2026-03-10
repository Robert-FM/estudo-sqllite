import sqlite3 as sql
from contextlib import closing 

with sql.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        
        while True:
            nome = input(f'Digite o produto: ')

            if not nome:
                print(f'Fim da consulta!')
                break

            cursor.execute('SELECT * FROM preços WHERE nome = ?',(nome,))
            
            x = 0

            for resultado in cursor.fetchall():
                print(f'Produto: {resultado[0]}\nPreço: {resultado[1]}')
                x += 1
            
            if x == 0:
                print("Não encontrado.")
            else:
                print(f"{x} produto(s) encontrado(s).")
