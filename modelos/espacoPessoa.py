import sqlite3
from flask_restful import Resource
from flask import request

class EspacoPessoa:
    def __init__(self, nome_espaco, nome_pessoa, etapa):
        self.nome_espaco = nome_espaco
        self.nome_pessoa = nome_pessoa
        self.etapa = etapa


class EspacoRegistrado(Resource):
    def post(self):
        data = request.get_json()

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        cursor.execute('''CREATE TABLE IF NOT EXISTS SalaPessoa (ID INTEGER PRIMARY KEY, nome_espaco TEXT, nome_pessoa TEXT, etapa INTEGER)''')

        #função para validar a entrada da pessoa no refeitório

        cursor.execute('''INSERT INTO Sala (NULL, ?, ?, ?)''', (data['nome_espaco'], data['nome_pessoa'], data['etapa'],))

        conexao.commit()
        conexao.close()
