# ---- Cadastro de Alunos com matrícula automática por curso ----

alunos = []

# Contadores por curso
GEC = 0
GEA = 0
GES = 0
GEB = 0
GET = 0

CURSOS_VALIDOS = {"GEC", "GEA", "GES", "GEB", "GET"}


def gerar_matricula(prefixo: str) -> str:
    """
    Gera a próxima matrícula para o curso (prefixo) informado.
    Usa contadores globais: GEC1, GEC2, ..., GES1, GES2, etc.
    """
    global GEC, GEA, GES, GEB, GET
    if prefixo == "GEC":
        GEC += 1
        return prefixo + str(GEC)
    elif prefixo == "GEA":
        GEA += 1
        return prefixo + str(GEA)
    elif prefixo == "GES":
        GES += 1
        return prefixo + str(GES)
    elif prefixo == "GEB":
        GEB += 1
        return prefixo + str(GEB)
    elif prefixo == "GET":
        GET += 1
        return prefixo + str(GET)
    else:
        return ""  # prefixo inválido


def cadastrar_alunos():
    nome = input("Digite o nome do aluno: ").strip()
    email = input("Digite o e-mail do aluno: ").strip()
    curso = input("Digite o curso do aluno (GEC, GEA, GES, GEB, GET): ").strip().upper()

    if curso not in CURSOS_VALIDOS:
        print("Curso inválido! Use apenas GEC, GEA, GES, GEB ou GET.")
        return

    matricula = gerar_matricula(curso)
    if not matricula:
        print("Falha ao gerar matrícula.")
        return

    alunos.append({"nome": nome, "email": email, "curso": curso, "matricula": matricula})
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(
                f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | "
                f"E-mail: {aluno['email']} | Curso: {aluno['curso']}"
            )


def atualizar_alunos():
    # Obs.: Atualizando por NOME (se houver nomes repetidos, atualiza o primeiro encontrado)
    nome = input("Digite o nome do aluno a ser atualizado: ").strip()

    for aluno in alunos:
        if aluno["nome"].strip().upper() == nome.strip().upper():
            novo_email = input(f"Digite o novo e-mail (atual: {aluno['email']}): ").strip()
            novo_curso = input(
                f"Digite o novo curso (GEC, GEA, GES, GEB, GET) (atual: {aluno['curso']}): "
            ).strip().upper()

            # Atualiza e-mail, se informado
            if novo_email:
                aluno["email"] = novo_email

            # Se curso não informado, mantém o atual
            if not novo_curso:
                print("Aluno atualizado (curso mantido, matrícula inalterada).")
                return

            # Se curso inválido
            if novo_curso not in CURSOS_VALIDOS:
                print("Curso inválido! Use apenas GEC, GEA, GES, GEB ou GET.")
                return

            # Se curso mudou, regenera a matrícula
            if novo_curso != aluno["curso"]:
                nova_matricula = gerar_matricula(novo_curso)
                if not nova_matricula:
                    print("Falha ao gerar nova matrícula.")
                    return
                aluno["curso"] = novo_curso
                aluno["matricula"] = nova_matricula
                print(f"Aluno atualizado com sucesso! Nova matrícula: {nova_matricula}")
            else:
                # Curso igual: não muda matrícula
                print("Aluno atualizado (curso mantido, matrícula inalterada).")
            return

    print("Aluno não encontrado.")


def remover_alunos():
    # Obs.: Removendo por NOME (se houver nomes repetidos, remove o primeiro encontrado)
    nome = input("Digite o nome do aluno a ser removido: ").strip()
    for aluno in alunos:
        if aluno["nome"].strip().upper() == nome.strip().upper():
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")


def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_alunos()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_alunos()
        elif opcao == '4':
            remover_alunos()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
