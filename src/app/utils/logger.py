import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger('Log Aluno')
        self.logger.setLevel(logging.DEBUG)

        arquivo_log = 'Alunos.log'
        file_handler = logging.FileHandler(arquivo_log)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def debug(self, mensagem):
        self.logger.debug(mensagem)

    def info(self, mensagem):
        self.logger.info(mensagem)

    def warning(self, mensagem):
        self.logger.warning(mensagem)

    def error(self, mensagem):
        self.logger.error(mensagem)

    def critical(self, mensagem):
        self.logger.critical(mensagem)
