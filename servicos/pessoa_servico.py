import sqlite3

class PessoaServico:
    def obterPessoas(self, nome, sobrenome): 
        
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        pessoa = cursor.execute('''SELECT * FROM Pessoa WHERE nome = ? AND sobrenome = ?''', (nome, sobrenome,)).fetchone()
        sala = cursor.execute('''SELECT * FROM Salas WHERE pessoa_id = ?''', (pessoa[0])).fetchall()
        espaco = cursor.execute('''SELECT * FROM Espaços_De_Café WHERE pessoa_id = ?''', (pessoa[0])).fetchall()

        conexao.close()
        return(f"Sala etapa 1: {sala[0][1]}. Sala etapa 2: {sala[1][1]}. Espaço intervalo 1: {espaco[0][1]}. Espaço intervalo 2: {espaco[1][1]}.")

    def inserirPessoa(self, nome, sobrenome):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO Pessoa VALUES(NULL, ?, ?)''', (nome, sobrenome,))
        conexao.close()
        return {'mensagem' : 'Pessoa inserida com sucesso!'}

    def editarPessoa(self, nome, sobrenome, id_pessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''UPDATE Pessoa SET nome = ?, sobrenome = ? WHERE ID = ?''', (nome, sobrenome, id_pessoa))
        conexao.close()
        return {'mensagem' : 'Pessoa editada com sucesso!'}

    def deletarPessoa(self, id_pessoa: int):
        conexao = sqlite3.connect("evento.db")
        cursor = conexao.cursor()
        
        cursor.execute('''DELETE FROM Pessoa WHERE id = ?''', (id_pessoa,))
        conexao.close()
        return {'mensagem' : 'Pessoa deletada com sucesso!'}
