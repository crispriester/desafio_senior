import sqlite3
nome_db = "dados/evento.db"

def obterPessoas(): 
        
    conexao = sqlite3.connect("dados/evento.db")
    cursor = conexao.cursor()

    lista_pessoas = []
    pessoas = cursor.execute('''SELECT * FROM Pessoa''')
    for i in pessoas.fetchall():
        lista_pessoas.append({"id" : i[0], "nome" : i[1], "sobrenome" : i[2]})
    lista_pessoas = tuple(lista_pessoas)

    conexao.close()
    return(lista_pessoas)

def obterPessoaPeloID(id_pessoa): 
        
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()

    pessoa = cursor.execute('''SELECT * FROM Pessoa WHERE id = ?''', (id_pessoa,)).fetchone()
    pessoa = {"id" : pessoa[0], "nome" : pessoa[1], "sobrenome" : pessoa[2]}

    conexao.close()
    return(pessoa)

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
    return cursor

def deletarPessoa(id_pessoa: int):
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
        
    cursor.execute('''DELETE FROM Pessoa WHERE id = ?''', (id_pessoa,))

    conexao.commit()
    conexao.close()
    return True
