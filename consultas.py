import sqlite3 as sql
from contextlib import closing 

with sql.connect('preços.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        
        parar = 's'
        while parar == 's':
            nome = input(f'Digite o produto: ').strip().capitalize()
            
            cursor.execute('SELECT * FROM preços WHERE nome = ?',(nome,))
            
            x = 0

            for resultado in cursor.fetchall():
                print(f'Produto: {resultado[0]}\nPreço: {resultado[1]}')
                x += 1
            
            if x == 0:
                print("Não encontrado.")
            else:
                print(f"{x} produto(s) encontrado(s).")

            parar = input(f'Você deseja continuar a pesquisa [s/n]: ').strip().lower()
    
    print(f'Fim da pesquisa!')
