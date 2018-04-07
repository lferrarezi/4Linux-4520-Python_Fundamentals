operacao = True
saldo = 100

while operacao:
    acao = input("Qual operação deseja realizar?\n(S)aque ou (D)epósito? ")
    if acao.lower() == "s":
        saque = input("Quanto você quer sacar? ")
        if int(saque) > 0:
            if int(saque) > int(saldo):
                print("Saldo insuficiente.\nSaque não realizado")
            elif int(saque) == int(saldo):
                confirma = input("Confirma o saque total? S/N ")
                if confirma.lower() == "s":
                    print("Saque realizado.\nO seu saldo atual está zerado.")
                else:
                    print("Saque cancelado")
            else:
                confirma = input("Confirma o saque de R$ " + saque + ",00? S/N ")
                if confirma.lower() == "s":
                    print("Saque realizado.\nO seu saldo atual é de: R$", int(saldo) - int(saque))
                else:
                    print("Saque cancelado")
        else:
            print("Valor de saque inválido!")

    elif acao.lower() == "d":
        deposito = input("Quanto você quer depositar? ")
        if int(deposito) > 0:
            saldo = int(saldo) + int(deposito)
            print("Depósito realizado.\nSeu saldo total passou a ser de R$",saldo)
        else:
            print("Valor para depósito inválido!")

    if input("Deseja realizar uma nova operação? S/N ").lower() == "n":
        print("Obrigado, volte sempre!")
        operacao = False