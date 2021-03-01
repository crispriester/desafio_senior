import sqlite3
nome_db = "dados/evento.db"

def obterSalasPessoasPeloId(elemento, id_elemento):

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    para_sala = '''SELECT * FROM SalaPessoa WHERE id_sala = ?'''
    para_pessoa = '''SELECT * FROM SalaPessoa WHERE id_pessoa = ?'''

    if elemento == "sala":
        consultas = cursor.execute(para_sala, (id_elemento,)).fetchall()
    else:
        consultas = cursor.execute(para_pessoa, (id_elemento)).fetchall()

    return (consultas)

def obterSalasPessoas(): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_salas_pessoas = []
    salas_pessoas = cursor.execute('''SELECT * FROM SalaPessoa''')
    for i in salas_pessoas.fetchall():
        lista_salas_pessoas.append({"id" : i[0], "salaId" : i[1], "pessoaId" : i[2], "etapa" : i[3]})
    tupla_salas_pessoas = tuple(lista_salas_pessoas)

    conexao.close()
    return (tupla_salas_pessoas)

def obterSalaPessoaPeloID(id_salapessoa): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    sala_pessoa = cursor.execute('''SELECT * FROM SalaPessoa WHERE id = ?''', (id_salapessoa,)).fetchone()
    valores_sala_pessoa = {"id" : sala_pessoa[0], "salaId" : sala_pessoa[1], "pessoaId" : sala_pessoa[2], "etapa" : sala_pessoa[3]}

    conexao.close()
    return (valores_sala_pessoa)

def obterQuantidadeDeSalaPessoa(id_sala):
    
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
    
    quantidade = cursor.execute('''SELECT COUNT(*) FROM SalaPessoa WHERE id_sala = ?''', (id_sala,)).fetchone()

    conexao.close()
    return (quantidade[0])

def inserirSalaPessoa(id_sala, id_pessoa, etapa):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO SalaPessoa VALUES(NULL, ?, ?, ?)''', (id_sala, id_pessoa, etapa))
        
    conexao.commit()
    conexao.close()
    return True

def editarSalaPessoa(id_sala, id_pessoa, etapa, id_salapessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE SalaPessoa SET id_sala = ?, id_pessoa = ?, etapa = ? WHERE id = ?''', (id_sala, id_pessoa, etapa, id_salapessoa))

    conexao.commit()
    conexao.close()
    return True

def deletarSalaPessoa(id_salapessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM SalaPessoa WHERE id = ?''', (id_salapessoa,))

    conexao.commit()
    conexao.close()
    return True
