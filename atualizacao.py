import sqlite3 as sql
from contextlib import closing

with sql.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''UPDATE agenda 
                       SET telefone = "12345-6789" 
                       WHERE nome = "Nilo" ''')

    conexao.commit()