import sqlite3
nome_db = "dados/evento.db"


def obterEspacos(): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    lista_espacos = []
    espacos = cursor.execute('''SELECT * FROM Espaco''')
    for i in espacos.fetchall():
        lista_espacos.append({"id" : i[0], "nome" : i[1], "lotação" : i[2]})
    lista_espacos = tuple(lista_espacos)

    conexao.close()
    return(lista_espacos)

def obterEspacoPeloID(id_espaco): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    espaco = cursor.execute('''SELECT * FROM Espaco WHERE id = ?''', (id_espaco,)).fetchone()
    espaco = {"id" : espaco[0], "nome" : espaco[1], "lotação" : espaco[2]}

    conexao.close()
    return(espaco)

def inserirEspaco(nome, lotacao):

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO Espaco VALUES(NULL, ?, ?)''', (nome, lotacao,))
        
    conexao.commit()
    conexao.close()
    return True

def editarEspaco(nome, lotacao, id_espaco: int):

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Espaco SET nome = ?, lotacao = ? WHERE id = ?''', (nome, lotacao, id_espaco,))

    conexao.commit()
    conexao.close()
    return True

def deletarEspaco(id_espaco: int):

    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Espaco WHERE id = ?''', (id_espaco,))

    conexao.commit()
    conexao.close()
    return True
