from flask import Flask, request

from servicos import obterPessoas, inserirPessoa, editarPessoa, deletarPessoa

app = Flask("Treinamento")


# CONTROLADOR DE PESSOA
#
@app.route("/pessoa/consultar", methods=["GET"])
def consultarPessoas():
    return obterPessoas()

@app.route("/pessoa/cadastrar", methods=["POST"])
def cadastrarPessoa():

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório")
    
    if("sobrenome" not in body):
        return gerarResposta(400, "O parâmetro 'sobrenome' é obrigatório")

    pessoa = inserirPessoa(body["nome"], body["sobrenome"])

    return gerarResposta(200, "Pessoa inserida", "pessoa", pessoa)

@app.route("/pessoa/editar/id=<pessoaId>", methods=["PUT"])
def removerPessoa(pessoaId):

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório")
    
    if("sobrenome" not in body):
        return gerarResposta(400, "O parâmetro 'sobrenome' é obrigatório")

    pessoa = editarPessoa(body["nome"], body["sobrenome"])

    return gerarResposta(200, "Pessoa editada", "pessoa", pessoa)

@app.route("/pessoa/remover/id=<pessoaId>", methods=["DELETE"])
def removerPessoa(pessoaId):

    return deletarPessoa(pessoaId)


# FUNÇÃO PARA EFETUAR RESPOSTAS
#
def gerarResposta(status, mensagem, nome_do_conteudo=False, conteudo=False):
    resposta = {}
    resposta["status"] = status
    resposta["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        resposta[nome_do_conteudo] = conteudo

    return resposta


app.run()