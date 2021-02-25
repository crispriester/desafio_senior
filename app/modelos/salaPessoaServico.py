import sqlite3

class SalaPessoaServico():
    def __init__(self, id_sala, id_pessoa, etapa):
        self.id_sala = id_sala
        self.id_pessoa = id_pessoa
        self.etapa = etapa

    def verificar_lotacao_geral(self):        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        menor_lotacao = cursor.execute('''SELECT MIN(lotacao) FROM Sala''').fetchone()
        total_pessoas = cursor.execute('''SELECT COUNT(*) FROM Pessoa''').fetchone()[0]
        total_salas = cursor.execute('''SELECT COUNT(*) FROM Sala''').fetchone()[0]
        cursor.close()

        min_pessoas_sala = total_pessoas // total_salas

        if min_pessoas_sala > menor_lotacao:
            return {'mensagem' : 'Não há salas o suficiente.'}        
        #return verificar_lotacao_atual()

    def verificar_lotacao_atual(self):      
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        
        salas = cursor.execute('''SELECT * FROM Sala''')

        lotacao_atual_salas = []
        for i in salas.fetchall():
            lotacao = cursor.execute('''SELECT COUNT(*) FROM SalaPessoa WHERE nome_sala = %s''' % (i[1]))
            lotacao_atual_salas.append(lotacao.fetchone()[0])

        menor_lotacao_atual = min(lotacao_atual_salas)

        cursor.execute('''SELECT COUNT(*) FROM SalaPessoa WHERE id = ?''', (self.id_sala,))
        cursor.close()
        if (cursor.fetchone()[0] + 1) - menor_lotacao_atual > 1:
            return {'mensagem' : 'Não há mais lugares nesta sala. Cadastre a pessoa em outra sala.'}
        return True
    

        
