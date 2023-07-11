import os
import pytest
from unittest.mock import Mock
from app.persistence.persistencia import Persistencia

payload_aluno = {
    "matricula": "1e9cd",
    "nome": "José",
    "sobrenome": "Gabriel",
    "notas": [10, 7]
}


def logger_mock():
    return Mock()


def test_iniciar_persistencia_sucesso():
    persistence = Persistencia(logger_mock())

    resultado = persistence._iniciar()

    assert resultado is None


def test_iniciar_persistencia_com_nome_teste_sucesso():
    Persistencia.NOME_ARQUIVO = "teste.txt"

    persistence = Persistencia(logger_mock())

    resultado = persistence._iniciar()

    assert resultado is None

    os.remove(Persistencia.NOME_ARQUIVO)

    Persistencia.NOME_ARQUIVO = "Aluno.json"


def test_carregar_persistencia_sucesso():
    persistence = Persistencia(logger_mock())

    resultado = persistence._carregar()

    assert resultado is None


def test_carregar_persistencia_nome_errado_excecao():
    persistence = Persistencia(logger_mock())

    Persistencia.NOME_ARQUIVO = "teste.txt"

    with pytest.raises(Exception) as error:
        persistence._carregar()

    assert str(error.value) == "exceptions must derive " \
                               "from BaseException"

    Persistencia.NOME_ARQUIVO = "Aluno.json"


def test_carregar_persistencia_arquivo_vazio_excecao():
    persistence = Persistencia(logger_mock())

    with open(Persistencia.NOME_ARQUIVO, "w",
              encoding="utf-8") as arquivo:
        arquivo.write("")

    resultado = persistence._carregar()

    assert resultado is None


def test_criar_aluno_preenchido_sucesso():
    persistence = Persistencia(logger_mock())

    resultado = persistence.criar(payload_aluno)

    assert resultado is None


def test_criar_aluno_vazio_excecao():
    persistence = Persistencia(logger_mock())

    with pytest.raises(KeyError) as error:
        persistence.criar({})

    assert str(error.value) == "'matricula'"


def test_criar_aluno_campo_nome_vazio_sucesso():
    persistence = Persistencia(logger_mock())

    payload_aluno["nome"] = ""

    resultado = persistence.criar(payload_aluno)

    assert resultado is None


def test_atualizar_aluno_preenchido_sucesso():
    persistence = Persistencia(logger_mock())

    payload_aluno['nome'] = "Maria"

    resultado = persistence.atualizar(
        "1e9cd",
        payload_aluno)

    assert resultado is None


def test_atualizar_aluno_matricula_vazia_excecao():
    persistence = Persistencia(logger_mock())

    with pytest.raises(Exception) as error:
        persistence.atualizar(None, payload_aluno)

    assert str(error.value) == "Não existe nenhum " \
                               "registro com matrícula: None"


def test_atualizar_aluno_matricula_nao_existente_excecao():
    persistence = Persistencia(logger_mock())

    with pytest.raises(Exception) as error:
        persistence.atualizar("123456", payload_aluno)

    assert str(error.value) == "Não existe nenhum " \
                               "registro com matrícula: 123456"


def test_deletar_aluno_matricula_certa_sucessso():
    persistence = Persistencia(logger_mock())

    resultado = persistence.deletar("1e9cd")

    assert resultado is None


def test_deletar_aluno_matricula_nao_existente_excecao():
    persistence = Persistencia(logger_mock())

    with pytest.raises(Exception) as error:
        persistence.deletar("123456")

    assert str(error.value) == "Não existe nenhum " \
                               "registro com matrícula: 123456"


def test_deletar_aluno_matricula_none_excecao():
    persistence = Persistencia(logger_mock())

    with pytest.raises(Exception) as error:
        persistence.deletar(None)

    assert str(error.value) == "Não existe nenhum " \
                               "registro com matrícula: None"


def test_listar_todos_alunos_sucessso():
    persistence = Persistencia(logger_mock())
    persistence.criar(payload_aluno)

    resultado = persistence.listar_todos()

    assert resultado is not None


def test_listar_todos_alunos_excecao():
    persistence = Persistencia(logger_mock())
    persistence._carregar()

    persistence.alunos = []

    with pytest.raises(Exception) as error:
        persistence.listar_todos()

    assert str(error.value) == "Não existe nenhum " \
                               "aluno cadastrado ainda."


def test_listar_um_aluno_por_mtaricula_sucessso():
    persistence = Persistencia(logger_mock())
    persistence._carregar()

    resultado = persistence.listar_um("1e9cd")

    assert resultado is not None


def test_listar_um_aluno_por_mtaricula_nao_existente_excecao():
    persistence = Persistencia(logger_mock())
    persistence._carregar()

    with pytest.raises(Exception) as error:
        persistence.listar_um("123456")

    assert str(error.value) == "Não existe nenhum " \
                               "registro com matrícula: 123456"


def test_listar_um_aluno_por_mtaricula_none_excecao():
    persistence = Persistencia(logger_mock())
    persistence._carregar()

    with pytest.raises(Exception) as error:
        persistence.deletar(None)

    assert str(error.value) == "Não existe nenhum " \
                               "registro com matrícula: None"


def test_salvar_preenchido_sucessso():
    persistence = Persistencia(logger_mock())

    resultado = persistence._salvar(payload_aluno)

    assert resultado is None


def test_salvar_vazio_sucessso():
    persistence = Persistencia(logger_mock())

    resultado = persistence._salvar()

    assert resultado is None
