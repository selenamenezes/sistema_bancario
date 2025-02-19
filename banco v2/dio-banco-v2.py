import textwrap

def end_formatado(rua, n, bairro, cidade, sigla):
    return f"{rua}, {n} - {bairro} - {cidade}/{sigla}\n"

def criar_usuario(usuarios, nome, data_nasc, cpf, rua, n, bairro, cidade, sigla):
    endereco = end_formatado(rua, n, bairro, cidade, sigla)
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado.")
            return
        
    usuario = {
        "nome": nome, 
        "data_nas": data_nasc, 
        "cpf": cpf, 
        "endereco": endereco
    }
    
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, registro, cpf):
    for usuario in registro:
        if usuario["cpf"] == cpf:
            print("Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("A criação da conta falhou, usuário não encontrado.")

def sacar(*, saldo, valor, limite, extrato, numero_saques, limite_saque):
    if numero_saques < limite_saque:
        if valor > saldo:
            print("Saque não realizado, saldo insuficiente na conta.")
        elif valor < 1:
            print("Saque não realizado, valor inválido.")
        elif valor > limite:
            print("O valor do saque excede o limite.")
        else:
            print("Saque realizado com sucesso!")
            saldo -= valor
            extrato += f"Saque: R${valor}\n"
            numero_saques += 1
    else:
        print("Limite de saque diário excedido.")
        
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor < 1:
        print("Deposito não realizado, valor inválido.")
    else:
        print("Deposito realizado com sucesso!")
        saldo += valor
        extrato += f"Depósito: R${valor}\n"
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(extrato)
    print(f"Saldo: R${saldo}")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ''
    usuarios = []
    contas = []
    
    while True:    
        menu = '''\n
        -=- MENU -=-
        [1] Novo usuário
        [2] Nova conta
        [3] Depositar
        [4] Sacar
        [5] Extrato
        [6] Listar contas
        [0] Sair
        >>> '''
        op = int(input(menu))
    
        if op == 3:
            valor = float(input("Valor do depósito: "))
        
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif op == 4:
            valor = float(input("Valor do saque: "))
        
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUE
            )
        
        elif op == 5:
            print("=== EXTRATO ===")
            exibir_extrato(saldo, extrato=extrato)
    
        elif op == 1:
            print("-= CADASTRO =-")
            nome = input("Nome: ").strip().title()
            data_nasc = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            print("ENDERECO.")
            rua = input("Rua: ").strip()
            n = input("N: ").strip()
            bairro = input("Bairro: ").strip()
            cidade = input("Cidade: ").strip()
            sigla = input("UF: ").strip().upper()
            
            criar_usuario(usuarios, nome, data_nasc, cpf, rua, n, bairro, cidade, sigla)
        
        elif op == 2:
            cpf = input("Informe o CPF do usuário: ")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios, cpf)
        
            if conta:
                contas.append(conta)

        elif op == 6:
            if contas:
                listar_contas(contas)
            else:
                print("Ainda não há contas criadas.")
        
        elif op == 0:
            print("Saindo..")
            break
    
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()
