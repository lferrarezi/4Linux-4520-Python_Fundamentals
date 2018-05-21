vontade = True
dic_aluno = {}
while vontade:
    dic_aluno["nome"] = input("Digite o nome do aluno")
    dic_aluno["email"] = input("Digite o e-mail do aluno")
    if input("Deseja adicionar outro aluno? (S/N) \n").lower() == "n":
        print(dic_aluno)
        vontade = False
