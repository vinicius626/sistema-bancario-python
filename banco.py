contas = {}

def criar_conta():
    usuario = input("Digite o nome do usuário: ")

    if usuario in contas:
        print("usuário já existe!")
        return
    
    senha = input("Digite a senha: ")

    contas[usuario] = {
        "senha": senha,
        "saldo":0,
        "historico": []
    }

    print("conta criada com sucesso!")

def login():
    usuario = input("usuário: ")
    senha = input("senha: ")

    if usuario in contas and contas[usuario]["senha"]== senha:
        print("Login realizado!")
        menu_conta(usuario)
    else:
        print("usuário ou senha incorretos")

def depositar(usuario):
    valor = float(input("valor para depositar: "))

    contas[usuario]["saldo"] += valor
    contas[usuario]["historico"].append(f"Depósito: {valor}")

    print("Depósito realizado!")

def sacar(usuario):
    valor = float(input("valor para sacar:"))

    if valor > contas[usuario]["saldo"]:
        print("saldo insuficiente!")
    else:
        contas[usuario]["saldo"] -= valor
        contas[usuario]["historico"].append(f"saque: {valor}")
        print("saque realizado!")

def ver_saldo(usuario):
    print(f"saldo atual: {contas[usuario]['saldo']}")

def ver_historico(usuario):
    print("Historico:")
    for h in contas[usuario]["historico"]:
            print(h)

def menu_conta(usuario):
    while True:
        print("\n1 - ver ssaldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Historico")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            ver_saldo(usuario)

        elif opcao == "2":
            depositar(usuario)

        elif opcao == "3":
            sacar(usuario)

        elif opcao == "4":
            ver_historico(usuario)

        elif opcao == "5":
            break

def menu_principal():
    while True:
        print("\n=== Banco do Vinicius ===")
        print("1 - Criar conta")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_conta()

        elif opcao == "2":
            login()

        elif opcao == "3":
            break

    menu_principal()
