import sqlite3

def obterSalasPessoa(): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    salapessoa = cursor.execute('''SELECT * FROM SalaPessoa''').fetchall()

    conexao.close()
    return(salapessoa)

def obterSalaPessoaPeloID(id_salapessoa): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    salapessoa = cursor.execute('''SELECT * FROM SalaPessoa WHERE id = ?''', (id_salapessoa,)).fetchone()

    conexao.close()
    return(salapessoa)

def inserirSalaPessoa(id_sala, id_pessoa, etapa):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO SalaPessoa VALUES(NULL, ?, ?, ?)''', (id_sala, id_pessoa, etapa))
        
    conexao.commit()
    conexao.close()
    return True

def editarSalaPessoa(id_sala, id_pessoa, etapa, id_salapessoa: int):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE SalaPessoa SET id_sala = ?, id_pessoa = ?, etapa = ? WHERE id = ?''', (id_sala, id_pessoa, etapa, id_salapessoa))

    conexao.commit()
    conexao.close()
    return True

def deletarSalaPessoa(id_salapessoa: int):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM SalaPessoa WHERE id = ?''', (id_salapessoa,))

    conexao.commit()
    conexao.close()
    return True
