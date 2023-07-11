class ValidadorEntrada:
    def __init__(self, logger):
        self.log = logger

    def validar_entradas(self, entrada_ignorar, valores_dict):
        self.log.info(f"Validação dos campos e valores "
                      f"{valores_dict} iniciada!")
        excecao_texto = ""
        for campo, valor in valores_dict.items():
            if campo in entrada_ignorar:
                continue
            if (
                    valor is None
                    or valor == ""
                    or (isinstance(valor, list) and len(valor) == 0)
            ):
                excecao_texto += "\nO campo " + campo + " está vazio!"
            else:
                self.log.info(f"O campo {campo} com valor "
                              f"{valor} foi validado!")

        if excecao_texto:
            raise Exception(excecao_texto)
