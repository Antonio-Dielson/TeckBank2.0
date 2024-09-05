import textwrap

def menu():
    menu = """\n
    Bem-Vindo ao TeckBank
    ============ MENU ============
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova Conta
    [NU]\tNovo Usuário
    [Q]\tSair
    =>: """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR${valor:.2f}\n'
        print(f'Deposito no valor de {valor} realizado com sucesso')
    else:
        print('Erro, valor invalido')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saque = numero_saques >= limite_saques
    if execedeu_saldo:
        print(f'Saldo insuficiente, seu saldo é de R${saldo}')
    elif execedeu_limite:
        print(f'O valor limite de saque é R${limite} por vez')
    elif execedeu_saque:
        print(f'Você atingiu o limite máximo de saques diários ({limite_saques})')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque\tR${valor:.2f}\n'
        print(f'Saque no valor de R${valor} efetuado com sucesso')
    else:
        print('Erro, a operação falhou')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f'''
============= EXTRATO ============
{extrato}
==================================
Saldo: R${saldo:.2f}
==================================
          ''')

def criar_usuario(usuarios):
    cpf = input('Digite seu cpf: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f'Usuário já cadastrado com esse cpf: {cpf}')
        return
    
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento(d%/m%/%y):')
    endereço = input('Digite seu endereço (logradoura, número, bairro, cidade/UF): ')
    usuarios.append({'nome': nome, 'data_de_nascimento':data_nascimento, 'cpf': cpf, 'endereço': endereço})
    print(f'Seu cadastro foi criando com sucesso, {nome}')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite seu cpf: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f'Conta criada com sucesso\nAgência: {agencia}, número da conta: {numero_conta}')
        return {'agencia': agencia, 'numero_da_conta': numero_conta, 'usuario': usuario}
    else:
        print('Usuário não cadastrado, faça seu cadastro no TeckBank')

def main():
    limite_Saque = 3
    agencia = '0001'
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opicao = menu()

        if opicao == 'D':
            valor = float(input('Digite o valor do deposito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opicao == 'S':
            valor = float(input('Digite o valor que deseja sacar: '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_Saque
            )

        elif opicao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opicao == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opicao == 'NU':
            criar_usuario(usuarios)

        elif opicao == 'Q':
            break
        else:
            print('Opção invalida, tente novamente')

main()

