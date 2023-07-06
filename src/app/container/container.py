from app.utils.logger import Logger
from app.utils.convertedor import Convertedor
from app.service.aluno_service import AlunoService
from app.persistence.persistencia import Persistencia
from app.utils.validador_entrada import ValidadorEntrada
from app.controller.controller_aluno import ControllerAluno

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    logger = providers.Singleton(Logger)

    _convertedor = providers.Singleton(Convertedor)

    _validador = providers.Singleton(ValidadorEntrada, logger)

    _persistencia = providers.Singleton(Persistencia, logger)

    _aluno_service = providers.Singleton(
        AlunoService, logger, _persistencia, _validador, _convertedor
    )

    controller_aluno = providers.Singleton(ControllerAluno, _aluno_service)
