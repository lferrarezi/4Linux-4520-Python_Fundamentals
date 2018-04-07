saldo = 100
saque = input("Quanto quer sacar? ")

if int(saque) > 0:
    if int(saque) > int(saldo):
        print("Saldo insuficiente. Saque não realizado")
    elif int(saque) == int(saldo):
        confirma = input("Confirma o saque total? S/N ")
        if confirma.lower() == "s":
            print("Saque realizado. O seu saldo atual está zerado.")
        else:
            print("Saque cancelado")
    else:
        confirma = input("Confirma o saque de R$ " + saque + ",00? S/N ")
        if confirma.lower() == "s":
            print("Saque realizado. O seu saldo atual é de: R$", int(saldo) - int(saque))
        else:
            print("Saque cancelado")
else:
    print("Valor de saque inválido!")
