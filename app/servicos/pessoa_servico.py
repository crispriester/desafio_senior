import sqlite3

class PessoaServico:
    def obterPessoas(self): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        pessoa = cursor.execute('''SELECT * FROM Pessoa''').fetchall()

        conexao.close()
        return(pessoa)

    def obterPessoaPeloID(self, id_pessoa): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        pessoa = cursor.execute('''SELECT * FROM Pessoa WHERE id = ?''', (id_pessoa,)).fetchone()

        conexao.close()
        return(pessoa)

    def inserirPessoa(self, nome, sobrenome):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO Pessoa VALUES(NULL, ?, ?)''', (nome, sobrenome,))
        
        conexao.commit()
        conexao.close()

    def editarPessoa(self, nome, sobrenome, id_pessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''UPDATE Pessoa SET nome = ?, sobrenome = ? WHERE id = ?''', (nome, sobrenome, id_pessoa))

        conexao.commit()
        conexao.close()

    def deletarPessoa(self, id_pessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''DELETE FROM Pessoa WHERE id = ?''', (id_pessoa,))

        conexao.commit()
        conexao.close()
