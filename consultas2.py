import sqlite3 as sql
from contextlib import closing 

with sql.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        
        preco1= input(f'Digite o menor preço a listar: ')
        preco2= input(f'Digite o maior preço a listar: ')

        cursor.execute('SELECT * FROM preços WHERE preços >= ? AND preços <= ?',(preco1,preco2))
            
        x = 0

        for resultado in cursor.fetchall():
            print(f'Produto: {resultado[0]}\nPreço: {resultado[1]}')
            print('-' * 20)
            x += 1
            
        if x == 0:
            print("Não encontrado.")
        else:
            print(f"{x} produto(s) encontrado(s).")
