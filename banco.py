
# deposito, saque, extrato
# com menu
'''
[d] = deposito
[s] = saque
[e] = extrato
[x] = sair
'''


class Cliente:
    nome = ""
    saldo = 0
    quant_saque = 3
    extrato = []


class Banco:

    def deposito(self, Cliente, acrescimo):
        if acrescimo > 0:
            Cliente.saldo += acrescimo
            Cliente.extrato.append({'deposito': acrescimo})
            print('deposito efetuado com sucesso')

    def saque(self, Cliente, decrescimo):
        if Cliente.saldo <= 0:
            print('saldo insuficiente')

        elif Cliente.quant_saque <= 0:
            print('atingiu limite de saques diarios')

        elif Cliente.saldo < decrescimo:
            print('valor do saque menor que o saldo')

        else:
            Cliente.saldo -= decrescimo
            Cliente.extrato.append({'saque': decrescimo})
            print('saque efetuado com sucesso')

    def extrato(self, Cliente):
        print('========EXTRATO========')
        print(f'Operação ---   Valor')
        for item in range(len(Cliente.extrato)):
            for operacao, valor in Cliente.extrato[item].items():
                print(f'{operacao} --- R$ {valor:0.02f}')
        print('----------------------')
        print(f'Saldo    --- R$ {Cliente.saldo:0.02f}')


# Login
cliente = Cliente()
banco = Banco()

# Menu
while True:

    print('[d] = deposito \n[s] = saque \n[e] = extrato \n[x] = sair \n')

    entrada = input()

    if entrada == 'd':
        valor = int(input())
        banco.deposito(Cliente=cliente, acrescimo=valor)

    elif entrada == 's':
        valor = int(input())
        banco.saque(Cliente=cliente, decrescimo=valor)

    elif entrada == 'e':
        banco.extrato(Cliente=cliente)

    elif entrada == 'x':
        break

    else:
        print('Opção inexistente, tente novamente')

    print()
