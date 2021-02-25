class PessoaServico:
    def obterPessoas(self): # não sei oq vai de parâmetro, daí coloquei self
        return "fazer o código pra retornar as pessoas e tal com o sqlite. isso é contigo moor! boa sorte :3 te amo"

    def inserirPessoa(@nome, @sobrenome)

        "INSERT INTO Pessoa VALUES(@nome, @sobrenome)"

    def editarPessoa(@pessoaId: int, @nome, @sobrenome)

        "UPDATE Pessoa SET nome = @nome, sobrenome = @sobrenome WHERE ID = @pessoaId"

    def deletarPessoa(@pessoaId: int)

        "DELETE FROM Pessoa WHERE id = @pessoaId"
