import sqlite3
nome_db = "dados/evento.db"


def obterSalasPessoas(): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_salaspessoas = []
    salaspessoas = cursor.execute('''SELECT * FROM SalaPessoa''')
    for i in salaspessoas.fetchall():
        lista_salaspessoas.append({"id" : i[0], "salaId" : i[1], "pessoaId" : i[2], "etapa" : i[3]})
    tupla_salaspessoas = tuple(lista_salaspessoas)

    conexao.close()
    return(tupla_salaspessoas)

def obterSalaPessoaPeloID(id_salapessoa): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    salapessoa = cursor.execute('''SELECT * FROM SalaPessoa WHERE id = ?''', (id_salapessoa,)).fetchone()
    salapessoa = {"id" : salapessoa[0], "salaId" : salapessoa[1], "pessoaId" : salapessoa[2], "etapa" : salapessoa[3]}

    conexao.close()
    return(salapessoa)

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
    return cursor

def deletarSalaPessoa(id_salapessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM SalaPessoa WHERE id = ?''', (id_salapessoa,))

    conexao.commit()
    conexao.close()
    return True
