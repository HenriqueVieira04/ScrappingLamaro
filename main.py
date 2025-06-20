def menu():
    # Impressão do menu
    print(
        "----------------------- Menu -----------------------\n" +
        "0: Lista de Cursos por Unidade\n" +
        "1: Dados de um determinado curso\n" +
        "2: Dados de todos os cursos\n" +
        "3: Dados de uma disciplina\n" +
        "4: Disciplinas que são usadas em mais de um curso\n"
        "10: Finalizar \n" +
        "----------------------------------------------------\n"
    )

if __name__ == "__main__":

    # Inicialização dos dicinários
    unidades = {}
    cursos = {}
    disciplinas = {}

    # Impressão do menu
    menu()

    # Leitura da opção
    option = input("Digite uma opção: ")
    print("\n")

    while option != "10":
        match option:
            # Lista de Cursos por Unidade
            case "0":
                unidade = input("Digite uma unidade: ")
                print("\n")
                if unidade in unidades:
                    print(unidades[unidade])
                    print("\n")
                else:
                    print(f"Unidade {unidade} não existente.\n")
            # Dados de um determinado curso
            case "1":
                print("Lista de cursos: ")
                for curso in cursos:
                    print(curso)
                    print("\n")
                curso = input("Digite o nome de um curso: ")
                print("\n")
                if curso in cursos:
                    print(cursos[curso])
                    print("\n")
                else:
                    print(f"Curso {curso} não existente.\n")
            # Dados de todos os cursos
            case "2":
                if len(cursos) != 0:
                    for curso in cursos:
                        print(curso)
                        print("\n")
                else:
                    print("Nenhum curso encontrado.\n")
            # Dados de uma disciplina
            case "3":
                disciplina = input("Digite o código de uma disciplina: ")
                print("\n")
                if disciplina in disciplinas:
                    print(disciplinas[disciplina])
                    print("\n")
                else:
                    print(f"Disciplina {disciplina} não existente.\n")
            # Disciplinas que são usadas em mais de um curso
            case "4":
                print("nada")
        
        menu()
        option = input("Digite uma opção: ")
        print("\n")
    
    print("Programa finalizado.")
        
