# # ARQUIVO USADO PARA ADMINISTRAR MANUALMENTE UMA BASE DE DADOS

# import sqlite3

# connection = sqlite3.connect('evento.db')

# connection.execute("PRAGMA foreign_keys = ON")

# with open('schema.sql') as f:
#     connection.executescript(f.read())

# connection.commit()
# connection.close()