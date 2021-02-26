import sqlite3

class SalaPessoaServico:
    def obterSalasPessoa(self): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        salapessoa = cursor.execute('''SELECT * FROM SalaPessoa''').fetchall()

        conexao.close()
        return(salapessoa)

    def obterSalaPessoaPeloID(self, id_salapessoa): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        salapessoa = cursor.execute('''SELECT * FROM SalaPessoa WHERE id = ?''', (id_salapessoa,)).fetchone()

        conexao.close()
        return(salapessoa)

    def inserirSalaPessoa(self, id_sala, id_pessoa, etapa):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO SalaPessoa VALUES(NULL, ?, ?, ?)''', (id_sala, id_pessoa, etapa))
        
        conexao.commit()
        conexao.close()

    def editarSalaPessoa(self, id_sala, id_pessoa, etapa, id_salapessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''UPDATE SalaPessoa SET id_sala = ?, id_pessoa = ?, etapa = ? WHERE id = ?''', (id_sala, id_pessoa, etapa, id_salapessoa))

        conexao.commit()
        conexao.close()

    def deletarSalaPessoa(self, id_salapessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''DELETE FROM SalaPessoa WHERE id = ?''', (id_salapessoa,))

        conexao.commit()
        conexao.close()
