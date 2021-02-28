import servicos.sala_servico as salaServico
import servicos.salaPessoa_servico as salaPessoaServico
import sqlite3

nome_db = "dados/evento.db"


def validarCadastroSala(id_sala):    

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    quant_sala = salaPessoaServico.obterQuantidadeDeSalaPessoa(id_sala)
    lotacao_sala = salaServico.obterSalaPeloID(id_sala)    
    ids_salas = salaServico.obterIdsSalas()

    quantidade = []
    for i in ids_salas:
        quant = cursor.execute('''SELECT COUNT(*) FROM SalaPessoa WHERE id_sala = ?''', (i,)).fetchone()
        quantidade.append(quant[0])    
    conexao.close()

    if (((quant_sala + 1) - min(quantidade)) > 1) or ((quant_sala + 1) > lotacao_sala['lotação']):
        return False
    return True
