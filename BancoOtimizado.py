'''
menu
depositar
sacar
extrato
criar usuario
filtrar usuario
criar conta
listar conta

utilizar funções
'''


def menu():
    print(
        "======MENU======\n[1] Deposito\n[2] Saque\n[3] Retirar Extrato\n[4] Nova Conta\n[5] Listar Contas\n[6] Novo Usuario\n[7] Sair\n")
    opcao = input()
    return opcao


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append({'deposito': valor})
        print("Operacao Realizada com Sucesso!\n")
    else:
        print("Operacao Não Realizada, Valor Invalido!\n")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo < valor:
        print("Valor maior do que o disponivel em conta!\n")

    elif limite < valor:
        print("Saque valor menor que o limite diario!\n")

    elif numero_saques >= limite_saques:
        print("Atingiu o limite de saques diarios!\n")

    elif 0 < valor:
        saldo -= valor
        extrato.append({'saque': valor})
        numero_saques += 1
        print('Saque Realizado com Sucesso!\n')

    else:
        print("Valor Invalido, tente novamente!\n")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('========EXTRATO========')
    print(f'Operação ---   Valor')
    for item in range(len(extrato)):
        for operacao, valor in extrato[item].items():
            print(f'{operacao} --- R$ {valor:0.02f}')
    print('----------------------')
    print(f'Saldo    --- R$ {saldo:0.02f}')


def criar_usuario(usuarios):
    cpf = input("informe cpf: ")
    nome = input("informe nome: ")

    cliente = filtrar_usuario(cpf, usuarios)

    if cliente:
        print("Usuario ja existente!\n")
        return

    usuarios.append({'nome': nome, 'cpf': cpf})
    print("Usuario Criado com Sucesso!\n")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta Criada com Sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, Criação de conta encerrada!\n")


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
    while True:
        LIMITE_SAQUES = 3
        AGENCIA = '001'

        saldo = 0
        limite = 500
        extrato = []
        numero_saques = 0
        usuarios = []
        contas = []

        opcao = menu()

        if opcao == '1':
            valor = float(input())
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input())
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                   limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            criar_usuario(usuarios=usuarios)

        elif opcao == '7':
            break

        else:
            print("Opcao invalida, selecione novamente!\n")


main()
