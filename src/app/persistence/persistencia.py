import os
import json
import os.path


class Persistencia:
    NOME_ARQUIVO = "Aluno.json"

    def __init__(self, log):
        self.log = log
        self.log.info(f"Persistencia iniciada!")
        self.alunos = []
        self._iniciar()

    def _iniciar(self):
        if not (os.path.exists(Persistencia.NOME_ARQUIVO)):
            self.log.info(
                f"O arquivo de salvamento dos dados ainda não existe!O arquivo estar sendo criado..."
            )
            with open(Persistencia.NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
                self.log.info(
                    f"O arquivo com nome Alunos.json foi criado e estar aberto para alterações!"
                )
        else:
            self.log.info(
                f"O arquivo de salvamento dos dados já existe com o nome Alunos.json!"
                f"O arquivo será aberto para alterações..."
            )
            self._carregar()
            self.log.info(
                f"O arquivo com nome Alunos.json estar aberto para alterações!"
            )

    def _salvar(self, aluno_dict={}):
        with open(Persistencia.NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            if aluno_dict:
                self.alunos.append(aluno_dict)
            json.dump(self.alunos, arquivo)

    def _carregar(self):
        try:
            with open(Persistencia.NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    alunos = json.loads(conteudo)
                    for aluno_da_vez in alunos:
                        self.alunos.append(aluno_da_vez)
                else:
                    self.log.info("O arquivo de dados está vazio.")
        except FileNotFoundError as erro:
            raise self.log.critical(erro)

    def atualizar(self, matricula, aluno):
        aluno_antigo = self.listar_um(matricula)
        for chave in aluno:
            if aluno[chave] is not None:
                aluno_antigo[chave] = aluno[chave]
        self._salvar()
        self.log.info(f"O aluno com a matrícula {matricula} foi atualizado!")

    def criar(self, aluno):
        matricula = aluno["matricula"]
        nome = aluno["nome"]
        sobrenome = aluno["sobrenome"]
        self._salvar(aluno)

        self.log.info(
            f"O aluno com nome {nome} {sobrenome} e matricula {matricula} foi cadastrado!"
        )

    def listar_todos(self):
        if not (self.alunos):
            raise Exception(f"Não existe nenhum aluno cadastrado ainda.")
        return self.alunos

    def deletar(self, matricula):
        with open(Persistencia.NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            for aluno in self.alunos:
                if matricula == aluno["matricula"]:
                    self.alunos.remove(aluno)
                    self._salvar({})
                    self.log.info(f"O registro com matrícula:{matricula} foi removido!")
                    return
        raise Exception(f"Não existe nenhum registro com matrícula: {matricula}")

    def listar_um(self, matricula):
        for aluno in self.alunos:
            if aluno["matricula"] == matricula:
                return aluno
        raise Exception(f"Não existe nenhum registro com matrícula: {matricula}")
