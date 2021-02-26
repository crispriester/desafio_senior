from flask import Flask, request
from servicos import pessoa_servico, sala_servico, espaco_servico, espacoPessoa_servico, salaPessoa_servico

app = Flask("Treinamento")

# CONTROLADOR DE PESSOA

@app.route("/pessoa/consultar", methods=["GET"])
def consultarPessoas():

    return pessoa_servico.obterPessoas()


@app.route("/pessoa/consultar/id=<pessoaId>", methods=["GET"])
def consultarPessoaPeloID(pessoaId: int):

    return pessoa_servico.obterPessoaPeloID(pessoaId)


@app.route("/pessoa/cadastrar", methods=["POST"])
def cadastrarPessoa():

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("sobrenome" not in body):
        return gerarResposta(400, "O parâmetro 'sobrenome' é obrigatório.")

    pessoa = pessoa_servico.inserirPessoa(body["nome"], body["sobrenome"])

    return gerarResposta(200, "Pessoa inserida", "pessoa", pessoa)


@app.route("/pessoa/editar/id=<pessoaId>", methods=["PUT"])
def editarPessoa(pessoaId: int):

    body = request.get_json()

    pessoa_registrada = pessoa_servico.obterPessoaPeloID(pessoaId)

    if pessoa_registrada is None:
        return gerarResposta(400, "Essa pessoa não é registrada.")
    pessoa_servico.deletarPessoa(pessoaId)

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("sobrenome" not in body):
        return gerarResposta(400, "O parâmetro 'sobrenome' é obrigatório.")

    pessoa = pessoa_servico.editarPessoa(body["nome"], body["sobrenome"], pessoaId)

    return gerarResposta(200, "Pessoa editada", "pessoa", pessoa)


@app.route("/pessoa/remover/id=<pessoaId>", methods=["DELETE"])
def removerPessoa(pessoaId: int):

    pessoa_registrada = pessoa_servico.obterPessoaPeloID(pessoaId)

    if pessoa_registrada is None:
        return gerarResposta(400, "Essa pessoa não é registrada.")
    pessoa_servico.deletarPessoa(pessoaId)

    return gerarResposta(200, "Pessoa removida.")




# CONTROLADOR DE Sala

@app.route("/sala/consultar", methods=["GET"])
def consultarSalas():

    return sala_servico.obterSalas()


@app.route("/sala/consultar/id=<salaId>", methods=["GET"])
def consultarSalaPeloID(salaId: int):

    return sala_servico.obterSalaPeloID(salaId)


@app.route("/sala/cadastrar", methods=["POST"])
def cadastrarSala():

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("lotação" not in body):
        return gerarResposta(400, "O parâmetro 'lotação' é obrigatório.")

    sala = sala_servico.inserirSala(body["nome"], body["lotação"])

    return gerarResposta(200, "Sala inserida", "sala", sala)


@app.route("/sala/editar/id=<salaId>", methods=["PUT"])
def editarSala(salaId: int):

    body = request.get_json()

    sala_registrada = sala_servico.obterSalaPeloID(salaId)

    if sala_registrada is None:
        return gerarResposta(400, "Essa sala não é registrada.")
    sala_servico.deletarSala(salaId)

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("lotação" not in body):
        return gerarResposta(400, "O parâmetro 'lotação' é obrigatório.")

    sala = sala_servico.editarSala(body["nome"], body["lotação"], salaId)

    return gerarResposta(200, "Sala editada", "sala", sala)


@app.route("/sala/remover/id=<salaId>", methods=["DELETE"])
def removerSala(salaId: int):

    sala_registrada = sala_servico.obterSalaPeloID(salaId)

    if sala_registrada is None:
        return gerarResposta(400, "Essa sala não é registrada.")
    sala_servico.deletarSala(salaId)

    return gerarResposta(200, "Sala removida.")




# CONTROLADOR DE Espaço

@app.route("/espaco/consultar", methods=["GET"])
def consultarEspaco():

    return espaco_servico.obterEspacos()


@app.route("/espaco/consultar/id=<espacoId>", methods=["GET"])
def consultarEspacoPeloID(espacoId: int):

    return espaco_servico.obterEspacoPeloID(espacoId)


@app.route("/espaco/cadastrar", methods=["POST"])
def cadastrarEspaco():

    body = request.get_json()

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("lotação" not in body):
        return gerarResposta(400, "O parâmetro 'lotação' é obrigatório.")

    espaco = espaco_servico.inserirEspaco(body["nome"], body["lotação"])

    return gerarResposta(200, "Espaço inserido", "espaço", espaco)


@app.route("/espaco/editar/id=<espacoId>", methods=["PUT"])
def editarEspaco(espacoId: int):

    body = request.get_json()

    espaco_registrada = espaco_servico.obterEspacoPeloID(espacoId)

    if espaco_registrada is None:
        return gerarResposta(400, "Esse espaço não é registrado.")
    espaco_servico.deletarEspaco(espacoId)

    if("nome" not in body):
        return gerarResposta(400, "O parâmetro 'nome' é obrigatório.")
    
    if("lotação" not in body):
        return gerarResposta(400, "O parâmetro 'lotação' é obrigatório.")

    espaco = espaco_servico.editarEspaco(body["nome"], body["lotação"], espacoId)

    return gerarResposta(200, "Espaço editada", "espaço", espaco)


@app.route("/espaco/remover/id=<espacoId>", methods=["DELETE"])
def removerEspaco(espacoId: int):

    espaco_registrada = espaco_servico.obterEspacoPeloID(espacoId)

    if espaco_registrada is None:
        return gerarResposta(400, "Essa espaço não é registrado.")
    espaco_servico.deletarEspaco(espacoId)

    return gerarResposta(200, "Espaço removido.")



# CONTROLADOR DE EspacoPessoa

@app.route("/espacoPessoa/consultar", methods=["GET"])
def consultarEspacoPessoa():

    return espacoPessoa_servico.obterEspacosPessoa()


@app.route("/espacoPessoa/consultar/id=<espacoPessoaId>", methods=["GET"])
def consultarEspacoPessoaPeloID(espacoPessoaId: int):

    return espacoPessoa_servico.obterEspacoPessoaPeloID(espacoPessoaId)


@app.route("/espacoPessoa/cadastrar", methods=["POST"])
def cadastrarEspacoPessoa():

    body = request.get_json()

    if("espacoId" not in body):
        return gerarResposta(400, "O parâmetro 'espacoId' é obrigatório.")
    
    if("pessoaId" not in body):
        return gerarResposta(400, "O parâmetro 'pessoaId' é obrigatório.")

    if("intervalo" not in body):
        return gerarResposta(400, "O parâmetro 'intervalo' é obrigatório.")

    espacoPessoa = espacoPessoa_servico.inserirEspacoPessoa(body["espacoId"], body["pessoaId"], body["intervalo"])

    return gerarResposta(200, "EspaçoPessoa inserido", "espaçoPessoa", espacoPessoa)


@app.route("/espacoPessoa/editar/id=<espacoPessoaId>", methods=["PUT"])
def editarEspacoPessoa(espacoPessoaId: int):

    body = request.get_json()

    espacoPessoa_registrado = espacoPessoa_servico.obterEspacoPessoaPeloID(espacoPessoaId)

    if espacoPessoa_registrado is None:
        return gerarResposta(400, "Esse EspacoPessoa não é registrado.")

    if("espacoId" not in body):
        return gerarResposta(400, "O parâmetro 'espacoId' é obrigatório.")
    
    if("pessoaId" not in body):
        return gerarResposta(400, "O parâmetro 'pessoaId' é obrigatório.")

    if("intervalo" not in body):
        return gerarResposta(400, "O parâmetro 'intervalo' é obrigatório.")    

    espacoPessoa = espacoPessoa_servico.editarEspacoPessoa(body["espacoId"], body["pessoaId"], body["intervalo"], espacoPessoa_registrado)

    return gerarResposta(200, "EspaçoPessoa editado", "espaçoPessoa", espacoPessoa)


@app.route("/espacoPessoa/remover/id=<espacoPessoaId>", methods=["DELETE"])
def removerEspacoPessoa(espacoPessoaId: int):

    espacoPessoa_registrada = espacoPessoa_servico.obterEspacoPessoaPeloID(espacoPessoaId)

    if espacoPessoa_registrada is None:
        return gerarResposta(400, "Esse espaçoPessoa não é registrado.")
    espacoPessoa_servico.deletarEspacoPessoa(espacoPessoaId)

    return gerarResposta(200, "EspaçoPessoa removido.")




# CONTROLADOR DE SalaPessoa

@app.route("/salaPessoa/consultar", methods=["GET"])
def consultarSalaPessoa():

    return salaPessoa_servico.obterSalasPessoa()


@app.route("/salaPessoa/consultar/id=<salaPessoaId>", methods=["GET"])
def consultarSalaPessoaPeloID(salaPessoaId: int):

    return salaPessoa_servico.obterSalaPessoaPeloID(salaPessoaId)


@app.route("/salaPessoa/cadastrar", methods=["POST"])
def cadastrarSalaPessoa():

    body = request.get_json()

    if("salaId" not in body):
        return gerarResposta(400, "O parâmetro 'salaId' é obrigatório.")
    
    if("pessoaId" not in body):
        return gerarResposta(400, "O parâmetro 'pessoaId' é obrigatório.")

    if("etapa" not in body):
        return gerarResposta(400, "O parâmetro 'etapa' é obrigatório.")

    salaPessoa = salaPessoa_servico.inserirSalaPessoa(body["salaId"], body["pessoaId"], body["etapa"])

    return gerarResposta(200, "SalaPessoa inserido", "salaPessoa", salaPessoa)


@app.route("/salaPessoa/editar/id=<salaPessoaId>", methods=["PUT"])
def editarSalaPessoa(salaPessoaId: int):

    body = request.get_json()

    salaPessoa_registrado = salaPessoa_servico.obterSalaPessoaPeloID(salaPessoaId)

    if salaPessoa_registrado is None:
        return gerarResposta(400, "Essa SalaPessoa não é registrada.")

    if("salaId" not in body):
        return gerarResposta(400, "O parâmetro 'salaId' é obrigatório.")
    
    if("pessoaId" not in body):
        return gerarResposta(400, "O parâmetro 'pessoaId' é obrigatório.")

    if("etapa" not in body):
        return gerarResposta(400, "O parâmetro 'etapa' é obrigatório.")    

    salaPessoa = salaPessoa_servico.editarSalaPessoa(body["salaId"], body["pessoaId"], body["etapa"], salaPessoa_registrado)

    return gerarResposta(200, "SalaPessoa editada", "salaPessoa", salaPessoa)


@app.route("/salaPessoa/remover/id=<salaPessoaId>", methods=["DELETE"])
def removerSalaPessoa(salaPessoaId: int):

    salaPessoa_registrada = salaPessoa_servico.obterSalaPessoaPeloID(salaPessoaId)

    if salaPessoa_registrada is None:
        return gerarResposta(400, "Essa salaPessoa não é registrada.")
    salaPessoa_servico.deletarSalaPessoa(salaPessoaId)

    return gerarResposta(200, "SalaPessoa removida.")




# FUNÇÃO PARA EFETUAR RESPOSTAS

def gerarResposta(status, mensagem, nome_do_conteudo=False, conteudo=False):

    resposta = {}
    resposta["status"] = status
    resposta["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        resposta[nome_do_conteudo] = conteudo

    return resposta


app.run()