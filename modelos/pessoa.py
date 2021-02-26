import sqlite3
from flask_restful import Resource
from flask import request

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class RegistroPessoa(Resource):
    def post(self):
        data = request.get_json()

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        cursor.execute('''INSERT INTO Pessoa VALUES (NULL, ?, ?)''', (data['nome'], data['sobrenome'],))

        conexao.commit()
        conexao.close()
