if __name__ == "__main__":
    print(
        "Menu: \n" +
        "0: Lista de Cursos por Unidade\n" +
        "1: Disciplinas que são usadas em mais de um curso \n" +
        "10: Finalizar \n"
    )

    option = input()

    while option != "10":
        match option:
            case "0":
                unidade = input("Digite uma unidade: ")
                print("cursos")
            case "1":
                print("disciplinas")
        
        option = input()
        
