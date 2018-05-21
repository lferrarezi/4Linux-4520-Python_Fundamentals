nome = "mariana"
user = {}

try:
    if "mariana" == nome:
        print(user["nome"])
except NameError:
    print("Erro ao acessar a uma variável")
except KeyError:
    print("Erro ao acessar a chave da variável")

print("Vem depois")

try:
    calculo = 10/0
except ZeroDivisionError:
    print("Divisão por zero")

print("Continua")