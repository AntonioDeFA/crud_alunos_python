from app.model.aluno import Aluno


class AlunoService:
    def __init__(self, log, persistencia, validador, convertedor):
        self.log = log
        self.persistencia = persistencia
        self.validador = validador
        self.convertedor = convertedor

    def criar_aluno(self, nome, sobrenome):
        self.log.info(
            f"Processo de criação de aluno inciada com nome {nome}, sobrenome {sobrenome}"
        )

        self.validador.validar_entradas([], {"nome": nome, "sobrenome": sobrenome})

        aluno = Aluno(nome, sobrenome)
        aluno = aluno.to_dict()
        self.persistencia.criar(aluno)

    def atualizar_aluno(self, matricula, aluno_dict):
        self.log.info(
            f"Processo de atualização de aluno com matricula {matricula} inciada. Valores a atualizar {aluno_dict}"
        )

        self.validador.validar_entradas(
            [], {"matricula": matricula, "dados alunos": aluno_dict}
        )

        self.persistencia.atualizar(matricula, aluno_dict)

    def deletar_aluno(self, matricula):
        self.log.info(f"Processo de deletar aluno inciado com matricula {matricula}")

        self.validador.validar_entradas([], {"matricula": matricula})

        self.persistencia.deletar(matricula)

    def listar_aluno_texto(self, matricula):
        self.log.info(f"Processo de listagem aluno inciado com matricula {matricula}")

        if matricula:
            return self.convertedor.dict_aluno_to_string_complex_describe(
                self.persistencia.listar_um(matricula)
            )

        alunos_recuperados = self.persistencia.listar_todos()
        alunos = [
            self.convertedor.dict_aluno_to_string(aluno) for aluno in alunos_recuperados
        ]
        return "\n".join(alunos)

    def listar_aluno_objeto(self, matricula):
        self.log.info(f"Processo de listagem aluno inciado com matricula {matricula}")

        if matricula:
            return self.persistencia.listar_um(matricula)

        return self.persistencia.listar_todos()
