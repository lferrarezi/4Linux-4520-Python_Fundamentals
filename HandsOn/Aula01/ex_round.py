nota = 3.1415926535897932384626433

x = []
x.append(nota)
x.append(round(nota,0))
x.append(round(nota,1))
x.append(round(nota,2))
x.append(round(nota,3))

print(x)


lista = []
lista.append(float(input("Digite um número decimal")))
lista.append(float(input("Digite um número decimal")))
lista.append(float(input("Digite um número decimal")))

print(round(lista[0]+lista[1]+lista[2],1))