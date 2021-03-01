# desafio_treinamento  
## Descrição do Projeto:  
Neste projeto foi criada uma API com a linguagem Python, utilizando o editor de código-fonte Visual Studio Code. Para criar requisições foi utilizado o programa Postman.  

## O sistema deve permitir:  
- o cadastro de pessoas com nome e sobrenome;  
- o cadastro de salas do evendo com nome e lotação;  
- o cadastro de espaços de café com nome e lotação.  

A diferença de pessoas em cada sala deverá ser de no máximo 1 pessoa. Para estimular a troca de conhecimentos, metade das pessoas precisam trocar de sala entre as duas etapas do treinamento.  
Ao consultar uma pessoa cadastrada no treinamento, o sistema deverá retornar à sala em que a pessoa ficará em cada etapa e o espaço onde ela realizará cada intervalo de café.  
Ao consultar uma sala cadastrada ou um espaço de café, o sistema deverá retornar uma lista das pessoas que estarão naquela sala ou espaço em cada etapa do evento.  

## Como rodar a aplicação:  
Para instalar o Flask, digite: pip install Flask no terminal.  
O usuário deve usar o programa Postman como a "interface" da API.  
Primeiramente, pelo Visual Studio Code, deve-se rodar o arquivo subir_banco.py (desafio_treinamento/app/dados/subir_banco). Certifique-se de que o diretório está em (desafio_treinamento/app) para rodar corretamente. Depois vá para o arquivo routes.py (desfio_treinamento/app) e o execute. Por fim, vá para o Postman para cadastrar, consultar e obter as pessoas, salas e espaços. 
