valor1 = input("Digite o primeiro valor numérico: ")
operacao = input("Qual operação você deseja realizar?\n1 p/ Soma\n2 p/ Subtração\n3 p/ Multiplicação\n4 p/ Divisão\n: ")
valor2 = input("Digite o segundo valor numérico: ")

if operacao == "1":
    print(int(valor1) + int(valor2))
elif operacao == "2":
    print(int(valor1) - int(valor2))
elif operacao == "3":
    print(int(valor1) * int(valor2))
elif operacao == "4":
    print(int(valor1) / int(valor2))
elif operacao == "5":
    print(int(valor1) ** int(valor2))
elif operacao == "6":
    print(int(valor1) // int(valor2))
else:
    print("Seleção inválida")