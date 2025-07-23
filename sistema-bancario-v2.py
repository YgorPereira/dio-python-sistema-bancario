menu = """
Qual operação deseja realizar?

1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Consultar extrato
5 - Sair
6 - Criar usuário
7 - Criar conta corrente
"""

saldo = 0
extrato = []
saques_diarios = 0
usuarios = []

contas_correntes = []

def criar_usuario(**kwargs):
    nome = kwargs.get('nome')
    data_nascimento = kwargs.get('data_nascimento')
    cpf = kwargs.get('cpf')
    endereco = kwargs.get('endereco')

    if cpf not in [usuario['cpf']  for usuario in usuarios]:
        usuarios.append({
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco,
            'contas_correntes': []
        })
        print(f'Usuário {nome} criado com sucesso!')
    else:
        print('CPF já cadastrado. Tente novamente com outro CPF.')

def criar_conta_corrente(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            numero_conta = len(contas_correntes) + 1
            conta = {
                'agencia': '0001',
                'numero_conta': numero_conta,
                'saldo': 0,
                'extrato': [],
                'saques_diarios': 0,
                'usuario': usuario
            }
            contas_correntes.append(conta)
            usuario['contas_correntes'].append(conta)
            print(f'Conta corrente criada com sucesso para {usuario['nome']}!')
            return
    print("CPF não encontrado. Usuário não existe.")
            
def consultar_saldo():
    global saldo
    print(f'Seu saldo atual é: R$ {saldo:.2f}')

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
    else:
        print('O valor para depósito deve ser maior que zero.')
    return saldo, extrato

def sacar(**kwargs):
    valor = kwargs.get('valor')
    saldo = kwargs.get('saldo')
    extrato = kwargs.get('extrato')
    saques_diarios = kwargs.get('saques_diarios')
    if valor > 500:
        print('O valor máximo para saque é R$ 500,00.')
    elif valor > saldo:
        print('Saldo insuficiente para saque.')
    elif saques_diarios >= 3:
        print('Limite diário de saques atingido. Tente novamente amanhã.')
    else:
        saldo -= valor
        saques_diarios += 1
        extrato.append(f'Saque: R$ {valor:.2f}')
        print(f'O limite diário de saques é 3. Saques realizados hoje: {saques_diarios}')
        print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
    return saldo, extrato

def consultar_extrato(saldo, /, *, extrato):
    print("-----Extrato:------")
    if not extrato:
        print('Nenhuma trasação realizada.')
    else:
        for transacao in extrato:
            print(transacao)
    print("-------------------")
    print(f'Saldo atual: R$ {saldo:.2f}')

def main():
    nome_usuario = input("Olá usuário! Digite o seu nome: ")

    print(f"""
    ---------- Seja bem-vindo {nome_usuario}! ----------
    """)

    saldo = 0
    extrato = []
    saques_diarios = 0

    while True:
        print(menu)
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            print(f'Seu saldo atual é: R$ {saldo:.2f}')

        elif opcao == 2:
            try:
                valor = float(input("Digite o valor que deseja depositar: "))
                saldo, extrato = depositar(valor, saldo, extrato)
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

        elif opcao == 3:
            try:
                valor = float(input("Digite o valor que deseja sacar: "))
                saldo, extrato, saques_diarios = sacar(
                    valor=valor, saldo=saldo, extrato=extrato, saques_diarios=saques_diarios
                )
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

        elif opcao == 4:
            consultar_extrato(saldo, extrato=extrato)

        elif opcao == 5:
            print("Você escolheu sair do sistema. Até logo!")
            break

        elif opcao == 6:
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ")
            criar_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

        elif opcao == 7:
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(cpf)

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
