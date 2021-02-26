# ARQUIVO USADO PARA ADMINISTRAR MANUALMENTE UMA BASE DE DADOS

import sqlite3

connection = sqlite3.connect('db_treinamento.db')

connection.execute("PRAGMA foreign_keys = ON")

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("INSERT INTO Pessoa (nome, sobrenome) VALUES (?, ?)",
            ('Matheus', 'Marchi Moro')
            )

cursor.execute("INSERT INTO Pessoa (nome, sobrenome) VALUES (?, ?)",
            ('Cristina', 'Priester')
            )

connection.commit()
connection.close()