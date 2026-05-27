import sys
nomes = []
senhas = []
while True:
    login = input("\nDigite o nome de usuário: ")
    pin = input("Digite a senha: ")
    if login in nomes and pin == senhas[nomes.index(login)]:
        print(f"\nLogin realizado com sucesso! Olá, {login}.")
        break
    else:
        print("Usuário não encontrado ou senha incorreta.")
        decisao = input("Deseja criar uma conta? (s/n): ").lower()
        if decisao == "s":
            novo_nome = input("Escolha um nome de usuário: ")
            novo_pin = input("Escolha uma senha: ")
            nomes.append(novo_nome)
            senhas.append(novo_pin)
            print("Conta criada! Agora faça o login.")
        else:
            print("Encerrando sistema...")
            exit()
saldo = 1000.00
limite_saque = 500.00
historico = []
while True:
    print("1 - Ver saldo")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Ver Histórico")
    print("5 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    elif opcao == "2":
        valor = float(input(f"Digite o valor do saque (Limite R$ {limite_saque}): R$ "))

        if valor > saldo:
            print("Erro: Saldo insuficiente.")
        elif valor > limite_saque:
            print(f"Erro: O limite por saque é de R$ {limite_saque}.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            saldo -= valor
            historico.append(f"Saque: - R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado!")
    elif opcao == "3":
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            historico.append(f"Depósito: + R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            print("Valor inválido.")
    elif opcao == "4":
        print("HISTÓRICO")
        for operacao in historico:
            print(operacao)
        if not historico:
            print("Nenhuma transação realizada.")
    elif opcao == "5":
        print("Operação encerrada. Volte sempre!")
       sys.exit()
   else:
        print("Opção inválida.")
    