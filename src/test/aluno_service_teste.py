import pytest
from unittest.mock import Mock
from app.service.aluno_service import AlunoService
from app.utils.validador_entrada import ValidadorEntrada

payload_valores_dict = {
    "matricula": "1e9cd",
    "nome": "José",
    "sobrenome": "Gabriel",
    "notas": [10, 7]
}


def container_mock():
    return Mock()


def test_criar_aluno_campos_preenchido_sucesso():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 mock._validador.return_value(""), mock._convertedor.return_value(""))

    resultado = aluno_service.criar_aluno("José", "Julio")

    assert resultado == None


def test_criar_aluno_nome_vazio_excecao():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 ValidadorEntrada(mock.logger.return_value("")), mock._convertedor.return_value(""))

    with pytest.raises(Exception) as error:
        aluno_service.criar_aluno("", "Julio")

    assert str(error.value) == "\nO campo nome está vazio!"


def test_criar_aluno_sobrenome_none_sucesso():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 mock._validador.return_value(""), mock._convertedor.return_value(""))

    with pytest.raises(Exception) as error:
        aluno_service.criar_aluno("José", None)

    assert str(error.value) == "'NoneType' object has no attribute 'strip'"


def test_atualizar_aluno_campos_preenchido_sucesso():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 mock._validador.return_value(""), mock._convertedor.return_value(""))

    resultado = aluno_service.atualizar_aluno("1234", "Julio")

    assert resultado == None


def test_atualizar_aluno_matricula_vazio_excecao():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 ValidadorEntrada(mock.logger.return_value("")), mock._convertedor.return_value(""))

    with pytest.raises(Exception) as error:
        aluno_service.atualizar_aluno("", payload_valores_dict)

    assert str(error.value) == "\nO campo matricula está vazio!"


def test_atualizar_aluno_matricula_none_excecao():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 ValidadorEntrada(mock.logger.return_value("")), mock._convertedor.return_value(""))

    with pytest.raises(Exception) as error:
        aluno_service.atualizar_aluno(None, payload_valores_dict)

    assert str(error.value) == "\nO campo matricula está vazio!"

def test_deletar_aluno_campos_preenchido_sucesso():
    mock = container_mock()
    aluno_service = AlunoService(mock.logger.return_value(""), mock._persistencia.return_value(""),
                                 mock._validador.return_value(""), mock._convertedor.return_value(""))

    resultado = aluno_service.deletar_aluno("1234")

    assert resultado == None
