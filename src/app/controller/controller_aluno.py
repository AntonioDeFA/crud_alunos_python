class ControllerAluno:
    def __init__(self, aluno_service):
        self.service_aluno = aluno_service

    def criar_aluno(self, nome, sobrenome):
        self.service_aluno.criar_aluno(nome, sobrenome)

    def atualizar_aluno(self, matricula, aluno_dict):
        self.service_aluno.atualizar_aluno(matricula, aluno_dict)

    def deletar_aluno(self, matricula):
        self.service_aluno.deletar_aluno(matricula)

    def listar_aluno_texto(self, matricula):
        return self.service_aluno.listar_aluno_texto(matricula)

    def listar_aluno_objeto(self, matricula):
        return self.service_aluno.listar_aluno_objeto(matricula)
