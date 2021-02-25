import sqlite3
from flask_restful import Resource
from flask import request

class Espaco:
    def __init__(self, nome, lotacao):
        self.nome = nome
        self.lotacao = lotacao

    def consultar_espaco(self, nome):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        lista_pessoasespaco = []
        sala = cursor.execute('''SELECT * FROM EspacoPessoa WHERE nome_espaco = ?''', (nome,))
        for i in sala.fetchall():
            lista_pessoasespaco.append(("Pessoa: "+i[2], "Intervalo: "+i[3]))

        conexao.close()
        return(lista_pessoasespaco)


class RegistroEspaco(Resource):
    def post(self):
        data = request.get_json()

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        cursor.execute('''CREATE TABLE IF NOT EXISTS Espaco (ID INTEGER PRIMARY KEY, nome TEXT, lotacao INTEGER)''')

        cursor.execute('''INSERT INTO Espaco (NULL, ?, ?)''', (data['nome'], data['lotacao'],))

        conexao.commit()
        conexao.close()
