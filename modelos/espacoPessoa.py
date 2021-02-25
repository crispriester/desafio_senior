import sqlite3
from flask_restful import Resource
from flask import request

class EspacoPessoa:
    def __init__(self, id_espaco, id_pessoa, intervalo):
        self.id_espaco = nome_espaco
        self.id_pessoa = nome_pessoa
        self.intervalo = intervalo


class RegistroEspacoPessoa(Resource):
    def post(self):
        data = request.get_json()

        id_espaco = data['id_espaco']
        id_pessoa = data['id_pessoa']
        intervalo = data['intervalo']

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        # Chamar função para validar o registro *Aqui
        
        cursor.execute('''INSERT INTO EspacoPessoa (NULL, ?, ?, ?)''', (id_espaco, id_pessoa, intervalo,))

        conexao.commit()
        conexao.close()
