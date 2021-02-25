import sqlite3
from flask_restful import Resource
from flask import request

class SalaPessoa:
    def __init__(self, nome_sala, nome_pessoa, etapa):
        self.nome_sala = nome_sala
        self.nome_pessoa = nome_pessoa
        self.etapa = etapa


class RegistroSalaPessoa(Resource):
    def post(self):
        data = request.get_json()

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        cursor.execute('''CREATE TABLE IF NOT EXISTS SalaPessoa (ID INTEGER PRIMARY KEY, nome_sala TEXT, nome_pessoa TEXT, etapa INTEGER)''')

        #função para validar a entrada da pessoa na sala

        cursor.execute('''INSERT INTO Sala (NULL, ?, ?, ?)''', (data['nome_sala'], data['nome_pessoa'], data['etapa'],))

        conexao.commit()
        conexao.close()
