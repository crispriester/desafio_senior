import sqlite3

def obterPessoas(): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    pessoa = cursor.execute('''SELECT * FROM Pessoa''').fetchall()

    conexao.close()
    return(pessoa)

def obterPessoaPeloID(id_pessoa): 
        
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    pessoa = cursor.execute('''SELECT * FROM Pessoa WHERE id = ?''', (id_pessoa,)).fetchone()

    conexao.close()
    return(pessoa)

def inserirPessoa(nome, sobrenome):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO Pessoa VALUES(NULL, ?, ?)''', (nome, sobrenome,))
        
    conexao.commit()
    conexao.close()
    return True

def editarPessoa(nome, sobrenome, id_pessoa: int):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''UPDATE Pessoa SET nome = ?, sobrenome = ? WHERE id = ?''', (nome, sobrenome, id_pessoa))

    conexao.commit()
    conexao.close()
    return True

def deletarPessoa(id_pessoa: int):
    conexao = sqlite3.connect("evento.db")
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Pessoa WHERE id = ?''', (id_pessoa,))

    conexao.commit()
    conexao.close()
    return True
