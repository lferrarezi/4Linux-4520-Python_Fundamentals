import psycopg2, psycopg2.extras

con = psycopg2.connect("host='localhost' dbname='aula_python' user='luiz' password='4linux'")
cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def listar_alunos():
    cur.execute("SELECT * FROM aluno;")
    # cur.fetchone() #traz apenas um aluno
    alunos = cur.fetchall()  # traz todos os alunos
    for aluno in alunos:
        print(aluno["id"], aluno["nome"], aluno["email"])


def adicionar_alunos(vnome, vemail):
    cur.execute("INSERT INTO aluno(nome, email) VALUES('%s', '%s');" % (vnome, vemail))
    con.commit()


def remover_alunos(vnome):
    cur.execute("DELETE FROM aluno WHERE nome='%s'" % (vnome))
    con.commit()


def atualizar_alunos(vnome, vemail):
    cur.execute("UPDATE aluno SET email='%s' WHERE nome='%s'" % (vemail, vnome))
    con.commit()


listar_alunos()

operacao = True

while operacao:
    acao = input("Qual operação deseja realizar?\n(I)nserir Aluno\n(R)emover Aluno\n(A)tualizar Aluno\n")
    if acao.lower() == "i":
        adicionar_alunos(input("Qual o nome do novo aluno?\n"), input("Qual o e-mail do novo aluno?\n"))
        listar_alunos()

    elif acao.lower() == "r":
        remover_alunos(input("Qual o nome do aluno que deseja remover?\n"))
        listar_alunos()

    elif acao.lower() == "a":
        atualizar_alunos(input("Qual o nome do aluno para ser atualizado?\n"), input("Qual o novo e-mail?\n"))
        listar_alunos()

    if input("Deseja realizar uma nova operação? S/N\n").lower() == "n":
        print("Obrigado, volte sempre!")
        operacao = False

listar_alunos()
