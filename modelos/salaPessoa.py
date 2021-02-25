import sqlite3
from flask_restful import Resource
from flask import request
import salaPessoaServico

class SalaPessoa:
    def __init__(self, id_sala, id_pessoa, etapa):
        self.id_sala = id_sala
        self.id_pessoa = id_pessoa
        self.etapa = etapa


class RegistroSalaPessoa(Resource):
    def post(self):
        data = request.get_json()
        
        id_sala = data['Id_sala']
        id_pessoa = data['id_pessoa']
        etapa = data['etapa']

        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
                
        # Chamar função para validar o registro *Aqui

        classe = salaPessoaServico.SalaPessoaServico(id_sala, id_pessoa, etapa)

        if SalaPessoaServico.verificar_lotacao_geral() == True: 
            cursor.execute('''INSERT INTO SalaPessoa (NULL, ?, ?, ?)''', (id_sala, id_pessoa, etapa,))

        conexao.commit()
        conexao.close()
