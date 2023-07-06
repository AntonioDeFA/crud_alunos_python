from app.container.container import Container

container = Container()
opcao = None

container.logger().info("Programa iniciado!")

while True:
    try:
        opcao = input(
            "Escola uma opção:"
            "\n[0] Para sair."
            "\n[1] Criar aluno."
            "\n[2] Adicionar nota ao aluno."
            "\n[3] Remover ou editar nota de aluno."
            "\n[4] Alterar dados do aluno."
            "\n[5] Excluir aluno."
            "\n[6] Listar aluno por id."
            "\n[7] Listar todos os alunos."
        )
        if opcao == "0":
            print("Saindo do programa!")
            break
        elif opcao == "1":
            nome = input("Digite o nome do aluno:")
            sobrenome = input("Digite o sobrenome do aluno:")

            container.controller_aluno().criar_aluno(nome, sobrenome)

            print("Aluno cadastrado!")
        elif opcao == "2":
            matricula = input("Digite a matrícula que você deseja adicionar notas:")
            notas = container.controller_aluno().listar_aluno_objeto(matricula)["notas"]
            nota = 0
            while True:
                nota = float(
                    input(
                        "Digite uma nota entre 0 e 10.\nCaso queira sair digite um valor menor que zero:"
                    )
                )
                if nota > 10:
                    print("Valor errado, tente novamente!")
                    continue
                elif nota < 0:
                    break
                print("Nota enviada!")
                notas.append(nota)
            container.controller_aluno().atualizar_aluno(matricula, {"notas": notas})

            print("Notas atualizadas")
        elif opcao == "3":
            matricula = input("Digite a matrícula que você deseja adicionar notas:")
            notas = container.controller_aluno().listar_aluno_objeto(matricula)["notas"]

            atualizou = False
            while notas:
                print(notas)
                posicao = input(
                    "Digite a posição da nota que deseja alterar:\nDigite 'Sair' para sair:"
                ).lower()
                if posicao == "sair":
                    break
                posicao = int(posicao)
                if posicao >= 0 and posicao <= len(notas):
                    print("Você escolheu a nota " + str(notas[posicao - 1]))
                    acao = input(
                        "Você deseja deletar ou atualizar?\nDigite 'Deletar' para deletar, 'Alterar' para alterar e 'Sair' para sair:"
                    ).lower()
                    if acao == "sair":
                        break
                    elif acao == "deletar":
                        notas.pop(posicao - 1)
                        atualizou = True
                    elif acao == "alterar":
                        nota = float(input("Digite a nova nota:"))
                        if nota > 10 or nota < 0:
                            print("Nota invalida! Tente novamente!")
                            break
                        notas[posicao - 1] = nota
                        atualizou = True
                else:
                    print("Posição errada, tente novamente!")
            else:
                print("Nenhuma nota foi cadastrada ainda!")

            if atualizou:
                container.controller_aluno().atualizar_aluno(
                    matricula, {"notas": notas}
                )
                print("Nota atualizada")

        elif opcao == "4":
            opcoes = ["nome", "sobrenome", "matricula"]
            matricula = input("Digite a matrícula que você deseja alterar os dados:")
            aluno_dict = {}
            while True:
                opcao = input(
                    (
                            "Digite a opção que você quer alterar:\nOpções são "
                            + ", ".join(opcoes)
                            + "\nCaso queira sair é só digitar 'Sair':"
                    )
                ).lower()
                if opcao == "sair":
                    break
                elif opcao in opcoes:
                    novo_valor = input("Digite o novo " + opcao + ":")
                    aluno_dict[opcao] = novo_valor
                else:
                    print("Esta opção não existe!\nTente novamente!")
            if aluno_dict:
                container.controller_aluno().atualizar_aluno(matricula, aluno_dict)
                print("Informações atualizadas!")
            else:
                print("Você não escolheu nada, o aluno não foi atualizado!")

        elif opcao == "5":
            print(container.controller_aluno().listar_aluno_texto(""))
            matricula = input("Digite a matrícula que você deseja excluir:")
            container.controller_aluno().deletar_aluno(matricula)
            print("Aluno excluido")
        elif opcao == "6":
            matricula = input("Digite a matrícula que você deseja ver os dados:")
            print(container.controller_aluno().listar_aluno_texto(matricula))
        elif opcao == "7":
            print(container.controller_aluno().listar_aluno_texto(None))
        else:
            print("Valor errado, tente novamente!")
    except Exception as erro:
        container.logger().error(erro)
        print(erro)
        continue

container.logger().info("Programa finalizado!")
