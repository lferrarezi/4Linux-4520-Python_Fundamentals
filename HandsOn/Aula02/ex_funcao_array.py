def buildDict(chave1, valor1, chave2, valor2):
    dicionario = {
        chave1: valor1,
        chave2: valor2
    }
    return dicionario

print(buildDict(input("Chave 1: "), input("Valor 1: "), input("Chave 2: "), input("Valor 2: ")))
