from app.utils.gerador_id import gerar_id


class Aluno:
    def __init__(self, nome, sobrenome, notas=[]):
        self.nome = nome.strip()
        self.sobrenome = sobrenome.strip()
        self.matricula = gerar_id()
        self.notas = notas

    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_matricula(self):
        return self.matricula

    def get_notas(self):
        return self.notas

    def set_nome(self, nome):
        self.nome = nome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_notas(self, notas):
        self.notas = notas

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "notas": self.notas,
        }
