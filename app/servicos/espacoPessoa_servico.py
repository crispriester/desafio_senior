import sqlite3

class EspacoPessoaServico:
    def obterEspacosPessoa(self): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        espacopessoa = cursor.execute('''SELECT * FROM EspacoPessoa''').fetchall()

        conexao.close()
        return(espacopessoa)

    def obterEspacoPessoaPeloID(self, id_espacopessoa): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        espacopessoa = cursor.execute('''SELECT * FROM EspacoPessoa WHERE id = ?''', (id_espacopessoa,)).fetchone()

        conexao.close()
        return(espacopessoa)

    def inserirEspacoPessoa(self, id_espaco, id_pessoa, etapa):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO EspacoPessoa VALUES(NULL, ?, ?, ?)''', (id_espaco, id_pessoa, etapa))
        
        conexao.commit()
        conexao.close()

    def editarEspacoPessoa(self, id_espaco, id_pessoa, etapa, id_espacopessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''UPDATE EspacoPessoa SET nome = ?, id_pessoa = ?, etapa = ? WHERE id = ?''', (id_espaco, id_pessoa, etapa, id_espacopessoa))

        conexao.commit()
        conexao.close()

    def deletarEspacoPessoa(self, id_espacopessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''DELETE FROM EspacoPessoa WHERE id = ?''', (id_espacopessoa,))

        conexao.commit()
        conexao.close()
