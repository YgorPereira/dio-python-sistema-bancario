menu = """
Qual operação deseja realizar?

1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Consultar extrato
5 - Sair
"""

saldo = 0
extrato = []
saques_diarios = 0

def consultar_saldo():
    global saldo
    print(f'Seu saldo atual é: R$ {saldo:.2f}')

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
    else:
        print('O valor para depósito deve ser maior que zero.')

def sacar(valor):
    global saldo, extrato, saques_diarios
    if valor > 500:
        print('O valor máximo para saque é R$ 500,00.')
    elif valor > saldo:
        print('Saldo insuficiente para saque.')
    elif saques_diarios >= 3:
        print('Limite diário de saques atingido. Tente novamente amanhã.')
    else:
        saldo -+ valor
        saques_diarios += 1
        extrato.append(f'Saque: R$ {valor:.2f}')
        print(f'O limite diário de saques é 3. Saques realizados hoje: {saques_diarios}')
        print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}')

def consultar_extrato():
    global extrato
    print("-----Extrato:------")
    if not extrato:
        print('Nenhuma trasação realizada.')
    else:
        for transacao in extrato:
            print(transacao)
    print("-------------------")

def main():
    nome_usuario = input("Olá usuário! Digite o seu nome: ")

    print(f"""
    ----------Seja bem vindo {nome_usuario}!----------
    """)
    
    while True:
        try: 
            print(menu)
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            consultar_saldo()
        elif opcao == 2:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            depositar(valor_deposito)
        elif opcao == 3: 
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            sacar(valor_saque)
        elif opcao == 4:
            consultar_extrato()
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")
        
    print("Você escolheu sair do sistema. Até logo!")

if __name__ == "__main__":
    main()
