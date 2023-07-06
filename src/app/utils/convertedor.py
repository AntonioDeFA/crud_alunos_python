import numpy as np


class Convertedor:

    def dict_aluno_to_string_complex_describe(self, aluno):
        media = np.mean(aluno["notas"]) if aluno["notas"] else 0
        estado_aprovacao = "Aprovado" if media >= 7 else "Reprovado"

        return "\n".join(
            [
                "Nome do aluno: " + aluno["nome"] + " " + aluno["sobrenome"],
                "Sua matrícula é: " + aluno["matricula"],
                "Suas notas são: " + str(aluno["notas"]),
                "Sua média é: " + str(media),
                estado_aprovacao,
            ]
        )

    def dict_aluno_to_string(self, aluno):
        return "\n".join(
            [
                "Nome do aluno: "
                + aluno["nome"]
                + " "
                + aluno["sobrenome"]
                + ". Sua matrícula é: "
                + aluno["matricula"]
                + ". Suas notas são: "
                + str(aluno["notas"])
            ]
        )
