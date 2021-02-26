import sqlite3

def obterSalas(): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    salas = cursor.execute('''SELECT * FROM Salas''').fetchall()

    conexao.close()
    return(salas)

def obterSalaPeloID(id_sala): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    sala = cursor.execute('''SELECT * FROM Sala WHERE id = ?''', (id_sala,)).fetchone()

    conexao.close()
    return(sala)

def inserirSala(nome, lotacao):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO Pessoa VALUES(NULL, ?, ?)''', (nome, lotacao,))
        
    conexao.commit()
    conexao.close()
    return True

def editarSala(nome, lotacao, id_sala: int):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Pessoa SET nome = ?, lotacao = ? WHERE id = ?''', (nome, lotacao, id_sala))

    conexao.commit()
    conexao.close()
    return True

def deletarSala(id_sala: int):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Sala WHERE id = ?''', (id_sala,))

    conexao.commit()
    conexao.close()
    return True
