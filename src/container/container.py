from utils.logger import Logger
from utils.convertedor import Convertedor
from utils.validador_entrada import Validador
from service.aluno_service import AlunoService
from persistencia.persistencia import Persistencia
from dependency_injector import containers, providers
from controller.controller_aluno import ControllerAluno

class Container(containers.DeclarativeContainer):

    logger = providers.Singleton(Logger)

    _convertedor = providers.Singleton(Convertedor)

    _validador = providers.Singleton(Validador, logger)

    _persistencia = providers.Singleton(Persistencia, logger)

    _aluno_service = providers.Singleton(AlunoService, logger, _persistencia, _validador, _convertedor)

    controller_aluno = providers.Singleton(ControllerAluno, _aluno_service)