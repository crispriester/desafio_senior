import sqlite3
nome_db = "dados/evento.db"


def obterEspacosPessoasPeloId(elemento, id_elemento):

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    para_espaco = '''SELECT * FROM EspacoPessoa WHERE id_espaco = ?'''
    para_pessoa = '''SELECT * FROM EspacoPessoa WHERE id_pessoa = ?'''

    if elemento == "espaco":
        consultas = cursor.execute(para_espaco, (id_elemento,)).fetchall()
    else:
        consultas = cursor.execute(para_pessoa, (id_elemento)).fetchall()

    return (consultas)

def obterEspacosPessoa(): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_espacos_pessoas = []
    espacos_pessoas = cursor.execute('''SELECT * FROM EspacoPessoa''')
    for i in espacos_pessoas.fetchall():
        lista_espacos_pessoas.append({"id" : i[0], "espacoId" : i[1], "pessoaId" : i[2], "etapa" : i[3]})
    tupla_espacos_pessoas = tuple(lista_espacos_pessoas)

    conexao.close()
    return(tupla_espacos_pessoas)

def obterEspacoPessoaPeloID(id_espacopessoa): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    espaco_pessoa = cursor.execute('''SELECT * FROM SalaPessoa WHERE id = ?''', (id_espacopessoa,)).fetchone()
    valores_espaco_pessoa = {"id" : espaco_pessoa[0], "salaId" : espaco_pessoa[1], "pessoaId" : espaco_pessoa[2], "etapa" : espaco_pessoa[3]}

    conexao.close()
    return (valores_espaco_pessoa)

def inserirEspacoPessoa(id_espaco, id_pessoa, etapa):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO EspacoPessoa VALUES(NULL, ?, ?, ?)''', (id_espaco, id_pessoa, etapa))
        
    conexao.commit()
    conexao.close()
    return True

def editarEspacoPessoa(id_espaco, id_pessoa, etapa, id_espacopessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE EspacoPessoa SET nome = ?, id_pessoa = ?, etapa = ? WHERE id = ?''', (id_espaco, id_pessoa, etapa, id_espacopessoa))

    conexao.commit()
    conexao.close()
    return True

def deletarEspacoPessoa(id_espacopessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM EspacoPessoa WHERE id = ?''', (id_espacopessoa,))

    conexao.commit()
    conexao.close()
    return True
