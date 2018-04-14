def args(a, *lista):
    print(a)
    print(lista)

args(5, 10, 15, 20)

def args(x=10, **dicionario):
    print(x)
    print(dicionario)
args(x=15, y=20, teste=25)
