import sqlite3
from flask_restful import Resource
from flask import request

class Sala:
    def __init__(self, nome, lotacao):
        self.nome = nome
        self.lotacao = lotacao

    def consultar_sala(self, nome):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        lista_pessoasetapas = []
        sala = cursor.execute('''SELECT * FROM SalaPessoa WHERE nome_sala = ?''', (nome,))
        for i in sala.fetchall():
            lista_pessoasetapas.append(("Pessoa: "+i[2], "Etapa: "+i[3]))

        conexao.close()
        return(lista_pessoasetapas)


class RegistroSala(Resource):
    def post(self):
        data = request.get_json()

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        # Chamar função para validar o registro *Aqui

        cursor.execute('''INSERT INTO Sala (NULL, ?, ?)''', (data['nome'], data['lotacao'],))

        conexao.commit()
        conexao.close()
