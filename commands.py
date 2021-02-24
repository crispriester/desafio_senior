# CLASSE USADA PARA ADMINISTRAR MANUALMENTE A BASE DE DADOS

import sqlite3

try:
    banco = sqlite3.connect('basededados.db')

    cursor = banco.cursor()

    cursor.execute("CREATE TABLE Pessoa(id integener identity(1, 1), nome text, sobrenome text)")

    cursor.execute("INSERT INTO Pessoa(nome, sobrenome) VALUES ('Matheus', 'Marchi Moro')")

    banco.commit()

    cursor.execute("SELECT * FROM Pessoa")

except sqlite3.Error as erro:
    print(erro)