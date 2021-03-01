import sqlite3
import servicos.espacoPessoa_servico as espacoPessoaServico
import servicos.salaPessoa_servico as salaPessoaServico
import servicos.espaco_servico as espacoServico
import servicos.sala_servico as salaServico


nome_db = "dados/evento.db"

def consultarPessoaPeloId(id_pessoa):
    
    consulta_sala = salaPessoaServico.obterSalasPessoasPeloId("pessoa", id_pessoa)
    consulta_espaco = espacoPessoaServico.obterEspacosPessoasPeloId("pessoa", id_pessoa)

    lista_consulta = []
    for i in consulta_sala:
        sala = salaServico.obterSalaPeloID(i[1])
        lista_consulta.append({"nome sala" : sala['nome'], "etapa" : i[3]})
    for i in consulta_espaco:
        espaco = espacoServico.obterEspacoPeloID(i[1])
        lista_consulta.append({"nome espaco" : espaco['nome'], "intervalo" : i[3]})
    tupla_consulta = tuple(lista_consulta)
        
    return (tupla_consulta)

def obterPessoas(): 
        
    conexao = sqlite3.connect("dados/evento.db")
    cursor = conexao.cursor()

    lista_pessoas = []
    pessoas = cursor.execute('''SELECT * FROM Pessoa''')
    for i in pessoas.fetchall():
        lista_pessoas.append({"id" : i[0], "nome" : i[1], "sobrenome" : i[2]})
    tupla_pessoas = tuple(lista_pessoas)

    conexao.close()
    return(tupla_pessoas)

def obterPessoaPeloID(id_pessoa): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    pessoa = cursor.execute('''SELECT * FROM Pessoa WHERE id = ?''', (id_pessoa,)).fetchone()
    if pessoa is None:
        valores_pessoa = None
    else:
        valores_pessoa = {"id" : pessoa[0], "nome" : pessoa[1], "sobrenome" : pessoa[2]}

    conexao.close()
    return(valores_pessoa)

def inserirPessoa(nome, sobrenome):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO Pessoa VALUES (NULL, ?, ?)''', (nome, sobrenome,))
        
    conexao.commit()
    conexao.close()
    return True

def editarPessoa(nome, sobrenome, id_pessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Pessoa SET nome = ?, sobrenome = ? WHERE id = ?''', (nome, sobrenome, id_pessoa))

    conexao.commit()
    conexao.close()
    return True

def deletarPessoa(id_pessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Pessoa WHERE id = ?''', (id_pessoa,))

    conexao.commit()
    conexao.close()
    return True
