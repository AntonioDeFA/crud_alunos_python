# Gerenciamento de Alunos em Python

Este repositório contém um projeto de gerenciamento de alunos desenvolvido em Python. O objetivo é fornecer uma solução para cadastro, manipulação e persistência de informações de alunos usando um banco de dados em formato JSON. O projeto utiliza as bibliotecas numpy e dependency_injector para otimização e injeção de dependências no container, respectivamente. Além de usar mvc para o organização dos aqruivos.

## Funcionalidades

O projeto oferece as seguintes funcionalidades:

- **Criar aluno**: Permite criar um novo aluno, fornecendo informações como nome e sobrenome.
- **Adicionar nota ao aluno**: Possibilita adicionar uma nota específica ao aluno pelo seu identificador único que é um UUID.
- **Remover ou editar nota de aluno**: Permite remover ou editar uma nota de um aluno existente.
- **Alterar dados do aluno**: Permite alterar as informações de um aluno, como nome, sobrenome e matricula.
- **Excluir aluno**: Remove um aluno do sistema com base no seu identificador único.
- **Listar aluno por ID**: Recupera e descreve com detalhes as informações de um aluno específico pelo seu identificador único.
- **Listar todos os alunos**: Retorna uma lista com todas as informações de todos os alunos cadastrados mostrando informações básicas sobre todos.

## Fluxo de execução

O projeto segue o seguinte fluxo de execução:

1. **Classe Main**: Responsável por inicializar o programa e controlar a interação com o usuário.
2. **Controller**: Faz a ponte entre a camada de apresentação (Main) e a camada de serviço (Service), recebendo e direcionando as requisições.
3. **Service**: Contém a lógica de negócio do sistema, realizando as operações necessárias usando os dados fornecidos.
4. **Persistência**: Responsável por armazenar e recuperar os dados dos alunos em um arquivo JSON.
5. **Arquivo de Log**: Gera registros de atividades importantes e os salva em um arquivo externo para fins de auditoria e rastreamento.

## Dependências

O projeto depende das seguintes bibliotecas:

- numpy: Utilizada para otimização de operações matemáticas como média dos alunos.
- dependency_injector: Utilizada para facilitar a injeção de dependências no código, criando um container responsável  por injetar as dependias sem criar acoplamento entre as classes.
  Obs: em src\requirements.txt é possível ver todas as bibliotecas utilizadas no projeto além de suas versões fixas, servindo também como arquivo de instalação de dependências.

## Testes Unitários

O projeto possui testes unitários para garantir a qualidade do código. Foram utilizados o pytest e o mock para criar e executar os testes. Os testes abrangem diferentes aspectos das funcionalidades implementadas, garantindo a corretude e robustez do sistema. Pode-se executa-los executando o comando 'pytest -v src/test' que também esta no arquivo Makefile.

## Utilização do Flake8 para Formatação de Código

Este projeto utiliza o Flake8 como uma ferramenta de análise estática e formatação de código Python, ajudando a manter um código limpo, legível e bem formatado. Para validar a formatação é só usar o camando 'flake8 --max-line-length=110 src' que também esta no arquivo Makefile.

O uso do Flake8 neste projeto garante que o código siga as melhores práticas de formatação e estilo recomendadas pela comunidade Python.

## Como usar

Para utilizar o projeto, siga os passos abaixo:

1. Clone o repositório para o seu ambiente local: `git clone https://github.com/AntonioDeFA/crud_alunos_python.git`
2. Certifique-se de ter as bibliotecas numpy e dependency_injector instaladas em seu ambiente Python, para isto use o comando `pip install -r .\src\requirements.txt` que também esta no arquivo Makefile.
3. Execute o arquivo `main.py` para iniciar o programa.
4. Siga as instruções apresentadas no console para interagir com as funcionalidades do sistema.
  Obs: Todos os comando usados para executar o projetor estão no arquivo Makefile.
