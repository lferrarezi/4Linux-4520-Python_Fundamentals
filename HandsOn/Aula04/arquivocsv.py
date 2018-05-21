import csv

with open("dados.csv") as csvfile:
    dados = csv.reader(csvfile)
    print(dados)
    for linha in dados:
        print(linha)

with open("arquivo.csv", "w", newline="") as csvfile:
    arquivo