import pytest
from unittest.mock import Mock
from app.utils.validador_entrada import ValidadorEntrada

payload_valores_dict = {
    "matricula": "1e9cd",
    "nome": "José",
    "sobrenome": "Gabriel",
    "notas": [10, 7]
}


def mock_logger():
    return Mock()


def test_entrada_preenchida_sem_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())

    resultado = validador.validar_entradas([], payload_valores_dict)

    assert resultado == None


def test_entrada_dict_vazio_sem_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict = {}

    resultado = validador.validar_entradas([], payload_valores_dict)

    assert resultado == None


def test_entrada_none_sem_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict = None

    with pytest.raises(AttributeError) as error:
        validador.validar_entradas([], payload_valores_dict)

    assert str(error.value) == "'NoneType' object has no attribute 'items'"


def test_entrada_preenchida_com_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())

    resultado = validador.validar_entradas(["nome", "teste"], payload_valores_dict)

    assert resultado == None


def test_entrada_dict_vazio_com_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict = {}

    resultado = validador.validar_entradas(["nome", "teste"], payload_valores_dict)

    assert resultado == None


def test_entrada_none_com_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict = None

    with pytest.raises(AttributeError) as error:
        validador.validar_entradas(["nome", "teste"], payload_valores_dict)

    assert str(error.value) == "'NoneType' object has no attribute 'items'"


def test_entrada_com_campo_nome_none_sem_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict["nome"] = None

    with pytest.raises(Exception) as error:
        validador.validar_entradas([], payload_valores_dict)

    assert str(error.value) == "\nO campo nome está vazio!"

    payload_valores_dict["nome"] = "José"


def test_entrada_com_campo_nome_vazio_sem_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict["nome"] = ""

    with pytest.raises(Exception) as error:
        validador.validar_entradas([], payload_valores_dict)

    assert str(error.value) == "\nO campo nome está vazio!"

    payload_valores_dict["nome"] = "José"


def test_entrada_com_campo_notas_vazio_sem_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict["notas"] = []

    with pytest.raises(Exception) as error:
        validador.validar_entradas([], payload_valores_dict)

    assert str(error.value) == "\nO campo notas está vazio!"

    payload_valores_dict["notas"] = [10, 7]


def test_entrada_com_campo_nome_none_com_campo_nome_campos_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict["nome"] = None

    resultado = validador.validar_entradas(["nome"], payload_valores_dict)

    assert resultado == None

    payload_valores_dict["nome"] = "José"


def test_entrada_com_campo_nome_vazio_com_campo_nome_nao_existente_para_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict["nome"] = ""

    with pytest.raises(Exception) as error:
        validador.validar_entradas([], payload_valores_dict)

    assert str(error.value) == "\nO campo nome está vazio!"

    payload_valores_dict["nome"] = "José"


def test_entrada_com_campo_notas_vazio_com_campo_nome_campos_para_para_ignorar_retorno_sucesso():
    validador = ValidadorEntrada(mock_logger())
    payload_valores_dict["notas"] = []

    with pytest.raises(Exception) as error:
        validador.validar_entradas([], payload_valores_dict)

    assert str(error.value) == "\nO campo notas está vazio!"

    payload_valores_dict["notas"] = [10, 7]
