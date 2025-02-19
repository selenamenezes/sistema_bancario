saldo = 0
deposito = 0
SAQUE_DIARIO = 3
LIMITE_SAQUE = 500
saque = 0
cont_saque = 0
extrato = ""

menu = """
-- BANCO DIO --
[1] Depositar
[2] Sacar
[3] Extratos
[0] Sair

>>> """
while True:
    opcao = input(menu)
    
    if opcao == "1":
        deposito = int(input("Depósito: "))
        if deposito < 1:
            print("Depósito não realizado, o valor deve ser válido.")
        else:
            print("Deposito realizado com sucesso!")
            saldo += deposito
            extrato += f"Depósito: R${deposito}\n"
            
    if opcao == "2":
        saque = float(input("Saque: "))
        if cont_saque < 3:
            if saque > LIMITE_SAQUE:
                print("Saque não realizado, o valor excedeu o limite.")
            elif saque > saldo:
                print("Saque não realizado, saldo insuficiente na conta.")
            elif saque < 1:
                 print("Saque não realizado, valor inválido.")
            else:
                print("Saque realizado com sucesso!")
                saldo -= saque
                cont_saque += 1
                extrato += f"Saque: R${saque}\n"
        else:
            print("Limite de saque diário excedido.")
            
    if opcao == "3":
        print("-- EXTRATO --")
        print(extrato)
        print(f"Saldo: R${saldo}")
    
    if opcao == "0":
        print("Saindo do sistema...")
        break
    
    if opcao not in ["1", "2", "3", "0"]:
        print("Opção inválida, tente novamente.")
