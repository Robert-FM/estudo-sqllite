import sqlite3 as sql

dados = [
    ('Leite', 6.20),
    ('Café', 15.40),
    ('Açúcar', 4.30),
    ('Sal', 2.10),
    ('Óleo de soja', 7.80),
    ('Farinha de trigo', 5.60),
    ('Manteiga', 9.90),
    ('Queijo', 18.50),
    ('Presunto', 16.30),
    ('Pão francês', 12.00),
    ('Biscoito', 3.90),
    ('Chocolate', 6.70),
    ('Refrigerante', 7.50),
    ('Suco', 5.20),
    ('Água mineral', 2.50),
    ('Iogurte', 4.80),
    ('Cereal', 11.40),
    ('Molho de tomate', 3.60),
    ('Milho', 4.20),
    ('Ervilha', 3.80),
    ('Atum', 9.70),
    ('Sardinha', 6.90),
    ('Batata', 5.10),
    ('Cebola', 4.90),
    ('Tomate', 6.30),
    ('Alho', 12.80),
    ('Banana', 3.70),
    ('Maçã', 7.20),
    ('Laranja', 4.40),
    ('Abacaxi', 6.60),
    ('Mamão', 5.30),
    ('Melancia', 8.90)
]

conexao = sql.connect('preços.db')
cursor = conexao.cursor()
cursor.executemany('''
                   INSERT INTO preços (nome,preços) 
                   VALUES(?,?)
                   ''',dados)
conexao.commit()
cursor.close()
conexao.close

#executemay aceita uma lista de tuplas como parâmetro.x