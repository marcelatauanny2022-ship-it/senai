opcao = input("Escolha uma opção: 1-Login, 2-Cadastrar, 3-Sair: ")

match opcao:
    case "1":
        print("Iniciando Login...")
    case "2":
        print("Criando nova conta...")
    case "3":
        print("Saindo do sistema...")
    case _:
        print("Opção inválida!")
