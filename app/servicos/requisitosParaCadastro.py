import servicos.sala_servico as salaServico
import servicos.salaPessoa_servico as salaPessoaServico
import servicos.pessoa_servico as pessoaServico
import sqlite3

nome_db = "dados/evento.db"

def validarCadastroSala(id_sala, id_pessoa, etapa):    

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    quant_sala = salaPessoaServico.obterQuantidadeDeSalaPessoa(id_sala)
    sala = salaServico.obterSalaPeloID(id_sala)    
    ids_salas = salaServico.obterIdsSalas()
    pessoa = pessoaServico.obterPessoaPeloID(id_pessoa)
    pessoaSala = cursor.execute('''SELECT * FROM SalaPessoa WHERE id_pessoa = ? AND etapa = ?''', (id_pessoa, etapa)).fetchone()

    if etapa == 1:
        quantidade = []
        for i in ids_salas:
            quant = cursor.execute('''SELECT COUNT(*) FROM SalaPessoa WHERE id_sala = ?''', (i,)).fetchone()
            quantidade.append(quant[0])    
        conexao.close()

        if (((quant_sala + 1) - min(quantidade)) > 1) or ((quant_sala + 1) > sala['lotação']) or (pessoa is None) or (sala is None) or (pessoaSala is not None):
            return False

    elif etapa == 2:
        metade_sala = sala['lotação'] // 2
        quant_etapa2_sala = cursor.execute('''SELECT COUNT(*) FROM SalaPessoa WHERE id_sala = ? AND etapa = ?''', (id_sala, 2,)).fetchone()

        if (metade_sala - quant_etapa2_sala[0] == 0) or (pessoa is None) or (sala is None) or (pessoaSala is not None):
            return False
    else:
        return False

    return True

def validarCadastroEspaco(id_espaco, id_pessoa, intervalo):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    pessoa = pessoaServico.obterPessoaPeloID(id_pessoa)
    espaco = cursor.execute('''SELECT * FROM Espaco WHERE id = ?''', (id_espaco,)).fetchone()
    pessoaEspaco = cursor.execute('''SELECT * FROM EspacoPessoa WHERE id_pessoa = ? AND intervalo = ?''', (id_pessoa, intervalo,)).fetchone()
    quant_pessoaEspaco = cursor.execute('''SELECT COUNT(*) FROM EspacoPessoa WHERE id_espaco = ? AND intervalo = ?''', (id_espaco, intervalo,)).fetchone()

    conexao.close()
    if intervalo == 2 or intervalo == 1:
        if ((quant_pessoaEspaco[0] + 1) > espaco[2]) or (pessoaEspaco is not None) or (pessoa is None) or (espaco is None):
            return False
        return True
    return False


