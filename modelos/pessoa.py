import sqlite3
from flask_restful import Resource
from flask import request

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def consultar_pessoas(self, nome):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        sala = cursor.execute('''SELECT * FROM Salas WHERE nome = ? and sobrenome = ?''', self.nome, self.sobrenome,).fetchall()
        espaco = cursor.execute('''SELECT * FROM Espaços_De_Café WHERE nome = ? and sobrenome = ?''', self.nome, self.sobrenome,).fetchall()

        conexao.close()
        return(f"Sala etapa 1: {sala[0][1]}. Sala etapa 2: {sala[1][1]}. Espaço intervalo 1: {espaco[0][1]}. Espaço intervalo 2: {espaco[1][1]}.")

class Registrar(Resource):
    def post(self):
        data = request.get_json()

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa (ID INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT)''')

        cursor.execute('''INSERT INTO Pessoa VALUES (NULL, ?, ?)''', (data['nome'], data['sobrenome'],))

        conexao.commit()
        conexao.close()
