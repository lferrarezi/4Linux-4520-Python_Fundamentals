operacao = True
saldo = 100

def depositar(valor):
    global saldo
    if int(valor) > 0:
        saldo += int(valor)
        print("Depósito realizado.\nSeu saldo total passou a ser de R$", saldo)
    else:
        print("Valor para depósito inválido!")

def sacar(valor):
    global saldo
    if int(saque) > 0:
        if int(saque) > int(saldo):
            print("Saldo insuficiente.\nSaque não realizado")
        elif int(saque) == int(saldo):
            confirma = input("Confirma o saque total? S/N ")
            if confirma.lower() == "s":
                saldo -= int(valor)
                print("Saque realizado.\nO seu saldo atual está zerado.")
            else:
                print("Saque cancelado")
        else:
            confirma = input("Confirma o saque de R$ " + saque + ",00? S/N ")
            if confirma.lower() == "s":
                saldo -= int(valor)
                print("Saque realizado.\nO seu saldo atual é de: R$", int(saldo))
            else:
                print("Saque cancelado")
    else:
        print("Valor de saque inválido!")

def consultar():
    global saldo
    print("R$ %s" % (saldo))

while operacao:
    acao = input("Qual operação deseja realizar?\n(S)aque\n(D)epósito\n(C)onsulta de saldo\n")
    if acao.lower() == "s":
        sacar(input("Quanto você quer sacar? "))

    elif acao.lower() == "d":
        depositar(input("Quanto você quer depositar? "))

    elif acao.lower() == "c":
        consultar()

    if input("Deseja realizar uma nova operação? S/N ").lower() == "n":
        print("Obrigado, volte sempre!")
        operacao = False