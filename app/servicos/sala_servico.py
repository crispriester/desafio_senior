import sqlite3
import servicos.salaPessoa_servico as salaPessoaServico
import servicos.pessoa_servico as pessoaServico
nome_db = "dados/evento.db"

def consultarSalasPeloId(id_sala):

    consulta = salaPessoaServico.obterSalasPessoasPeloId("sala", id_sala)
    
    lista_consulta = []
    for i in consulta:
        pessoa = pessoaServico.obterPessoaPeloID(i[2])
        lista_consulta.append({"nome pessoa" : pessoa['nome'], "etapa" : i[3]})
    tupla_consulta = tuple(lista_consulta)
        
    return (tupla_consulta)

def obterSalas(): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_salas = []
    salas = cursor.execute('''SELECT * FROM Sala''')
    for i in salas.fetchall():
        lista_salas.append({"id" : i[0], "nome" : i[1], "lotação" : i[2]})
    lista_salas = tuple(lista_salas)

    conexao.close()
    return(lista_salas)

def obterSalaPeloID(id_sala): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    sala = cursor.execute('''SELECT * FROM Sala WHERE id = ?''', (id_sala,)).fetchone()
    if sala is None:
        valores_sala = None
    else:
        valores_sala = {"id" : sala[0], "nome" : sala[1], "lotação" : sala[2]}

    conexao.close()
    return(valores_sala)

def obterIdsSalas():
    
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_salas = []
    salas = cursor.execute('''SELECT * FROM Sala''')
    for i in salas.fetchall():
        lista_salas.append(i[0])

    conexao.close()
    return (lista_salas)

def obterQuantidadeDeSalas():
    
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    ids_salas = []
    salas = cursor.execute('''SELECT * FROM Sala''')
    for i in salas.fetchall():
        ids_salas.append(i[0])
    
    conexao.close()
    return (ids_salas)

def inserirSala(nome, lotacao):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO Sala VALUES (NULL, ?, ?)''', (nome, lotacao,))
        
    conexao.commit()
    conexao.close()
    return True

def editarSala(nome, lotacao, id_sala: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Sala SET nome = ?, lotacao = ? WHERE id = ?''', (nome, lotacao, id_sala))

    conexao.commit()
    conexao.close()
    return True

def deletarSala(id_sala: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Sala WHERE id = ?''', (id_sala,))

    conexao.commit()
    conexao.close()
    return True
