import sqlite3

class SalaServico:
    def obterSalas(self): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        salas = cursor.execute('''SELECT * FROM Salas''').fetchall()

        conexao.close()
        return(salas)

    def obterSalaPeloID(self, id_sala): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        sala = cursor.execute('''SELECT * FROM Sala WHERE id = ?''', (id_sala,)).fetchone()

        conexao.close()
        return(sala)

    def inserirSala(self, nome, lotacao):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO Pessoa VALUES(NULL, ?, ?)''', (nome, lotacao,))
        
        conexao.commit()
        conexao.close()

    def editarSala(self, nome, lotacao, id_sala: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''UPDATE Pessoa SET nome = ?, lotacao = ? WHERE id = ?''', (nome, lotacao, id_sala))

        conexao.commit()
        conexao.close()

    def deletarPessoa(self, id_sala: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''DELETE FROM Sala WHERE id = ?''', (id_sala,))

        conexao.commit()
        conexao.close()
