from pymongo import MongoClient

client = MongoClient('127.0.0.1')  # servidor
db = client['aula_python']  # escolha do banco
alunos = db.aluno.find()  # Escolha da Collection (tabela) - db.collection.find()


def listar_alunos():
    alunos = db.aluno.find()
    for aluno in alunos:
        print(aluno)

def buscar_aluno(vnome):
    alunos = db.aluno.find({"nome":vnome})
    for aluno in alunos:
        print(aluno)


def adicionar_aluno(vnome, vemail):
    db.aluno.insert_one({
        "nome": vnome,
        "email": vemail
    })
#    listar_alunos()


def adicionar_alunos(**valuno):
    db.aluno.insert_many({
        valuno
    })
#    listar_alunos()


def remover_aluno(vnome):
    db.aluno.delete_one({
        "nome": vnome
    })


def atualizar_aluno(vnome, vemail):
    db.aluno.update_one({
        "nome": vnome
    }, {
        "$set": {"email": vemail}
    })

# def update_aluno(find{}, update={})

operacao = True

while operacao:
    acao = input(
        "Qual operação deseja realizar?\n(I)nserir Aluno\n(R)emover Aluno\n(A)tualizar Aluno\n(B)uscar Aluno\n(L)istar Alunos\n")

    if acao.lower() == "i":
        adicionar = input("Deseja adicionar apenas 1 aluno? (S/N)\n")

        if  adicionar.lower() == "s":
            adicionar_aluno(input("Qual o nome do novo aluno?\n"), input("Qual o e-mail do novo aluno?\n"))

        else:
            vontade = True
            # dic_aluno = {}
            while vontade:
                # dic_aluno["nome"] = input("Digite o nome do aluno")
                # dic_aluno["email"] = input("Digite o e-mail do aluno")
                # adicionar_alunos(dic_aluno)
                adicionar_aluno(input("Qual o nome do novo aluno?\n"), input("Qual o e-mail do novo aluno?\n"))
                listar_alunos()
                if input("Deseja adicionar outro aluno? (S/N) \n").lower() == "n":
                    vontade = False

        listar_alunos()

    elif acao.lower() == "r":
        remover_aluno(input("Qual o nome do aluno que deseja remover?\n"))
        listar_alunos()

    elif acao.lower() == "a":
        atualizar_aluno(input("Qual o nome do aluno para ser atualizado?\n"), input("Qual o novo e-mail?\n"))
        listar_alunos()

    elif acao.lower() == "l":
        listar_alunos()

    elif acao.lower() == "b":
        buscar_aluno(input("Qual o nome do aluno que deseja buscar?\n"))

    if input("Deseja realizar uma nova operação? S/N\n").lower() == "n":
        listar_alunos()
        print("Obrigado, volte sempre!")
        operacao = False