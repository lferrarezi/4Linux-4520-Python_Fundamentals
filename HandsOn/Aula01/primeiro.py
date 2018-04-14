#x = input("Digite aqui o valor de x:")
#print(x)

CONSTANTE = 9.8
print(CONSTANTE)

numero = 10
print(numero)

decimal = 3/4
print(decimal)

texto = "4Linux Devops"
print(texto)

aluno = {
    "nome": "Luiz",
    "email": "lferrarezi@gmail.com",
    "endereco": {
        "logradouro": "R. Vergueiro",
        "numero": "3057",
        "cidade": "São Paulo"
    }
}
print(aluno)
print(aluno["nome"])
print(aluno["email"])
print(aluno["endereco"]["logradouro"], aluno["endereco"]["numero"])

#print(CONSTANTE, numero, decimal, texto, aluno["nome"])

print(type(aluno), type(decimal), type(numero))

lista = ["joao", "gabriel", "luiz", "pedro"]
print(lista[1])

aluno0 = {
    "nome": "Luiz",
    "email": "lferrarezi@gmail.com",
    "endereco": {
        "logradouro": "R. Vergueiro",
        "numero": "3057",
        "cidade": "São Paulo"
    }
}

aluno1 = {
    "nome": "Alberto",
    "email": "alberto@gmail.com",
    "endereco": {
        "logradouro": "R. Chaves",
        "numero": "100",
        "cidade": "São Bernardo do Campo"
    }
}

alunos = [aluno0, aluno1]

print(alunos[0])
time.sleep
print(alunos[0]["nome"])