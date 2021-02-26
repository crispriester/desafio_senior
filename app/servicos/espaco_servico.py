import sqlite3

def obterEspacos(): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    espacos = cursor.execute('''SELECT * FROM Espacos''').fetchall()

    conexao.close()
    return(espacos)

def obterEspacoPeloID(id_espaco): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    espaco = cursor.execute('''SELECT * FROM Espacos WHERE id = ?''', (id_espaco,)).fetchone()

    conexao.close()
    return(espaco)

def inserirEspaco(nome, lotacao):

    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO Espaco VALUES(NULL, ?, ?)''', (nome, lotacao,))
        
    conexao.commit()
    conexao.close()
    return True

def editarEspaco(nome, lotacao, id_espaco: int):

    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Espaco SET nome = ?, lotacao = ? WHERE id = ?''', (nome, lotacao, id_espaco,))

    conexao.commit()
    conexao.close()
    return True

def deletarEspaco(id_espaco: int):

    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Espacos WHERE id = ?''', (id_espaco,))

    conexao.commit()
    conexao.close()
    return True
