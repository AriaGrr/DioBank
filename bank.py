# 3 saques diários, não podendo passar de 500 cada um.

balance = 0
daily_limit = 3
statement = []

def deposit():
    global balance
    value = float(input('Digite o valor do depósito: '))
    balance += value
    print('Depósito realizado com sucesso!')
    statement.append("Depósito:")
    statement.append(value)

def debit ():
    global balance
    global daily_limit
    value = float(input('Digite o valor do saque: '))
    if value > 500:
        print('O valor máximo de saque é de R$ 500,00.')
    elif daily_limit == 0:
        print('Você atingiu o limite de saques diários.')
    elif value > balance:
        print('Saldo insuficiente.')
    else:
        balance -= value
        daily_limit -= 1
        print('Saque realizado com sucesso!')
        statement.append("Saque:")
        statement.append(value)

def statements():
    if len(statement) == 0:
        print('Não foram realizadas movimentações.')
    else:
        for i in statement:
            if i == "Depósito:":
                print('Depósito realizado: R$ {:.2f}'.format(statement[statement.index(i)+1]))
            elif i == "Saque:":
                print('Saque realizado: R$ {:.2f}'.format(statement[statement.index(i)+1]))
    print('Saldo atual: R$ {:.2f}'.format(balance))

def clear_screen():
    # Função para limpar a tela do terminal
    print('\033[H\033[J')

# Menu principal
while True:
    clear_screen()
    print('=== Banco ===')
    print('1. Depósito')
    print('2. Saque')
    print('3. Extrato')
    print('0. Sair')

    option = input('Escolha uma opção: ')

    if option == '1':
        deposit()
    elif option == '2':
        debit()
    elif option == '3':
        statements()
    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Obrigado por utilizar o Sistema de Banco!')